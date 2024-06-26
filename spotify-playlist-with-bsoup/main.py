import os

import requests
import spotify
from bs4 import BeautifulSoup

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

sp = spotify.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="Mozo",
    )
)
user_id = sp.current_user()["id"]

URL = "https://www.billboard.com/charts/hot-100/"
time_travel = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_name_list = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = time_travel.split("-")[0]
for song in song_name_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

response = requests.get(URL + time_travel)
billboard_web_page = response.text
# print(response.text)

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_name_spans = soup.select("li ul li h3")

song_name_list = [song.getText().strip() for song in song_name_spans]

with open("songs.txt", "a", encoding="utf-8") as file:
    for song_list in song_name_list:
        file.write(f"{song_list}\n")
