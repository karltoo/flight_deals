import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_headers = {
    "Authorization": "Basic a2FybHRvbzo4eEMxOVJlbEkjekJKMCYhdw=="
}
        self.sheety_endpoint = "https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices"
        self.sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        self.sheety_response = self.sheety_response.json()

    def get_city_names(self):
        self.city_name_list = [self.sheety_response["prices"][item]["city"] for item in
                               range(0, len(self.sheety_response["prices"]))]
        return self.city_name_list

    def put_IATA_codes(self, city_IATA_dict):

        sheety_headers = {
            "Authorization": "Basic a2FybHRvbzo4eEMxOVJlbEkjekJKMCYhdw=="
        }

        self.object_id = 1

        self.city_IATA_dict = city_IATA_dict

        for item in self.city_IATA_dict:
            self.object_id += 1

            spreadsheet_input = {
                "price": {
                    "city": item,
                    "code": self.city_IATA_dict.get(f"{item}")
                }
            }

            sheety_endpoint = \
                f"https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices/{self.object_id}"

            response1 = requests.put(url=sheety_endpoint, json=spreadsheet_input, headers=sheety_headers)
            #pprint(response1.text)
            return response1.json()









































#sheety_headers = {
#    "Authorization": "Basic a2FybHRvbzo4eEMxOVJlbEkjekJKMCYhdw=="
#
#sheety_endpoint = "https://api.sheety.co/73ac2a4f5aaba6549a1f2635672c29d3/myFlightDeals/prices#
#sheety_response = requests.get(url=sheety_endpoint, headers=sheety_headers)
#print(sheety_response.text)