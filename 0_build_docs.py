import great_expectations as gx

# Create the context including the context folder locally
context = gx.get_context()

# Build data docs and open data docs
context.build_data_docs()
context.open_data_docs()
