import great_expectations as gx

# Get the context from local file
context = gx.get_context()

# Build data docs and open data docs
context.build_data_docs()
context.open_data_docs()
