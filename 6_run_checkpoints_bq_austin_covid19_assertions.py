import great_expectations as gx

# Create the context including the context folder locally
context = gx.get_context()


covid10_assertions_asset = context.get_datasource("bq_austin").get_asset(
    "covid19_assertions"
)
covid19_assertions_request = covid10_assertions_asset.build_batch_request()

# Add the checkpoint to the context
checkpoint = context.add_or_update_checkpoint(
    name="bq_austin_covid19_assertions_checkpoint",
    validations=[
        {
            "batch_request": covid19_assertions_request,
            "expectation_suite_name": "covid19_assertions_suite",
        }
    ],
)

checkpoint_result = checkpoint.run()
