import great_expectations as gx

# Get the context from local file
context = gx.get_context()

bq_datasource = context.datasources["bq_austin"]

# Create assets for our datasource - add existing tables
covid19_assertions_asset = bq_datasource.add_table_asset(
    name="covid19_assertions",
    table_name="covid19_assertions",
    schema_name="austin_bikeshare",
)
