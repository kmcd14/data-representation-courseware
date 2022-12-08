# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json"

#https://data.gov.ie/dataset?q=exchequer+account+%28historical+series%29&sort=score+desc%2C+metadata_created+desc

# Import libaries
import requests
import json


# Api link
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"


# Function to get the data
def getData():
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":

    # Writing and storing data in a json file.
    with open("cso.json","wt") as fp:
        print(json.dumps(getData()), file=fp)