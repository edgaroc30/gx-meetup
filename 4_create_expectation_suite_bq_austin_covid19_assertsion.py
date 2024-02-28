import great_expectations as gx

# Create the context including the context folder locally
context = gx.get_context()
context.add_or_update_expectation_suite(
    expectation_suite_name="covid19_assertions_suite"
)
