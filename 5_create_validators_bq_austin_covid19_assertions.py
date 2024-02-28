import great_expectations as gx

# Create the context including the context folder locally
context = gx.get_context()


covid10_assertions_asset = context.get_datasource("bq_austin").get_asset(
    "covid19_assertions"
)
covid19_assertions_request = covid10_assertions_asset.build_batch_request()

# # Get validator from the suite
covid19_assertions_validator = context.get_validator(
    batch_request=covid19_assertions_request,
    expectation_suite_name="covid19_assertions_suite",
)

covid19_assertions_validator.expect_column_values_to_not_be_null(column="geo_id")
covid19_assertions_validator.expect_column_values_to_be_between(
    column="confirmed_cases", min_value=0, max_value=1000
)
covid19_assertions_validator.expect_column_to_exist(column="confirmed_cases")
covid19_assertions_validator.expect_column_values_to_be_of_type(
    column="confirmed_cases", type_="INTEGER"
)
covid19_assertions_validator.expect_column_values_to_be_unique(
    column="country_territory_code"
)
covid19_assertions_validator.expect_column_values_to_be_in_set(
    column="country_territory_code", value_set=["US", "CA", "MX"]
)
covid19_assertions_validator.expect_column_values_to_match_strftime_format(
    column="date", strftime_format="%Y-%m-%d"
)

# Save the expectation suite

covid19_assertions_validator.save_expectation_suite(discard_failed_expectations=False)
