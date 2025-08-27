from feast import FileSource, PushSource
from feast.data_format import ParquetFormat

ds_file_product_general_score = FileSource(
    name="ds_file_product_general_score",
    path="data/product_features/product_general_scores.parquet",
    file_format=ParquetFormat(),
    timestamp_field="event_timestamp",
)

ds_push_product_general_score = PushSource(
    name="ds_push_product_general_score",
    batch_source=ds_file_product_general_score,
)


ds_file_product_bestseller_ethnicity_tag = FileSource(
    name="ds_file_product_bestseller_ethnicity_tag",
    path="data/bestseller_features/product_bestseller_ethnicity_tag.parquet",
    file_format=ParquetFormat(),
    timestamp_field="event_timestamp",
)

ds_push_product_bestseller_ethnicity_tag = PushSource(
    name="ds_push_product_bestseller_ethnicity_tag",
    batch_source=ds_file_product_bestseller_ethnicity_tag,
)


ds_file_user_propensity_score = FileSource(
    name="ds_file_user_propensity_score",
    path="data/bestseller_features/user_propensity_score.parquet",
    file_format=ParquetFormat(),
    timestamp_field="event_timestamp",
)

ds_push_user_propensity_score = PushSource(
    name="ds_push_user_propensity_score",
    batch_source=ds_file_user_propensity_score,
)

ds_file_buy_it_again_feature_group = FileSource(
    name="ds_file_buy_it_again_feature_group",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/buy-it-again-feature-group/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_buy_it_again_feature_group = PushSource(
    name="ds_push_buy_it_again_feature_group",
    batch_source=ds_file_buy_it_again_feature_group,
)


ds_file_cheap_product_black_list = FileSource(
    name="df_file_cheap_product_black_list",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/cheap_product_black_list/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_cheap_product_black_list = PushSource(
    name="ds_push_cheap_product_black_list",
    batch_source=ds_file_cheap_product_black_list,
)

ds_file_cold_start_retrieval = FileSource(
    name="ds_file_cold_start_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/cold-start-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_cold_start_retrieval = PushSource(
    name="ds_push_cold_start_retrieval",
    batch_source=ds_file_cold_start_retrieval,
)

ds_file_dssm_retrieval = FileSource(
    name="ds_file_dssm_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/dssm-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_dssm_retrieval = PushSource(
    name="ds_push_dssm_retrieval",
    batch_source=ds_file_dssm_retrieval,
)

ds_file_grocery_best_seller_v2 = FileSource(
    name="ds_file_grocery_best_seller_v2",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/grocery-best-seller-v2/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_grocery_best_seller_v2 = PushSource(
    name="ds_push_grocery_best_seller_v2",
    batch_source=ds_file_grocery_best_seller_v2,
)

ds_file_local_comp_items = FileSource(
    name="ds_file_local_comp_items",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-comp-items/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_comp_items = PushSource(
    name="ds_push_local_comp_items",
    batch_source=ds_file_local_comp_items,
)

ds_file_local_imp_discounting = FileSource(
    name="ds_file_local_imp_discounting",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-imp-discounting/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_imp_discounting = PushSource(
    name="ds_push_local_imp_discounting",
    batch_source=ds_file_local_imp_discounting,
)

ds_file_local_previous_pdp = FileSource(
    name="ds_file_local_previous_pdp",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-previous-pdp/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_previous_pdp = PushSource(
    name="ds_push_local_previous_pdp",
    batch_source=ds_file_local_previous_pdp,
)

ds_file_local_product_video = FileSource(
    name="ds_file_local_product_video",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-product-video/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_product_video = PushSource(
    name="ds_push_local_product_video",
    batch_source=ds_file_local_product_video,
)

ds_file_local_sales_org_hero_products = FileSource(
    name="ds_file_local_sales_org_hero_products",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-sales-org-hero-products/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_sales_org_hero_products = PushSource(
    name="ds_push_local_sales_org_hero_products",
    batch_source=ds_file_local_sales_org_hero_products,
)

ds_file_local_sim_items = FileSource(
    name="ds_file_local_sim_items",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/local-sim-items/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_local_sim_items = PushSource(
    name="ds_push_local_sim_items",
    batch_source=ds_file_local_sim_items,
)

ds_file_long_term_buy_again_retrieval = FileSource(
    name="ds_file_long_term_buy_again_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/long-term-buy-again-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_long_term_buy_again_retrieval = PushSource(
    name="ds_push_long_term_buy_again_retrieval",
    batch_source=ds_file_long_term_buy_again_retrieval,
)

ds_file_masgusto_hp_retrieval = FileSource(
    name="ds_file_masgusto_hp_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/masgusto-hp-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_masgusto_hp_retrieval = PushSource(
    name="ds_push_masgusto_hp_retrieval",
    batch_source=ds_file_masgusto_hp_retrieval,
)

ds_file_new_product_retrieval = FileSource(
    name="ds_file_new_product_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/new-product-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_new_product_retrieval = PushSource(
    name="ds_push_new_product_retrieval",
    batch_source=ds_file_new_product_retrieval,
)

ds_file_newuser_search_keyword = FileSource(
    name="ds_file_newuser_search_keyword",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/newuser-search-keyword/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",  #  TODO change to EventTime
)

ds_push_newuser_search_keyword = PushSource(
    name="ds_push_newuser_search_keyword",
    batch_source=ds_file_newuser_search_keyword,
)

ds_file_on_sale_personalized_ranking = FileSource(
    name="ds_file_on_sale_personalized_ranking",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/on-sale-personalized-ranking/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_on_sale_personalized_ranking = PushSource(
    name="ds_push_on_sale_personalized_ranking",
    batch_source=ds_file_on_sale_personalized_ranking,
)

ds_file_product_features_v2 = FileSource(
    name="ds_file_product_features_v2",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/product-features-v2/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_product_features_v2 = PushSource(
    name="ds_push_product_features_v2",
    batch_source=ds_file_product_features_v2,
)

ds_file_secondary_store_rfy = FileSource(
    name="ds_file_secondary_store_rfy",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/secondary-store-rfy/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_secondary_store_rfy = PushSource(
    name="ds_push_secondary_store_rfy",
    batch_source=ds_file_secondary_store_rfy,
)

ds_file_topx_retrieval = FileSource(
    name="ds_file_topx_retrieval",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/topx-retrieval/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_topx_retrieval = PushSource(
    name="ds_push_topx_retrieval",
    batch_source=ds_file_topx_retrieval,
)

ds_file_user_in_cart_history = FileSource(
    name="ds_file_user_in_cart_history",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/user-in-cart-history/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",  # TODO
)

ds_push_user_in_cart_history = PushSource(
    name="ds_push_user_in_cart_history",
    batch_source=ds_file_user_in_cart_history,
)

ds_file_waterfall_secondary_product = FileSource(
    name="ds_file_waterfall_secondary_product",
    path="s3://sagemaker-us-west-2-551230544614/featurestore/hp-online-redis-test/waterfall-secondary-product/",
    file_format=ParquetFormat(),
    timestamp_field="update_time",
)

ds_push_waterfall_secondary_product = PushSource(
    name="ds_push_waterfall_secondary_product",
    batch_source=ds_file_waterfall_secondary_product,
)
