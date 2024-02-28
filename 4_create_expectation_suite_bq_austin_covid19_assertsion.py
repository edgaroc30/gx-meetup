import great_expectations as gx

# Get the context from local file
context = gx.get_context()
context.add_or_update_expectation_suite(
    expectation_suite_name="covid19_assertions_suite"
)

# Or run great_expectations suite new
# great_expectations suite edit covid19_assertions_suite
