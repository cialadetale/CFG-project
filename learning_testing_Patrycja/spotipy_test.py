import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

print("country_codes= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', ")
print("'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', ")
print("'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']")
print('')
country = input('Choose a country: ')

url = "https://api.spotify.com/v1/browse/categories/toplists/playlists"
query = f"?country={country}&limit=1"

results = url+query
print(results)

json_result = json.loads(results.content)["playlists"]["items"]

print(json_result)
