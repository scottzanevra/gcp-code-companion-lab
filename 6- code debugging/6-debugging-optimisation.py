
# ************************** Code Companion Prompt ***********************************
# what is wrong with this code
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
for item in items.keys():
    income = 0
    qty = input(f"How many {item}s have you sold? ")
    income = income + qty * items[item]
print(f"\nThe income today was £{income:0.2f}")

#     income = income + qty * items[item]
#                       ~~~~^~~~~~~~~~~~~
# TypeError: can't multiply sequence by non-int of type 'float'





# ************************** Code Companion Prompt ***********************************
# which is this fuction returning the wrong answer
def multiply(a, b):
    z = int(a)*b
    return z


# ************************** Code Companion Prompt ***********************************
# write a function that will upload an file to google cloud storage
# hightlight the code and ask

# ************************** Code Companion Prompt ***********************************
# optimise for large files



# how could this Bigquery query be optimised
'''
WITH daily_sum AS ( -- Group on the date, then sum to get total passengers per day
 SELECT
   vendor_id,
   DATE_TRUNC(pickup_datetime, DAY) AS the_date,
   SUM(passenger_count) AS passengers_ferried
 FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
 GROUP BY 1, 2
)
SELECT
 ds.*,
 dss.passengers_ferried AS passengers_ferried_prev_day,
 ds.passengers_ferried - dss.passengers_ferried AS increase_in_passengers
FROM daily_sum ds
LEFT JOIN daily_sum dss ON ds.the_date = DATE_ADD(dss.the_date, INTERVAL 1 DAY) -- Self-join the CTE on vendor ID and date
 AND ds.vendor_id = dss.vendor_id
ORDER BY the_date ASC
'''


# ************************** Code Companion Prompt ***********************************
# what IAM permission are required to perform this action
def download_json_from_gcs(bucket_name, file_name):
    """Downloads a JSON file from a GCS bucket."""

    from google.cloud import storage

    # Creates a client
    storage_client = storage.Client()

    # The path to which the file should be downloaded
    local_file_name = "downloaded.json"

    # Downloads the file
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.download_to_filename(local_file_name)

    # Prints a success message
    print(
        "Downloaded {} from {} to {}.".format(
            file_name, bucket_name, local_file_name
        )
    )


# ************************** Code Companion Prompt ***********************************
# what IAM permission are required to perform this action
def provision_dataflow_cluster(project_id, region, cluster_name, num_workers):
    """Provisions a Cloud Dataflow cluster."""

    from google.cloud import dataflow_v1beta3 as dataflow

    # Creates a client
    dataflow_client = dataflow.JobsV1Beta3Client()

    # The Cloud Dataflow cluster to create
    cluster = dataflow.Cluster(
        project_id=project_id,
        cluster_name=cluster_name,
        region=region,
        num_workers=num_workers,
    )

    # Creates the cluster
    operation = dataflow_client.create_cluster(project_id, region, cluster)

    # Waits for the operation to complete
    operation.result()

    # Prints a success message
    print("Created Cloud Dataflow cluster {} in region {}.".format(cluster_name, region))