#!/bin/zsh

export fs_external_url =
# test pod : kubectl run curlpod --rm -it --restart=Never --image=curlimages/curl:latest -- sh

curl "http://localhost:8002/get-online-features" \
	--json '{
		"features": ["product_general_score_fresh:general_score"],
		"entities": {"product_id": [9]}
	}' \
	| jq


#	--json '{
#		"features": ["product_general_score:general_score", "product_general_score:event_timestamp"],
#		"entities": {"product_id": [0]}
#	}' \
#	| jq

#	--json '{
#		"features": ["zipcode_features:state", "zipcode_features:population"],
#		"entities": {"zipcode": [7675, 94538]}
#	}' \


feast get-online-features -f fv_push_product_general_score:general_score -e product_id=9000001 -e product_id=1001

curl "http://${fs_external_url}/get-online-features" \
--json '{
		"features": ["fv_push_product_bestseller_ethnicity_tag:short_term_products_ethnic_tag"],
		"entities": {"ethnicity_user": ["Chinese"]}
	}' | jq

curl "http://${fs_external_url}/get-online-features" --json '{"features": ["fv_push_user_propensity_score:user_type","fv_push_user_propensity_score:score"], "entities": {"user_id": [7216502, 93590]}}' | jq

curl "http://${fs_internal_url}/get-online-features" --json '{"features": ["fv_push_user_propensity_score:user_type","fv_push_user_propensity_score:score"], "entities": {"user_id": [7216502, 93590]}}' | jq

curl "http://${fs_external_url}/get-online-features" --json '{"features": ["fv_push_user_propensity_score:score"], "entities": {"user_id": [7216502]}}' | jq
curl "http://${fs_internal_url}/feast/get-online-features" --json '{"features": ["fv_push_user_propensity_score:score"], "entities": {"user_id": [7216502]}}' | jq
feast get-online-features -f fv_push_category_ranking:l1_all_list -e user_id=7216502

