

# The code is trying to multiply the qty by the price of the item, but qty is a string and items[item] is a float. 
# To fix this, we need to convert qty to a float before multiplying it.

# Here is the fixed code:

items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
for item in items.keys():
    income = 0
    qty = input(f"How many {item}s have you sold? ")
    income = income + float(qty) * items[item]
print(f"\nThe income today was £{income:0.2f}")




# multiply(3.14, 2)
# We would expect the function to return 6.28, but it actually returns 6. This is because int(3.14) is 3, so the function is actually multiplying 3 by 2.
# To fix the function, we can change the line z = int(a)*b to z = float(a)*b. This will ensure that the decimal places in a are preserved.

# Here is the fixed function:
def multiply(a, b):
    z = float(a)*b
    return z


# ************************** Code Companion Prompt ***********************************
# write a function that will upload an file to google cloud storage
# hightlight the code and ask

# ************************** Code Companion Prompt ***********************************
# optimise for large files

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race
    # conditions and data corruptions. The request to upload is aborted if the
    # object's generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    # generation_match_precondition = 1488435555500303

    blob.upload_from_filename(source_file_name, chunk_size=1024 * 1024 * 5, num_retries=5)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

    return blob




# how could this Bigquery query be optimised
'''
1) Use a window function to calculate the previous day's passengers ferried. This can be done using the LAG() function, as shown below:
SELECT
  ds.*,
  LAG(ds.passengers_ferried, 1, 0) OVER (PARTITION BY ds.vendor_id ORDER BY ds.the_date) AS passengers_ferried_prev_day,
  ds.passengers_ferried - LAG(ds.passengers_ferried, 1, 0) OVER (PARTITION BY ds.vendor_id ORDER BY ds.the_date) AS increase_in_passengers
FROM daily_sum ds
ORDER BY the_date ASC


2) Use a subquery to calculate the previous day's passengers ferried. This can be done using a subquery, as shown below:
SELECT
  ds.*,
  (SELECT passengers_ferried
   FROM daily_sum
   WHERE vendor_id = ds.vendor_id
   AND the_date = DATE_ADD(ds.the_date, INTERVAL -1 DAY)) AS passengers_ferried_prev_day,
  ds.passengers_ferried - (SELECT passengers_ferried
                           FROM daily_sum
                           WHERE vendor_id = ds.vendor_id
                           AND the_date = DATE_ADD(ds.the_date, INTERVAL -1 DAY)) AS increase_in_passengers
FROM daily_sum ds
ORDER BY the_date ASC


3) Use a materialized view to store the daily sum of passengers ferried. This can be done using a materialized view, as shown below:
CREATE MATERIALIZED VIEW daily_sum AS
SELECT
  vendor_id,
  DATE_TRUNC(pickup_datetime, DAY) AS the_date,
  SUM(passenger_count) AS passengers_ferried
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
GROUP BY 1, 2;


4) Once the materialized view is created, the query can be rewritten as follows:
SELECT
  ds.*,
  dss.passengers_ferried AS passengers_ferried_prev_day,
  ds.passengers_ferried - dss.passengers_ferried AS increase_in_passengers
FROM daily_sum ds
LEFT JOIN daily_sum dss ON ds.the_date = DATE_ADD(dss.the_date, INTERVAL 1 DAY)
 AND ds.vendor_id = dss.vendor_id
ORDER BY the_date ASC







'''