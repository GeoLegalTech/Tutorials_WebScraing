import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the html
scifi_url = 'https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_1960s'

# Download the html from the scifi_url
download_url = requests.get(scifi_url)

# Parse the html with beautiful soup and create object
soup = BeautifulSoup(download_url.text)

# Create a Local Copy.
with open("download_scifi.html", "w") as file:
	file.write(soup.prettify())

# Cleaning and preparing data
table_60 = soup.select("table.wikitable")
print (table_60)

table_60_2 = soup.select("table.wikitable tbody") #Just the body
print (table_60_2)

table_60_3 = soup.select("table.wikitable tbody")[0] #Just the body
print (table_60_3)

# Extraction of the table column headers
head_table = table_60_3.select("tr th")
print (head_table)

print ("-------")
for element in head_table:
    print (element.text)

table_columns = []
for element in table_head:
    column_label = element.get_text(separator=" ", strip=True)
    table_columns.append(column_label)
    print (column_label)
print ("---------")
print (table_columns)

table_columns = []
for element in table_head:
    column_label = element.get_text(separator=" ", strip=True)
    column_label =  column_label.replace(" ", "_")
    table_columns.append(column_label)
    print (column_label)

print ("---------")
print (table_columns)

regex=re.compile("_\[\w\]")
table_columns = []
for element in table_head:
    column_label = element.get_text(separator=" ", strip=True)
    column_label =  column_label.replace(" ", "_")
    column_label =  regex.sub("", column_label)
    table_columns.append(column_label)
    print (column_label)
print ("---------")
print (table_columns)

# Extract the table data
rows = full_table.select("tr")
print (rows)

table_data = []
for index, element in enumerate(table_data):
    if index > 0:
        row_list = []
        values = element.select("td")
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)
print (table_data)

#Creating the DataFrame
df = pd.DataFrame(table_data, columns=table_columns)
print (df)
