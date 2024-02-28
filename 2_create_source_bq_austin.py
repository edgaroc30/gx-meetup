import great_expectations as gx

# Create the context including the context folder locally
context = gx.get_context()

# Create a datasource to our context
bq_datasource = context.sources.add_or_update_sql(
    name="bq_austin",
    connection_string="bigquery://sbx-edgar-gx/austin_bikeshare",
)
