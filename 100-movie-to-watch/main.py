import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
emp_web_page = response.text
# print(emp_web_page)

soup = BeautifulSoup(emp_web_page, "html.parser")
find_all_title = [soup.find_all(name="h3", class_="title")]
findall_title = soup.findAll(name="h3", class_="title")
pop = findall_title.pop(0).getText()
print(find_all_title)
print(findall_title)
print(pop)
