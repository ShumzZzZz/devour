#!/bin/bash

k create ns feast
k config set-context --current --namespace feast

k get nodes --no-headers | awk '$3 != "control-plane" {print $1}' | while read node; do
  k label node "$node" dedicated=featurestore --overwrite
  k taint node "$node" dedicated=featurestore:NoExecute --overwrite
done


curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/feast_scheduling_pref.yaml
helm install kyverno kyverno/kyverno -n kyverno --create-namespace \
  --values feast_scheduling_pref.yaml

k wait --for=condition=available --timeout=5m deployment/kyverno-admission-controller -n kyverno
k wait --for=condition=available --timeout=5m deployment/kyverno-background-controller -n kyverno
k wait --for=condition=available --timeout=5m deployment/kyverno-cleanup-controller -n kyverno
k wait --for=condition=available --timeout=5m deployment/kyverno-reports-controller -n kyverno

curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/kyverno_cluster_policy.yaml
k apply -f kyverno_cluster_policy.yaml


git clone https://github.com/prometheus-operator/kube-prometheus.git
k apply --server-side -f kube-prometheus/manifests/setup
k wait \
	--for condition=Established \
	--all CustomResourceDefinition \
	--namespace=monitoring
k apply -f kube-prometheus/manifests/
# https://github.com/prometheus-operator/kube-prometheus/blob/main/docs/access-ui.md
# kp --namespace monitoring svc/grafana 3000



curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/prerequisite_setup.yaml
k apply -f prerequisite_setup.yaml

k wait --for=condition=available --timeout=5m deployment/redis-feast
k wait --for=condition=available --timeout=5m deployment/postgres-feast

#curl -sSL https://raw.githubusercontent.com/feast-dev/feast/refs/heads/master/infra/feast-operator/dist/install.yaml -o feast_operator_install.yaml
curl -sSL https://raw.githubusercontent.com/ShumzZzZz/feast/refs/heads/customize-operator/infra/feast-operator/dist/install.yaml -o feast_operator_install.yaml
k apply -f feast_operator_install.yaml

k wait --for=condition=available --timeout=5m deployment/feast-operator-controller-manager -n feast-operator-system

curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/feast.yaml
k apply -f feast.yaml
sleep 3
k wait --for=condition=available --timeout=8m deployment/feast-example






k exec deployment/postgres-feast -- psql -h localhost -U feastuser feastdb -c '\dt'
k exec deployment/feast-example -itc online -- bash # feast version


# cronjob & customization
kubectl get feast/example -o jsonpath='{.status.applied.cronJob.containerConfigs.commands}'
feast materialize-incremental $(date -u +'%Y-%m-%dT%H:%M:%S')
#feast materialize '2022-01-01T00:00:00' $(date -u +"%Y-%m-%dT%H:%M:%S")
#kubectl patch feast/example --patch '{"spec":{"cronJob":{"containerConfigs":{"commands":["pip install -r ../requirements.txt","cd ../ && python run.py"]}}}}' --type=merge

k create job --from=cronjob/feast-example feast-example-apply
k wait --for=condition=complete --timeout=8m job/feast-example-apply
k logs job/feast-example-apply --all-containers=true

# port-forward
kp svc/feast-example-registry 8001:80 &
# kp svc/postgre-service 8001:5432 &
kp svc/feast-example-online 8002:80 &
kp svc/feast-example-ui 8003:80 &

kill "$(lsof -i :8001 | awk 'NR>1 {print $2}' | sort -nu)"
kill "$(lsof -i :8002 | awk 'NR>1 {print $2}' | sort -nu)"
kill "$(lsof -i :8003 | awk 'NR>1 {print $2}' | sort -nu)"

helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard \
	--create-namespace --namespace kubernetes-dashboard \
	--set metricsScraper.enabled=true

kubectl create serviceaccount admin-user -n kubernetes-dashboard
kubectl create clusterrolebinding admin-user-binding \
  --clusterrole=cluster-admin \
  --serviceaccount=kubernetes-dashboard:admin-user
kubectl -n kubernetes-dashboard create token admin-user


curl -L https://istio.io/downloadIstio | sh -
cd $(ls | grep istio)
export PATH="$PATH:$PWD/bin"


cat <<EOF | kubectl apply -f -
apiVersion: projectcalico.org/v3
kind: FelixConfiguration
metadata:
  name: default
spec:
  # Disable connect-time load balancing entirely
  bpfConnectTimeLoadBalancing: Disabled
EOF

kubectl -n calico-system rollout restart daemonset calico-node

cat <<EOF > istio-cni.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  components:
    cni:
      namespace: istio-system
      enabled: true
EOF
istioctl install -f istio-cni.yaml -y

kubectl -n istio-system patch svc istio-ingressgateway --type='merge' -p '{
  "spec": {
    "type": "NodePort",
    "ports": [
      {
        "name": "status-port",
        "port": 15021,
        "targetPort": 15021,
        "protocol": "TCP",
        "nodePort": 30021
      },
      {
        "name": "http2",
        "port": 80,
        "targetPort": 8080,
        "protocol": "TCP",
        "nodePort": 30080
      },
      {
        "name": "https",
        "port": 443,
        "targetPort": 8443,
        "protocol": "TCP",
        "nodePort": 30443
      },
      {
        "name": "tcp-postgres",
        "port": 5432,
        "targetPort": 5432,
        "protocol": "TCP",
        "nodePort": 30432
      }
    ]
  }
}'

curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/service_exposure/gateway_virtualService.yaml
k apply -f gateway_virtualService.yaml

#curl -sSLO https://raw.githubusercontent.com/ShumzZzZz/devour/refs/heads/main/tofu/scripts/feast_setup/istio-hostport-ingress.yaml
#istioctl install -f istio-hostport-ingress.yaml -y

kubectl get <kind> <name> -n <ns> -oyaml \
  | yq eval '.metadata.name = "new-name" | del(.metadata.uid, .metadata.resourceVersion)' - \

#kubectl get <kind> <name> -n <ns> -o json \
#  | jq 'del(.metadata.namespace, .metadata.resourceVersion, .metadata.uid, .metadata.creationTimestamp, .metadata.annotations.creationTimestamp)' \


k delete --ignore-not-found=true -f kube-prometheus/manifests/ -f kube-prometheus/manifests/setup
k delete -f feast.yaml
k delete -f feast_operator_install.yaml
k delete -f prerequisite_setup.yaml


# for vs, get ingress -n istio-system and get the ALB address, add a cname record to Route53 and create a VS for it to point to
# k get secrets -n jenkins jenkins-operator-credentials-ci-only -o 'jsonpath={.data.password}' | base64 -d
#

kubectl annotate ingress -n istio-system web-ingress 'alb.ingress.kubernetes.io/load-balancer-attributes=deletion_protection.enabled=true,routing.http.preserve_host_header.enabled=true' --overwrite
kubectl annotate ingress -n istio-system web-ingress alb.ingress.kubernetes.io/ssl-redirect='443' --overwrite
kubectl annotate ingress -n istio-system web-ingress 'alb.ingress.kubernetes.io/certificate-arn=arn:aws:acm:us-east-2:134057274056:certificate/f9f40367-5e81-4cff-8106-7b293b9bfb3f' --overwrite
kubectl annotate ingress -n istio-system web-ingress 'alb.ingress.kubernetes.io/certificate-arn=# arn:aws:acm:us-east-2:529086600118:certificate/cc43398f-27bf-47f6-99ff-7fec0e9059ac' --overwrite

# run awscli
kubectl run awscli-test -n jenkins \
  --image=amazon/aws-cli --restart=Never -it --rm \
  --command -- /bin/sh

aws sts get-caller-identity  # to get the current role




