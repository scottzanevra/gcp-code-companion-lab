# ************************** Code Companion Prompt ***********************************
# Implement a Python decorator to measure the execution time of functions and log the results.
import time
import logging

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"Function {func.__name__} took {end - start} seconds to execute.")
        return result
    return wrapper


# ************************** Code Companion Prompt ***********************************
# Create a Python class for a REST API client, handling authentication, GET/POST requests, and JSON parsing.
import requests
import json

class RestApiClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, auth=(self.username, self.password), params=params)
        return response.json()

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.post(url, auth=(self.username, self.password), json=data)
        return response.json()


# ************************** Code Companion Prompt ***********************************
# Build a Python script to scrape data from a website using Beautiful Soup, extract specific elements, and store the results in a CSV file.
import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, elements):
    """Scrapes data from a website using Beautiful Soup and extracts specific elements.

    Args:
        url (str): The URL of the website to scrape.
        elements (list): A list of CSS selectors for the elements to extract.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row of data.
    """

    # Get the HTML content of the website.
    response = requests.get(url)
    html = response.content

    # Parse the HTML content using Beautiful Soup.
    soup = BeautifulSoup(html, "html.parser")

    # Extract the data from the specified elements.
    data = []
    for element in elements:
        for item in soup.select(element):
            data.append({
                "element": element,
                "text": item.text,
                "href": item.get("href")
            })

    # Return the data as a list of dictionaries.
    return data


def save_to_csv(data, filename):
    """Saves the data to a CSV file.

    Args:
        data (list): A list of dictionaries, where each dictionary represents a row of data.
        filename (str): The name of the CSV file to save the data to.
    """

    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["element", "text", "href"])
        writer.writeheader()
        writer.writerows(data)


# Example usage.
url = "https://www.example.com"
elements = ["h1", "h2", "h3", "a"]
data = scrape_website(url, elements)
save_to_csv(data, "data.csv")




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
