
from feast import (
    Entity,
    ValueType
)

et_user = Entity(
    name="et_user",
    join_keys=["user_id"],
    value_type=ValueType.INT64,
    description="User ID"
)
et_product = Entity(
    name="et_product",
    join_keys=["product_id"],
    value_type=ValueType.INT64,
    description="Product ID"
)

et_ethnicity_user = Entity(
    name="et_user_ethnicity",
    join_keys=["ethnicity_user"],
    value_type=ValueType.STRING,
    description="User Ethnicity"
)
