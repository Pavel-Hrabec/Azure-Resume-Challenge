import os
import json
import azure.functions as func
from azure.cosmos import CosmosClient


def main(req: func.HttpRequest) -> func.HttpResponse:

    ### Gets variables specified from local.setting.json file 
    endpoint = os.environ["Endpoint"] 
    key = os.environ["CosmosDBConnectionString"]
    database_name = os.environ['DatabaseName']
    container_name = os.environ['CollectionName']

    try:
        client = CosmosClient(endpoint, key) # Connection to Azure CosmosDB API
        database = client.get_database_client(database_name) # Gets database we want to query from
        container = database.get_container_client(container_name) # Gets container inside the database we want to work with

        item = container.read_item("2", partition_key="2") # Finds item ID 2 in container 
        GetCountValue = item["count"] # Gets the value for count
        IncrementValue = int(GetCountValue) + 1 # Increments count value by 1
        item["count"] = str(IncrementValue) # Passes incremented count value back to dictionary
        updated_item = container.upsert_item(item) # Uploads dictionary back to the Cosmos DB with updated count value

        return func.HttpResponse(json.dumps(item), status_code=200)

    except Exception as error:
        print(error)
        return func.HttpResponse(json.dumps(item), status_code=200)


