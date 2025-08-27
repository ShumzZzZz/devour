from feast import Entity, ValueType

et_user = Entity(
    name="et_user",
    join_keys=["user_id"],
    value_type=ValueType.INT64,
    description="User ID",
)

et_product = Entity(
    name="et_product",
    join_keys=["product_id"],
    value_type=ValueType.INT64,
    description="Product ID",
)

et_ethnicity_user = Entity(
    name="et_user_ethnicity",
    join_keys=["ethnicity_user"],
    value_type=ValueType.STRING,
    description="User Ethnicity",
)

et_ethnicity_product = Entity(
    name="et_ethnicity_product",
    join_keys=["ethnicity_product"],
    value_type=ValueType.STRING,
    description="Product Ethnicity",
)

et_use_case = Entity(
    name="et_use_case",
    join_keys=["use_case_id"],
    value_type=ValueType.STRING,
    description="Use Case ID",
)

et_lang_store = Entity(
    name="et_lang_store",
    join_keys=["lang_store"],
    value_type=ValueType.STRING,
    description="Language + Store ID",
)

et_lang_store_kw = Entity(
    name="et_lang_store_kw",
    join_keys=["lang_store_kw"],
    value_type=ValueType.STRING,
    description="Language + Store ID + Keyword",
)

et_store = Entity(
    name="et_store",
    join_keys=["store"],
    value_type=ValueType.STRING,
    description="Language | Store ID, such as lang_xxx | store_xxx",
)

et_sales_org = Entity(
    name="et_sales_org",
    join_keys=["sales_org_id"],
    value_type=ValueType.STRING,
    description="Sales Org ID",
)

et_prodEth_salesReg = Entity(
    name="et_prodEth_salesOrg",
    join_keys=["prodethnicity_salesregion"],
    value_type=ValueType.STRING,
    description="Product Ethnicity + Sales Region ID",
)
