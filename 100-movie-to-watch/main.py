import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
emp_web_page = response.text
# print(emp_web_page)

result = []
soup = BeautifulSoup(emp_web_page, "html.parser")
find_all_title = soup.find_all(name="h3", class_="title")

# title_pop = find_all_title.pop(0)
#
# print(title_pop)
# print(pop)
for title in find_all_title:
    text = title.getText().replace(")", "").replace(":", "")
    int_text = num(text.split()[0])
    title_text = ' '.join(text.split()[1:])
    result.append((int_text, title_text))

# print(result)
sorted_result = sorted(result, key=lambda x: x[0])

# for i in sorted_result:
    # print(i[0], i[1])
    # open("movies.txt", "a").write(f"{i[0]} {i[1]}\n")
for num, text in sorted_result:
    try:
        open("movies.txt", "a").write(f"{num} {text}\n")
    except FileNotFoundError:
        open("movies.txt", "w").write(f"{num} {text}\n")
