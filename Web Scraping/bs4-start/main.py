from bs4 import BeautifulSoup

# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())
print(soup.h1.name)  # h1
print(soup.h1.string)  # Hitesh
