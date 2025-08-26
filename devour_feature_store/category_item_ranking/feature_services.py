from common.features import *
from feast import FeatureService

fs_category_ranking_generic_v1 = FeatureService(
    name="fs_category_ranking_generic_v1",
    features=[
        fv_product_general_score,  # [["general_score"]] will cause pyright error, TODO talk to Feast team
    ],
    owner="shumin",
)

fs_category_ranking_generic_v2 = FeatureService(
    name="fs_category_ranking_generic_v2",
    features=[
        fv_push_product_general_score,
    ],
    owner="shumin",
)

fs_test_v1 = FeatureService(
    name="fs_test_v2", features=[fv_push_user_propensity_score]
)
