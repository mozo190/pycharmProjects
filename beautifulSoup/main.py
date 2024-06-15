from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
soup.title.string = "Title changed using BeautifulSoup"
