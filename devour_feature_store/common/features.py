from datetime import timedelta

from common.data_sources import *
from common.entities import *
from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32, Int64, String

fv_product_general_score = FeatureView(
    name="fv_product_general_score",
    entities=[et_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="general_score", dtype=Float32),
    ],
    source=ds_file_product_general_score,
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
    source=ds_push_product_general_score,
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
    source=ds_push_user_propensity_score,
)

fv_push_buy_it_again_feature_group = FeatureView(
    name="fv_push_buy_it_again_feature_group",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="buy_it_again_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_buy_it_again_feature_group,
)

fv_push_cheap_product_black_list = FeatureView(
    name="fv_push_cheap_product_black_list",
    entities=[et_use_case],
    ttl=timedelta(days=365),
    schema=[
        Field(name="cheap_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_cheap_product_black_list,
)

fv_push_cold_start_retrieval = FeatureView(
    name="fv_push_cold_start_retrieval",
    entities=[et_lang_store],
    ttl=timedelta(days=365),
    schema=[
        Field(name="cold_start_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_cold_start_retrieval,
)

fv_push_dssm_retrieval = FeatureView(
    name="fv_push_dssm_retrieval",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="dssm_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_dssm_retrieval,
)

fv_push_grocery_best_seller_v2 = FeatureView(
    name="fv_push_grocery_best_seller_v2",
    entities=[et_ethnicity_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="long_term_products", dtype=String),  # TODO
        Field(name="short_term_products", dtype=String),  # TODO
        Field(name="long_term_products_ethnic_tag", dtype=String),  # TODO
        Field(name="short_term_products_ethnic_tag", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_grocery_best_seller_v2,
)

fv_push_local_comp_items = FeatureView(
    name="fv_push_local_comp_items",
    entities=[et_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="comp_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_comp_items,
)

fv_push_local_imp_discounting = FeatureView(
    name="fv_push_local_imp_discounting",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="imp_discounting_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_imp_discounting,
)

fv_push_local_previous_pdp = FeatureView(
    name="fv_push_local_previous_pdp",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="previous_pdp_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_previous_pdp,
)

fv_push_local_product_video = FeatureView(
    name="fv_push_local_product_video",
    entities=[et_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="video_id", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_product_video,
)

fv_push_local_sales_org_hero_products = FeatureView(
    name="fv_push_local_sales_org_hero_products",
    entities=[et_sales_org],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sku_list_5k", dtype=String),  # TODO
        Field(name="sku_list_10k", dtype=String),  # TODO
        Field(name="sku_list_15k", dtype=String),  # TODO
        Field(name="sku_list_20k", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_sales_org_hero_products,
)

fv_push_local_sim_items = FeatureView(
    name="fv_push_local_sim_items",
    entities=[et_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sim_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_local_sim_items,
)

fv_push_long_term_buy_again_retrieval = FeatureView(
    name="fv_push_long_term_buy_again_retrieval",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="long_term_bia_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_long_term_buy_again_retrieval,
)

fv_push_masgusto_hp_retrieval = FeatureView(
    name="fv_push_masgusto_hp_retrieval",
    entities=[et_prodEth_salesReg],
    ttl=timedelta(days=365),
    schema=[
        Field(name="masgusto_hp_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_masgusto_hp_retrieval,
)

fv_push_new_product_retrieval = FeatureView(
    name="fv_push_new_product_retrieval",
    entities=[et_ethnicity_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="new_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_new_product_retrieval,
)

fv_push_newuser_search_keyword = FeatureView(
    name="fv_push_newuser_search_keyword",
    entities=[et_lang_store_kw],
    ttl=timedelta(days=365),
    schema=[
        Field(name="atc_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_newuser_search_keyword,
)

fv_push_on_sale_personalized_ranking = FeatureView(
    name="fv_push_on_sale_personalized_ranking",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="l1_all_list", dtype=String),  # TODO
        Field(name="l1_l2_list", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_on_sale_personalized_ranking,
)

fv_push_product_features_v2 = FeatureView(
    name="fv_push_product_features_v2",
    entities=[et_product],
    ttl=timedelta(days=365),
    schema=[
        Field(name="title_emb", dtype=String),
        Field(name="vendor_id", dtype=Int64),
        Field(name="newuser_order_ct_7d", dtype=Int64),
        Field(name="newuser_order_atc_rate_30d", dtype=Float32),
        Field(name="subcategory_id", dtype=Int64),
        Field(name="category_id", dtype=Int64),
        Field(name="qty_7", dtype=Int64),
        Field(name="pdp_view_ct_30", dtype=Int64),
        Field(name="post_ct_30", dtype=Int64),
        Field(name="post_ct_7", dtype=Int64),
        Field(name="newuser_order_ct_30d", dtype=Int64),
        Field(name="ds", dtype=String),
        Field(name="newuser_pdp_view_ct_30d", dtype=Int64),
        Field(name="price", dtype=Float32),
        Field(name="order_ct_30", dtype=Int64),
        Field(name="qty_30", dtype=Int64),
        Field(name="pdp_view_ct_7", dtype=Int64),
        Field(name="product_id", dtype=Int64),
        Field(name="ethnicity_p", dtype=String),
        Field(name="tier", dtype=Int64),
        Field(name="order_ct_7", dtype=Int64),
    ],
    online=True,
    offline=True,
    source=ds_push_product_features_v2,
)

fv_push_secondary_store_rfy = FeatureView(
    name="fv_push_secondary_store_rfy",
    entities=[et_store],
    ttl=timedelta(days=365),
    schema=[
        Field(name="rfy_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_secondary_store_rfy,
)

fv_push_topx_retrieval = FeatureView(
    name="fv_push_topx_retrieval",
    entities=[et_ethnicity_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="topx_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_topx_retrieval,
)

fv_push_user_in_cart_history = FeatureView(
    name="fv_push_user_in_cart_history",
    entities=[et_user],
    ttl=timedelta(days=365),
    schema=[
        Field(name="in_cart_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_user_in_cart_history,
)

fv_push_waterfall_secondary_product = FeatureView(
    name="fv_push_waterfall_secondary_product",
    entities=[et_store],
    ttl=timedelta(days=365),
    schema=[
        Field(name="secondary_products_lst", dtype=String),  # TODO
    ],
    online=True,
    offline=True,
    source=ds_push_waterfall_secondary_product,
)
