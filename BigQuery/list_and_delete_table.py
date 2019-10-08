from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'emata'
tables = client.list_tables(dataset_id)
print("Tables contained in '{}':".format(dataset_id))
for table in tables:
    client.delete_table(table, not_found_ok=True)
    print("Deleted table '{}'.".format(table))
#    print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))
