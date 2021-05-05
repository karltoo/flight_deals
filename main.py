#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime
from data_manager import DataManager
from flight_search import FlightSearch
import time

dm = DataManager()
city_names_list = dm.get_city_names()

time.sleep(60)

fs = FlightSearch()
city_IATA_dict = fs.get_city_IATA(city_names_list)

time.sleep(60)

cities_IATA_price_dict = dm.put_IATA_codes(city_IATA_dict)

#cities_IATA_price_dict = {'Paris': ['PAR', 54], 'Berlin': ['BER', 42], 'Tokyo': ['TYO', 485], 'Sydney': ['SYD', 551], 'Istanbul': ['IST', 95], 'Kuala Lumpur': ['KUL', 414], 'New York': ['NYC', 240], 'San Francisco': ['SFO', 260], 'Cape Town': ['CPT', 378]}

fs.search_flight(cities_IATA_price_dict)




