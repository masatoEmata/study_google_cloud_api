from google.cloud import bigquery
# [END bigquery_simple_app_deps]


def query_stackoverflow():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    query_job = client.query("""
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10""")

    results = query_job.result()  # Waits for job to complete.
    # [END bigquery_simple_app_query]

    # [START bigquery_simple_app_print]
    for row in results:
        print("{} : {} views".format(row.url, row.view_count))
    # [END bigquery_simple_app_print]


if __name__ == '__main__':
    query_stackoverflow()
# [END bigquery_simple_app_all]