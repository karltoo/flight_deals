import requests
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.city_IATA_dictionary = {}
        self.today = datetime.now().date().strftime("%d/%m/%Y")


    def get_city_IATA(self, city_names_list):

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
            # print(data["locations"][0]["city"]["code"])

            sheety_endpoint = f"https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices/{object_id}"

            response1 = requests.get(url=sheety_endpoint, headers=sheety_headers)
            price_data = response1.json()
            price = price_data["price"]["lowestPrice"]
            print(price)

            city_IATA = {city: [data["locations"][0]["city"]["code"], price]}
            # print(city_IATA)
            self.city_IATA_dictionary.update(city_IATA)

        print(self.city_IATA_dictionary)
        return self.city_IATA_dictionary

        #for city in city_names_list:
        #    headers = {
        #        "apikey": "YQOtHkfklr36Cbbm36Nuxb6C75PdDhM2"
        #    }
#
        #    tequila_response = requests.get(
        #        url=f"https://tequila-api.kiwi.com/locations/query?term={city}&locale=en-US&location_"
        #            "types=airport&limit=3&active_only=true", headers=headers)
        #    data = tequila_response.json()
        #    #print(data["locations"][0]["city"]["code"])
#
        #    city_IATA = {city: data["locations"][0]["city"]["code"]}
        #    #print(city_IATA)
        #    self.city_IATA_dictionary.update(city_IATA)
#
        #print(self.city_IATA_dictionary)
        #return self.city_IATA_dictionary


    def search_flight(self, dictionary):

        self.date_6_months = (datetime.now().date() + timedelta(182)).strftime("%d/%m/%Y")
        # print(date_6_months)

        flight_search_data = dictionary

        headers = {
            "apikey": "YQOtHkfklr36Cbbm36Nuxb6C75PdDhM2"
        }
        for item in flight_search_data:
            params = {
                "fly_from": "TLL",
                "fly_to": f"{flight_search_data[f'{item}'][0]}",
                "date_from": self.today,
                "date_to": self.date_6_months,
                "price_to": f"{flight_search_data[f'{item}'][1]}"

            }

            tequila_response = requests.get(url=f"https://tequila-api.kiwi.com/v2/search", params=params,
                                            headers=headers)
            data = tequila_response.json()
            print(data)