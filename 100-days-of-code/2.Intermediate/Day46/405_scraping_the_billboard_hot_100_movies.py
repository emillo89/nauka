from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os

CLIENT_ID = os.environ["SPOTIFY_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope = "playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://example.com",
    # show_dialog=True,
    # cache_path="token.txt"
))

user_id = sp.current_user()["id"]

print(user_id)


URL = "https://web.archive.org/web/20210404021759/https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")

hot_100 = soup.find_all(name='span',class_="chart-element__information__song text--truncate color--primary")

hot_100_title = [songs.getText() for songs in hot_100]
print(hot_100_title)
song_uris = []


for song in hot_100_title[:10]:
    result = sp.search(q=f"track: {song}", type="track")
    # print(result)
    try:
        uri = result["tracks"]['items'][0]['uri']
        # print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped")
    else:
        song_uris.append(uri)

pprint.pprint(song_uris)

playlist = sp.user_playlist_create(user=user_id, name="Billboard hot 100 songs", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist)