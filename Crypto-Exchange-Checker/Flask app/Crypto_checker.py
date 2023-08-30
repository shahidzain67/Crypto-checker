import requests
import os
from dotenv import load_dotenv
import json

# Get environmental variables
load_dotenv()
url = str(os.getenv('MAIN_URL'))
access_key = str(os.getenv('API_ACCESS_KEY'))

# All accessible endpoints
endpoints = {
    "list_endpoint" : "/list",
    "live_endpoint" : "/live",
    "historical_endpoint" : "/historical",
}

# Run loop until exited
while(True):

    print("\n-----------------------------------------------------------------------------")
    print("Select one of the options below:\n-----------------------------------------------------------------------------")
    print("list: request a JSON list containing all supported crypto and fiat currencies")#
    print("live: request the most recent cryptocurrency rates")
    print("historical: request historical rates for a specific day")

    selected = input("\n\nSelect an option or enter x to exit: ")

    if selected == "list":
        list = requests.get(url+endpoints["list_endpoint"]+"?access_key="+access_key)
        data = json.loads(list.content)
        formatted_data = json.dumps(data, indent=2)
        print(formatted_data)

    elif selected == "live":
        live = requests.get(url+endpoints["live_endpoint"]+"?access_key="+access_key)
        data = json.loads(live.content)
        formatted_data = json.dumps(data, indent=2)
        print(formatted_data)

    elif selected == "historical":
        day = input("Please enter a day in the format YYYY-MM-DD: ")
        historical = requests.get(url+endpoints["historical_endpoint"]+day+"?access_key="+access_key)
        data = json.loads(historical.content)
        formatted_data = json.dumps(data, indent=2)
        print(formatted_data)

    elif selected == "x":
        break

    else:
        print("Please select a valid option.\n\n") 

print("Goodbye!\n")