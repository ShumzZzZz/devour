from feast import FeatureService
from common.features import *

fs_category_ranking_generic_v1 = FeatureService(
	name="fs_category_ranking_generic_v1",
	features=[
		fv_product_general_score[["general_score"]],
	],
	owner="shumin"
)

fs_category_ranking_generic_v2 = FeatureService(
	name="fs_category_ranking_generic_v2",
	features=[
		fv_push_product_general_score[["general_score"]],
	],
	owner="shumin"
)