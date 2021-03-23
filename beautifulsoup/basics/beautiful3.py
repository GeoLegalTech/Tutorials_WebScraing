import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the html
scifi_url = "https://schifferstadt.more-rubin1.de/meeting.php?sid=ni_2021-03-150"

# Download the html from the scifi_url
download_url = requests.get(scifi_url)

# Parse the html with beautiful soup and create object
soup = BeautifulSoup(download_url.text, features="html.parser")

# Create a Local Copy.
with open("rubin.html", "w") as file:
	file.write(soup.prettify())
