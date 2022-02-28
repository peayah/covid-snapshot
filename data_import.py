import requests
from requests import *
from flask import request
from datetime import date


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f1810c00c8msh4de5774e31df7eap1ac26fjsn82c708fe9563",
}

# import world data
world_response = requests.request("GET", url, headers=headers)
# print(world_response.text)


##############################################


today = date.today()
this_year = today.isoformat()
last_year_same_time = today.replace(year=today.year - 1)
# print(this_year)
# print(last_year_same_time)

country = "usa"

# request for one country's data
one_country_url = "https://covid-193.p.rapidapi.com/history"

one_country_querystring = {"country": country, "day": this_year}
last_year_one_country_querystring = {"country": country, "day": last_year_same_time}

one_country_headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f1810c00c8msh4de5774e31df7eap1ac26fjsn82c708fe9563"
    }

one_country_response = requests.request("GET", one_country_url,
                                        headers=one_country_headers,
                                        params=one_country_querystring)

last_year_one_country_response = requests.request("GET", one_country_url,
                                                  headers=one_country_headers,
                                                  params=last_year_one_country_querystring)

# print(one_country_response.text)


##############################################


def return_data_for_one_country(c):
    today = date.today()
    this_year = today.isoformat()

    last_year_same_time = today.replace(year=today.year - 1)

    if c == "":
        country = "USA"
    else:
        country = c


    # request for one country's data
    y_url = "https://covid-193.p.rapidapi.com/history"

    y_querystring = {"country": country, "day": this_year}
    ly_querystring = {"country": country, "day": last_year_same_time}

    y_headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "f1810c00c8msh4de5774e31df7eap1ac26fjsn82c708fe9563"
        }

    this_years_numbers = requests.request("GET", one_country_url,
                                            headers=y_headers,
                                            params=y_querystring)

    last_years_numbers = requests.request("GET", y_url,
                                          headers=y_headers,
                                          params=ly_querystring)

    return this_years_numbers, last_years_numbers
