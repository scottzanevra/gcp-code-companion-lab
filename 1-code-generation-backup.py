# function that generates a random uuid

def generate_uuid():
    return str(uuid.uuid4())


# function that extracts and email address using regex from a string

def extract_email(string):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    return  pattern



# function that does a inner join between two lists

def inner_join(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result.append(item1)
    return result


# write a function that runs a query on google big query given a dataset, table, and query as an input

def run_query(dataset, table, query):
    """Runs a query on Google BigQuery.

    Args:
        dataset: The name of the dataset to query.
        table: The name of the table to query.
        query: The query to run.

    Returns:
        A list of dictionaries representing the results of the query.
    """

    # Import the BigQuery client library.
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Set the default project for the client.
    client.project = "bigquery-public-data"

    # Set the dataset and table for the query.
    dataset_ref = bigquery.DatasetReference(client.project, dataset)
    table_ref = dataset_ref.table(table)

    # Set the query to run.
    query_job = client.query(query)

    # Wait for the query to complete.
    query_job.result()  # Waits for the query to complete.

    # Get the results of the query.
    results = query_job.result().to_dataframe()

    # Return the results.
    return results
