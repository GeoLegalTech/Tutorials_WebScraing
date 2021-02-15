import requests
from bs4 import BeautifulSoup

# URL
url = "https://www.holzwickede.de/amtsblatt/index.php"

# Getting content
download_url =  requests.get(url)


# Parse the html with beautifulsoup and creat the object
soup = BeautifulSoup(download_url.text, features="html.parser")

# Create a local copy (Best practice to download a non static webpage)
with open("download-form.html", "w") as file:
    file.write(soup.prettify())

# Grab all the titles for the scrap
name_tags = soup.find_all(class_="trigger trigger_active announcement-anchor")

# Lets print what we get from them
for name in name_tags:
    print (name)
