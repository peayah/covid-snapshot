import requests




url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f1810c00c8msh4de5774e31df7eap1ac26fjsn82c708fe9563",
}

# import for the world
world_response = requests.request("GET", url, headers=headers)



