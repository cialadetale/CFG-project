"""
Spotify API - the best song in specified country
Project made by:
Patrycja Jankowska
Magdalena Mendrala
Diana Kasoro
"""

# importing necessary libraries
import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import country_converter as coco
#from googleapiclient.discovery import build


# start of authorization
load_dotenv()

# here create .env file
# your CLIENT_ID and CLIENT_SECRET have to be put into .env file (use yours id and secret)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
#youtube_key = os.getenv("api_key")


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


# getting an authorization
token = get_token()


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# function to get one, searched playlist - later from this playlist we take tracks url to get the first song in the country
def search_for_playlist(token, country_iso2):
    url = "https://api.spotify.com/v1/browse/categories/toplists/playlists"
    headers = get_auth_header(token)
    query = f"?country={country_iso2}&limit=1"
    url_query = url + query

    result = get(url_query, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    return json_result


# converting country name given by the user to iso2 standard (required by SpotifyAPI)
country = input('Please select a country: ')
country_iso2 = coco.convert(names=country, to='ISO2')

# getting a playlist
top_playlist = search_for_playlist(token, country_iso2)
# getting a href (link)
tracks = top_playlist[0]["tracks"]["href"]


# function to get the top song in a specified country
def search_for_track(token, country_iso2):
    url = tracks
    headers = get_auth_header(token)
    query = f"?country={country_iso2}&limit=1"
    url_query = url + query

    result = get(url_query, headers=headers)
    json_result = json.loads(result.content)["items"][0]
    return json_result


number_one = search_for_track(token, country_iso2)
artists = number_one["track"]["artists"]
# getting all artists who made a song (there will be more than one) and printing them
authors = []
for artist in artists:
    authors.append(artist["name"])
# getting track title and printing it
track = number_one["track"]["name"]

print(f'The most popular track in {country} is {track} by {(", ".join(authors))}')

'''
# using build module to get authorization from YouTube vol.3 API
youtube = build("youtube", "v3", developerKey=youtube_key)

# searching for the track's title and author in YouTube videos
query = youtube.search().list(
    part="snippet",
    maxResults=1,
    type="video",
    q=f"{track} + {authors}"
)
result = query.execute()
# pprint(result)
# getting
video_id = result["items"][0]["id"]["videoId"]

# getting a link to searched video
video_link = f"https://www.youtube.com/watch?v={video_id}"
'''