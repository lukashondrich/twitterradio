

from google.cloud import bigquery
client = bigquery.Client()
#def query_tweet():
query = """
    SELECT *
    FROM `disco-sky-304721.twitterradio.test_data_6`
    WHERE ingestion_time = (SELECT MAX(ingestion_time) FROM `disco-sky-304721.twitterradio.test_data_6` WHERE done_reading=False )
"""
query_job = client.query(query)  # Make an API request.

for row in query_job:
    print(row[0])
    # Row values can be accessed by field name or index.
