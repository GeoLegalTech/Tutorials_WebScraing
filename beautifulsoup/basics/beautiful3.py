import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the html
scifi_url = 'https://www.myeblaettle.de/frontend/getcatalog.do?catalogId=191056&catalogVersion=1&lang=de'

# Download the html from the scifi_url
download_url = requests.get(scifi_url)

# Parse the html with beautiful soup and create object
soup = BeautifulSoup(download_url.text, features="html.parser")

# Create a Local Copy.
with open("myeblaettle.html", "w") as file:
	file.write(soup.prettify())
