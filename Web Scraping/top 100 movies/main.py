import requests
from bs4 import BeautifulSoup

ENDPOINT = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(ENDPOINT)
web_contents = r.text


soup = BeautifulSoup(web_contents, "html.parser")
name = soup.findAll(name="h3", class_="title")
# Fetching names of the movies
name_list = [name.getText().lstrip() for name in name]
# Find the position of the movies ordered
numbers = [name_list.split()[0] for name_list in name_list]
# List contain the numbers
list_number = [int(num.strip("):")) for num in numbers]
# Finding the max value from the list
while len(list_number) != 0:
    max_num = min(list_number)
    index = list_number.index(max_num)
    with open("TOP 100 MOVIES TO WATCH.txt", mode="a") as file:
        file.write(f"{name_list[index]}\n")
    list_number.remove(max_num)
    # print(list_number)
