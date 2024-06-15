from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
soup.title.string = "Title changed using BeautifulSoup"
# soup.findAll(name="a")[0].string = "Google"
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.get("href"))

company_url = soup.select_one(selector="#name")
print(company_url)