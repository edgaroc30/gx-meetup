import great_expectations as gx

# Get the context from local file
context = gx.get_context()

# Create a datasource to our context
bq_datasource = context.sources.add_or_update_sql(
    name="bq_austin",
    connection_string="bigquery://sbx-edgar-gx/austin_bikeshare",
)

# Or run great_expectations datasource new
