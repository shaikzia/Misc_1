# Program to download all the images from a Website
# Youtube - SAF Business Analytics
import urllib.request
from bs4 import BeautifulSoup

def get_all(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = get_all("https://uwaterloo.ca")

i = 1
for img in soup.findAll('img'):
    temp = img.get('src')
    if temp[:1] == "/":
        image = "https://uwaterloo.ca" + temp
    else:
        image = temp

    nametemp = img.get('alt')
    if len(nametemp) == 0:
        filename = str(i)
        i = i + 1
    else:
        filename = nametemp

    imagefile = open(filename + ".jpeg", "wb")
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()