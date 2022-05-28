from logging import exception
from bs4 import BeautifulSoup
import requests
import creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("What date do you want to travel to?  (format: YYYY-MM-DD): ")
# date = '2003-08-30'

url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")
song_data = soup.select('li ul li h3')
song_list = [(song.text).strip() for song in song_data]

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, show_dialog=True, cache_path="46/token.txt"))

user_id = sp.current_user()["id"]

playlist_id = sp.user_playlist_create(user_id, f"Playlist for week of {date}", public=False, collaborative=False, description='POC auto created playlist for date.')
print(playlist_id)
song_uris = []
for song in song_list:
    id = sp.search(f"track:{song} year:{date[0:3]}", limit=1, type='track',market='US')
    try:
        print(song)
        song_uris.append(id["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

sp.playlist_add_items(playlist_id["id"], song_uris)