import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#print(client_id, client_secret)

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

def search_for_playlist(token, country):
    url = "https://api.spotify.com/v1/browse/categories/toplists/playlists"
    headers = get_auth_header(token)
    query = f"?country={country}&limit=1"
    url_query = url + query

    result = get(url_query, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    return json_result

token = get_token()
print("country_codes= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', ")
print("'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', ")
print("'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']")
print('')
country = input('Choose a country: ')
top_playlist = search_for_playlist(token, country)

tracks = top_playlist[0]["tracks"]["href"]

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
for artist in artists:
    print(artist["name"])
track = number_one["track"]["name"]
print(track)
