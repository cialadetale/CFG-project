import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

'''
How to connect Spotify API Client ID and Client Secret with spotipy:
1. When the code is in "run" mode, in the terminal nothing will happen - spotipy module is waiting 
for SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET. These two you can get in Your Spotify Developer Account.
2. When you get your ID, then in terminal type:
$env:SPOTIPY_CLIENT_ID="your_id"
my: $env:SPOTIPY_CLIENT_ID="f32c482748114d6f8e7f86b3faf4164d"
3. Press enter.
4. Type:
$env:SPOTIPY_CLIENT_SECRET="your_secret"
my: $env:SPOTIPY_CLIENT_SECRET="bffdec09d4814a42a7602384518e9192"
5. Press enter.
6. Run the code again - voila :)
'''

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
