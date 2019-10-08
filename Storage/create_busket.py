def create_bucket():
    # [START storage_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import storage

    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = 'emata_test_bucket2'

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print('Bucket {} created.'.format(bucket.name))
    # [END storage_quickstart]


if __name__ == '__main__':
    run_quickstart()
