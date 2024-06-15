import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
time_travel = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(URL + time_travel)
billboard_web_page = response.text
# print(response.text)

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_name_spans = soup.select("li ul li h3")

song_name_list = [song.getText().strip() for song in song_name_spans]

with open("songs.txt", "a", encoding="utf-8") as file:
    for song_list in song_name_list:
        file.write(f"{song_list}\n")
