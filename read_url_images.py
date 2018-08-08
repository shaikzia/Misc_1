import requests
from bs4 import BeautifulSoup
r = requests.get("https://uwaterloo.ca")

soup = BeautifulSoup(r.content)
# print(soup.prettify())

all_a = soup.find_all("a")
print(all_a)

for link in soup.find_all("a"):
    print(link.get("href"))
    print(link.text)