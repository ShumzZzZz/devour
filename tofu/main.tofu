terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.100.0"
    }
  }
}

provider "aws" {
  region  = "us-west-2"
  profile = var.environment
  default_tags {
    tags = var.default_project_tags
  }
}

resource "aws_vpc" "devour_k8s" {
  cidr_block           = "10.10.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "devour-k8s-vpc"
  }
}

resource "aws_internet_gateway" "devour_k8s_igw" {
  vpc_id = aws_vpc.devour_k8s.id

  tags = {
    Name = "k8s-igw"
  }
}

# Public subnet (example for one AZ)
resource "aws_subnet" "public_subnet_a" {
  vpc_id                  = aws_vpc.devour_k8s.id
  cidr_block              = "10.10.1.0/24"
  availability_zone       = "us-west-2a"
  map_public_ip_on_launch = true

  tags = {
    Name = "devour-k8s-public-subnet-a"
  }
}

# Route table for the public subnet
resource "aws_route_table" "devour_k8s_public_rt" {
  vpc_id = aws_vpc.devour_k8s.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.devour_k8s_igw.id
  }

  tags = {
    Name = "devour-k8s-public-rt"
  }
}

# Subnet association with the route table
resource "aws_route_table_association" "devour_k8s_public_subnet_a_assoc" {
  subnet_id      = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.devour_k8s_public_rt.id
}


resource "aws_security_group" "devour_k8s" {
  name        = "devour-k8s-sg"
  description = "Security group for Devour K8s"
  vpc_id      = aws_vpc.devour_k8s.id

  tags = {
    Name = "devour-k8s-sg"
  }
}

resource "aws_vpc_security_group_egress_rule" "allow_all_outbound_ipv4" {
  description       = "allow all outbound ipv4"
  security_group_id = aws_security_group.devour_k8s.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

resource "aws_vpc_security_group_ingress_rule" "all_traffic_within_vpc" {
  ip_protocol       = "-1"
  from_port         = -1
  to_port           = -1
  cidr_ipv4         = aws_vpc.devour_k8s.cidr_block
  security_group_id = aws_security_group.devour_k8s.id
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
  description       = "allow ssh"
  security_group_id = aws_security_group.devour_k8s.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_ingress_rule" "allow_nodeports" {
  description       = "allow nodeports"
  security_group_id = aws_security_group.devour_k8s.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 30000
  ip_protocol       = "tcp"
  to_port           = 32767
}

resource "aws_vpc_security_group_ingress_rule" "allow_kubectl" {
  description       = "allow kubectl"
  security_group_id = aws_security_group.devour_k8s.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 6443
  ip_protocol       = "tcp"
  to_port           = 6443
}

resource "aws_vpc_security_group_ingress_rule" "allow_calico_ipip" {
  description       = "Allow Calico IP in IP encapsulation traffic on control plane nodes"
  security_group_id = aws_security_group.devour_k8s.id
  cidr_ipv4         = aws_vpc.devour_k8s.cidr_block
  ip_protocol       = "4"
  from_port         = -1
  to_port           = -1
}

resource "aws_iam_policy" "s3_join_command_policy" {
  name        = "s3-join-command-policy"
  description = "Allows access to K8s join command in S3"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = ["s3:*"],
        Resource = "*"
        Effect = "Allow",
      },
      {
        "Action" : "ec2:*",
        "Resource" : "*"
        "Effect" : "Allow",
      },
      {
        "Action" : "elasticloadbalancing:*",
        "Resource" : "*"
        "Effect" : "Allow",
      },
      {
        "Action" : "cloudwatch:*",
        "Resource" : "*"
        "Effect" : "Allow",
      },
      {
        "Action" : "autoscaling:*",
        "Resource" : "*"
        "Effect" : "Allow",
      },
      {
        "Effect" : "Allow",
        "Action" : "iam:CreateServiceLinkedRole",
        "Resource" : "*",
        "Condition" : {
          "StringEquals" : {
            "iam:AWSServiceName" : [
              "autoscaling.amazonaws.com",
              "ec2scheduled.amazonaws.com",
              "elasticloadbalancing.amazonaws.com",
              "spot.amazonaws.com",
              "spotfleet.amazonaws.com",
              "transitgateway.amazonaws.com"
            ]
          }
        }
      }
    ]
  })
}

resource "aws_iam_role" "ec2_k8s_node_role" {
  name = "ec2-k8s-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "s3_attach" {
  role       = aws_iam_role.ec2_k8s_node_role.name
  policy_arn = aws_iam_policy.s3_join_command_policy.arn
}

resource "aws_iam_instance_profile" "ec2_k8s_node_profile" {
  name = "ec2-k8s-node-profile"
  role = aws_iam_role.ec2_k8s_node_role.name
}

resource "aws_instance" "k8s_control_plane_nodes" {
  count                  = 1
  ami                    = "ami-03f8acd418785369b" # "ami-0b6d6dacf350ebc82"
  instance_type          = "t2.medium"
  key_name               = "shumin-test"
  iam_instance_profile   = aws_iam_instance_profile.ec2_k8s_node_profile.name
  subnet_id              = aws_subnet.public_subnet_a.id
  vpc_security_group_ids = [aws_security_group.devour_k8s.id]

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
  }

  tags = {
    Name = "k8s-control-plane"
  }
}

# AWS Instances for Kubernetes Worker Nodes
resource "aws_instance" "k8s_worker_nodes" {
  count                  = 2
  ami                    = "ami-03f8acd418785369b"
  instance_type          = "t2.xlarge"
  key_name               = "shumin-test"
  iam_instance_profile   = aws_iam_instance_profile.ec2_k8s_node_profile.name
  subnet_id              = aws_subnet.public_subnet_a.id
  vpc_security_group_ids = [aws_security_group.devour_k8s.id]

  root_block_device {
    volume_size = 100
    volume_type = "gp3"
  }

  tags = {
    Name = "k8s-worker-node-${count.index}"
  }
}


locals {
  cp_private_ips = join(",", aws_instance.k8s_control_plane_nodes[*].private_ip)
  wk_private_ips = join(",", aws_instance.k8s_worker_nodes[*].private_ip)
  cp_public_ips  = join(",", aws_instance.k8s_control_plane_nodes[*].public_ip)
  # give dummy ips for testing the script template
  # cp_private_ips = "1.1.1.1"
  # wk_private_ips = "4.4.4.4,5.5.5.5"
  # cp_public_ips  = "1.1.1.2"
  init_script = templatefile("scripts/init.sh.tftpl", {
    cp_private_ips        = local.cp_private_ips,
    cp_public_ips         = local.cp_public_ips,
    wk_private_ips        = local.wk_private_ips,
    containerd_version    = var.containerd_version,
    runc_version          = var.runc_version
    cni_plugin_version    = var.cni_plugin_version,
    tigera_calico_version = var.tigera_calico_version,
    timestamp_suffix      = timestamp()
  })
  all_nodes = merge(
    { for idx, instance in aws_instance.k8s_control_plane_nodes : "cp-${idx}" => instance },
    { for idx, instance in aws_instance.k8s_worker_nodes : "wk-${idx}" => instance }
  )
}


resource "local_file" "init_script" {
  content  = local.init_script
  filename = "init_nodes.sh"
}

resource "null_resource" "init_nodes" {
  for_each = local.all_nodes

  depends_on = [
    aws_instance.k8s_control_plane_nodes,
    aws_instance.k8s_worker_nodes
  ]

  connection {
    type        = "ssh"
    host        = each.value.public_ip
    user        = "ubuntu"
    private_key = file("~/.ssh/shumin-test.pem")
  }

  provisioner "remote-exec" {
    inline = [
      <<-EOF
        cat <<'EOF2' > /tmp/init_nodes.sh
        ${local.init_script}
        EOF2
        chmod +x /tmp/init_nodes.sh
        sudo /tmp/init_nodes.sh
      EOF
    ]
  }
}

# output "rendered_init_script" {
#   value = local.init_script
# }

output "vpc_id" {
  value = aws_vpc.devour_k8s.id
}

output "subnet_id" {
  value = aws_subnet.public_subnet_a.id
}

output "security_group_id" {
  value = aws_security_group.devour_k8s.id
}

output "cp_private_ips" {
  value = aws_instance.k8s_control_plane_nodes[*].private_ip
}

output "wk_public_ips" {
  value = aws_instance.k8s_worker_nodes[*].public_ip
}

output "cp_public_ips" {
  value = aws_instance.k8s_control_plane_nodes[*].public_ip
}