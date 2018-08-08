# Read all the images with a single click
# Youtube - Tutspy
import urllib
i = 30
print("Downloading Started")

while i > 0:
    u = "http://behindwoods.com/tamil-actor/vijay/vijay-stills-photos"\
        "-pictures-"
#    i = i - 1
    URL = u+str(i)+".jpg"
    IMAGE = URL.rsplit('/', 1)[1]
    try:
        urllib.urlretrieve(URL, IMAGE)
    except Exception as e:
        print("Downloading Image", i)

    i = i - 1
