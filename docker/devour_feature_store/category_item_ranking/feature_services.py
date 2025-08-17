from common.features import *
from feast import FeatureService

fs_category_ranking_generic_v1 = FeatureService(
    name="fs_category_ranking_generic_v1",
    features=[
        fv_product_general_score[["general_score"]],
    ],
    owner="shumin",
)

fs_category_ranking_generic_v2 = FeatureService(
    name="fs_category_ranking_generic_v2",
    features=[
        fv_push_product_general_score[["general_score"]],
    ],
    owner="shumin",
)
