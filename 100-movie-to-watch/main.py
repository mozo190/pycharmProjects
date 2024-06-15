import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
emp_web_page = response.text
# print(emp_web_page)

result = []
soup = BeautifulSoup(emp_web_page, "html.parser")
find_all_title = soup.find_all(name="h3", class_="title")

for title in find_all_title:
    text = title.getText().replace(")", "").replace(":", "").replace("â", "").replace("'\'", "").replace("x80",
                                                                                                         "").replace(
        "x93", "")
    int_text = int(text.split()[0])
    title_text = ' '.join(text.split()[1:])
    result.append((int_text, title_text))

# print(result)
sorted_result = sorted(result, key=lambda x: x[0])
print(sorted_result)

with open("movies.txt", "w", encoding="utf-8") as file:
    for num, text in sorted_result:
        file.write(f"{num} {text}\n")
