from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
web_page = r.text

soup = BeautifulSoup(web_page, "html.parser")
tags = soup.findAll(name="span")
scores = soup.find(name="span", class_="score").getText()
for tag in tags:
    text = tag.getText()
    link = tag.get("href")
    print(f"{text}\n{link}\n{scores}")


# ----------------------------------------------
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.prettify())
# print(soup.h1.name)  # h1
# print(soup.h1.string)  # Hitesh
# -------------------------------------------------
all_anchor = soup.findAll(name="a")
# print(all_anchor)

# for tag in all_anchor:
#     print(tag.getText())
#     print(tag.get('href'))
# ------------------------------------------------
heading = soup.find(name='h1', id="name")
print(heading)
# -------------------------------------------------
heading_3 = soup.findAll(name='h3', class_='heading')
for tag in heading_3:
    print(tag.getText())
# --------------------------------------------------

name = soup.select_one("#name")
print(name)

heading1 = soup.select(".heading")
print(heading1)
