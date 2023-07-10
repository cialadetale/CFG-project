'''
Spotify API - the best song in specified country
Project made by: 
Patrycja Jankowska
Magdalena Mendrala
Diana Kasoro
'''

# importing necessary libraries
import json
from dotenv.main import load_dotenv
import os
import base64
from requests import post, get

# start of authorization
load_dotenv()

# here create .env file
# your CLIENT_ID and CLIENT_SECRET have to be put into .env file (use yours id and secret)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#print(client_id, client_secret)

# function to get token/authorization from Spotify API
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded" 
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

#token = get_token()
#print(token)

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# function to get one, seaarched playlist - later from this playlist we take tracks url to get the first song in the country
def search_for_playlist(token, country):
    url = "https://api.spotify.com/v1/browse/categories/toplists/playlists"
    headers = get_auth_header(token)
    query = f"?country={country}&limit=1"
    url_query = url + query

    result = get(url_query, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    return json_result

# getting an authorization
token = get_token()
print("country_codes= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', ")
print("'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', ")
print("'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']")
print('')
# getting a country from user - it is necessary to specify where is the user searching for the top song now
country = input('Choose a country: ')

# getting a playlist 
top_playlist = search_for_playlist(token, country)
#print(top_playlist)

# getting a href (link)
tracks = top_playlist[0]["tracks"]["href"]

# function to get the top song in a specified country
def search_for_track(token, country):
    url = tracks
    headers = get_auth_header(token)
    query = f"?country={country}&limit=1"
    url_query = url + query

    result = get(url_query, headers=headers)
    json_result = json.loads(result.content)["items"][0]
    return json_result

number_one = search_for_track(token, country)
artists = number_one["track"]["artists"]
# getting all artists who made a song (there will be more than one) and printing them
for artist in artists:
    print(artist["name"])
track = number_one["track"]["name"]
# printing title of a track
print(track)
