from bs4 import BeautifulSoup
import requests

# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# soup.title.string = "Title changed using BeautifulSoup"
# # soup.findAll(name="a")[0].string = "Google"
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # print(tag.get("href"))
#
# company_url = soup.select_one(selector="#name")
# print(company_url)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("tr", class_="athing")
# print(articles)
article_data = []
for article in articles:
    title_line = article.find("span", class_="titleline")
    if title_line:
        article_tag = title_line.find("a")
        if article_tag:
            article_text = article_tag.getText()
            article_link = article_tag.get("href")
            # score = article_tag.get("score")
            # print(article_text)
            # print(article_link)
            # print(score)

            subtext = article.find_next_sibling("tr").find("td", class_="subtext")
            if subtext:
                score_tag = subtext.find("span", class_="score")
                if score_tag:
                    score = score_tag.getText()
                    score_value = int(score.split(" ")[0])
                    article_data.append((article_text, article_link, score_value))

if article_data:
    max_article = max(article_data, key=lambda x: x[2])
    print("Article text: ", max_article[0])
    print("Article link: ", max_article[1])
    print("Article score: ", max_article[2])
else:
    print("No articles found")