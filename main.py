#Weather Forecasting Website (backend)

print("Weather Forecasting Website Application")

import config

import requests
import json
import ipinfo
from geopy.geocoders import Nominatim

APIKey = config.api_key
API_HOST = config.api_host
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode(input("\nWhat City Do You Live In? "))
 
# printing address
print(getLoc.address)

# Weather Options
def weatherGet1(lat,lon):
    """3 hour interval - 5 day forecast for a given lat/lon"""
    """remember to use enviroment variables to hide api keys 341f6c3c6fmsh324475775f8beabp1ada0fjsn7d3aee0230ad"""
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
    querystring = {"lat":lat,"lon":lon,"units":"imperial"}
    headers = {
		"X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
	}
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)

def weatherGet2(lat,lon):
    '''Returns the current (most recent) weather observation of a given location'''
    """remember to use enviroment variables to hide api keys 341f6c3c6fmsh324475775f8beabp1ada0fjsn7d3aee0230ad"""
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lon":lon,"lat":lat,"units":"imperial"}
    headers = {
        "X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)

def weatherGet3 (lat,lon):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely"
    querystring = {"lat":lat,"lon":lon,"units":"imperial"}
    headers = {
        "X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)

def weatherGet4(lat,lon):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
    querystring = {"lat":lat,"lon":lon,"units":"imperial"}
    headers = {
        "X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)
    
def weatherGet5(lat,lon,hours):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"
    querystring = {"lat":lat,"lon":lon,"hours":hours,"units":"imperial"}
    headers = {
        "X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)

def weatherGet6(lat,lon):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/alerts"
    querystring = {"lat":lat,"lon":lon,"units":"imperial"}
    headers = {
        "X-RapidAPI-Key": APIKey,
		"X-RapidAPI-Host": API_HOST
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)
    print(parsed)
    
    
print("\n1. 5 day forecast")
print("\n2. Current Weather Data of a location")
print("\n3. 1 Hour / Minutely Forecast")
print("\n4. 16 Day Forecast")
print("\n5. 120 Hour Forecast")
print("\n6. Severe Weather Alerts")


choice = int(input("\nEnter your choice: "))
while choice <1 or choice >6:
    choice = int(input("\nEnter a valid choice: "))


if choice == 1:
    weatherGet1(getLoc.latitude,getLoc.longitude)
elif choice == 2:
    weatherGet2(getLoc.latitude,getLoc.longitude)
elif choice == 3:
    weatherGet2(getLoc.latitude,getLoc.longitude)
elif choice == 4:
    weatherGet2(getLoc.latitude,getLoc.longitude)
elif choice == 5:
    hours = int(input("\nHow many hours do you want to see into the future? "))
    while hours < 0 or hours > 120:
        hours = int(input("\nEnter a valid number of hours: "))
    weatherGet2(getLoc.latitude,getLoc.longitude,hours)
else:
    weatherGet2(getLoc.latitude,getLoc.longitude)