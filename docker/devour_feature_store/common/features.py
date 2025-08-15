from datetime import timedelta
from feast import (
	FeatureView,
	Field,
)
from feast.types import Float32, String

from common.data_sources import *
from common.entities import *

fv_product_general_score = FeatureView(
	name="fv_product_general_score",
	entities=[et_product],
	ttl=timedelta(days=365),
	schema=[
		Field(name="general_score", dtype=Float32),
	],
	source=ds_file_product_general_score
)

fv_push_product_general_score = FeatureView(
	name="fv_push_product_general_score",
	entities=[et_product],
	ttl=timedelta(days=365),
	schema=[
		Field(name="general_score", dtype=Float32),
	],
	online=True,
	offline=True,
	source=ds_push_product_general_score
	# has to be push source, otherwise the push source will not be registered and found
)

fv_push_product_bestseller_ethnicity_tag = FeatureView(
	name="fv_push_product_bestseller_ethnicity_tag",
	entities=[et_ethnicity_user],
	ttl=timedelta(days=365),
	schema=[
		Field(name="short_term_products_ethnic_tag", dtype=String),
		Field(name="long_term_products_ethnic_tag", dtype=String),
	],
	online=True,
	offline=True,
	source=ds_push_product_bestseller_ethnicity_tag
)

fv_push_user_propensity_score = FeatureView(
	name="fv_push_user_propensity_score",
	entities=[et_user],
	ttl=timedelta(days=365),
	schema=[
		Field(name="user_type", dtype=String),
		Field(name="score", dtype=Float32),
	],
	online=True,
	offline=True,
	source=ds_push_user_propensity_score
)
