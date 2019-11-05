from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'emata'

job_config = bigquery.QueryJobConfig()
# Set the destination table
table_ref = client.dataset(dataset_id).table("test_api_post")
job_config.destination = table_ref
sql = """
    SELECT corpus
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY corpus;
"""

# Start the query, passing in the extra configuration.
query_job = client.query(
    sql,
    # Location must match that of the dataset(s) referenced in the query
    # and of the destination table.
    location="US",
    job_config=job_config,
)  # API request - starts the query

query_job.result()  # Waits for the query to finish
print("Query results loaded to table {}".format(table_ref.path))