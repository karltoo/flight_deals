#sheety_response = {
#  "prices": [
#    {
#      "city": "Paris",
#      "iataCode": "PAR",
#      "lowestPrice": 54,
#      "id": 2
#    },
#    {
#      "city": "Berlin",
#      "iataCode": "",
#      "lowestPrice": 42,
#      "id": 3
#    },
#    {
#      "city": "Tokyo",
#      "iataCode": "",
#      "lowestPrice": 485,
#      "id": 4
#    },
#    {
#      "city": "Sydney",
#      "iataCode": "",
#      "lowestPrice": 551,
#      "id": 5
#    },
#    {
#      "city": "Istanbul",
#      "iataCode": "",
#      "lowestPrice": 95,
#      "id": 6
#    },
#    {
#      "city": "Kuala Lumpur",
#      "iataCode": "",
#      "lowestPrice": 414,
#      "id": 7
#    },
#    {
#      "city": "New York",
#      "iataCode": "",
#      "lowestPrice": 240,
#      "id": 8
#    },
#    {
#      "city": "San Francisco",
#      "iataCode": "",
#      "lowestPrice": 260,
#      "id": 9
#    },
#    {
#      "city": "Cape Town",
#      "iataCode": "",
#      "lowestPrice": 378,
#      "id": 10
#    }
#  ]
#}
#list_lenght = len(sheety_response["prices"])
##print(list_lenght)
##city_name_list = []
##for item in range(0, list_lenght):
##    city_name = sheety_response["prices"][item]["city"]
##    print(city_name)
##    city_name_list.append(city_name)
#
#city_name_list = [sheety_response["prices"][item]["city"] for item in range(0, len(sheety_response["prices"]))]
#print(city_name_list)

# --------------------------------------- GETTING CITIES IATA CODES FROM TEQUILA ------------------------------------- #
#import requests
#
#city_IATA_dictionary = {
#
#}
#
#city_names_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York',
#                   'San Francisco', 'Cape Town']
#
#for city in city_names_list:
#  headers = {
#      "apikey": "YQOtHkfklr36Cbbm36Nuxb6C75PdDhM2"
#  }
#
#  tequila_response = requests.get(url=f"https://tequila-api.kiwi.com/locations/query?term={city}&locale=en-US&location_"
#                  "types=airport&limit=3&active_only=true", headers=headers)
#  data = tequila_response.json()
#  print(data["locations"][0]["city"]["code"])
#
#  city_IATA = {city : data["locations"][0]["city"]["code"]}
#  print(city_IATA)
#  city_IATA_dictionary.update(city_IATA)
#
#print(city_IATA_dictionary)

# --------------------------------------------- Adding city IATA codes to Google Sheets ------------------------------ #
#import requests
#
#city_IATA_dict = {'Paris': 'PAR', 'Berlin': 'BER', 'Tokyo': 'TYO', 'Sydney': 'SYD', 'Istanbul': 'IST', 'Kuala Lumpur': 'KUL',
# 'New York': 'NYC', 'San Francisco': 'SFO', 'Cape Town': 'CPT'}
#
#sheety_headers = {
#    "Authorization": "Basic a2FybHRvbzo4eEMxOVJlbEkjekJKMCYhdw=="
#}
#
#object_id = 1
#
#city_IATA_dict = {'Paris': 'PAR', 'Berlin': 'BER', 'Tokyo': 'TYO', 'Sydney': 'SYD', 'Istanbul': 'IST', 'Kuala Lumpur': 'KUL',
# 'New York': 'NYC', 'San Francisco': 'SFO', 'Cape Town': 'CPT'}
#
#for item in city_IATA_dict:
#
#    object_id += 1
#
#    spreadsheet_input = {
#        "price": {
#            "city": item,
#            "code": city_IATA_dict.get(f"{item}")
#        }
#    }
#
#    sheety_endpoint = f"https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices/{object_id}"
#    #sheety_endpoint = "https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices"
#
#    response1 = requests.put(url=sheety_endpoint, json=spreadsheet_input, headers=sheety_headers)
#    print(response1.text)
#
#    #USE THE PUT METHOD!!!
#
# --------------------------- Getting dictionary with both city code and price ------------------------------------ #

import requests

city_IATA_dictionary = {}

city_names_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']

sheety_headers = {
    "Authorization": "Basic a2FybHRvbzo4eEMxOVJlbEkjekJKMCYhdw=="
}

object_id = 1

for city in city_names_list:

    object_id += 1

    headers = {
        "apikey": "YQOtHkfklr36Cbbm36Nuxb6C75PdDhM2"
    }

    tequila_response = requests.get(
        url=f"https://tequila-api.kiwi.com/locations/query?term={city}&locale=en-US&location_"
            "types=airport&limit=3&active_only=true", headers=headers)
    data = tequila_response.json()
    #print(data["locations"][0]["city"]["code"])

    sheety_endpoint = f"https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices/{object_id}"

    response1 = requests.get(url=sheety_endpoint, headers=sheety_headers)
    price_data = response1.json()
    print(price_data)
    price = price_data["price"]["lowestPrice"]
    print(price)

    city_IATA = {city: [data["locations"][0]["city"]["code"], price]}
    # print(city_IATA)
    city_IATA_dictionary.update(city_IATA)

print(city_IATA_dictionary)

# ----------------------------------------------- SEARCHING FOR FLIGHT ----------------------------------------------- #
import requests
from datetime import datetime, timedelta

today = datetime.now().date().strftime("%d/%m/%Y")
#print(today)
date_6_months = (datetime.now().date() + timedelta(182)).strftime("%d/%m/%Y")
#print(date_6_months)

flight_search_data = {'Paris': ['PAR', 30], 'Berlin': ['BER', 30], 'Tokyo': ['TYO', 300], 'Sydney': ['SYD', 300],
                      'Istanbul': ['IST', 60], 'Kuala Lumpur': ['KUL', 300], 'New York': ['NYC', 180],
                      'San Francisco': ['SFO', 230], 'Cape Town': ['CPT', 250]}

search_endpoint = "https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021"

headers = {
                "apikey": "YQOtHkfklr36Cbbm36Nuxb6C75PdDhM2"
            }
for item in flight_search_data:
    params = {
        "fly_from": "TLL",
        "fly_to": f"{flight_search_data[f'{item}'][0]}",
        "date_from": today,
        "date_to": date_6_months,
        "price_to": f"{flight_search_data[f'{item}'][1]}"


    }

    tequila_response = requests.get(url=f"https://tequila-api.kiwi.com/v2/search", params=params, headers=headers)
    data = tequila_response.json()
    print(data)