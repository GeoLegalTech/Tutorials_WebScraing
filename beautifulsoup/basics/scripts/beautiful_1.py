import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the html
scifi_url = 'https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_1960s'

# Download the html from the scifi_url
download_url = requests.get(scifi_url)

# Parse the html with beautiful soup and create object
soup = BeautifulSoup(download_url.text, features="html.parser")

# Create a Local Copy.
with open("download_scifi.html", "w", encoding="utf-8") as file:
	file.write(soup.prettify())

# Cleaning and preparing data
table_60 = soup.select("table.wikitable") # Extracts all
# print (table_60)

table_60_2 = soup.select("table.wikitable tbody") #Just the body
# print (table_60_2)

table_60_3 = soup.select("table.wikitable tbody")[0] #Just the body
# print (table_60_3)
# print (type(table_60_3))

# Extraction of the table column headers
head_table = table_60_3.select("tr th")
# print (head_table)
print (type(head_table))

span = soup.select("table.wikitable tr td span")
print (span)

print ("-------")
for element in head_table:
    print (element.text)

print ("-------")
for element in span:
    print (element.text)

for span in soup.find_all("tr td span"):
    print (span)


<<<<<<< HEAD:beautifulsoup/basics/beautifuls4.py
# # table_columns = []
# # for element in head_table[0 : 5]: # Selecting the first 5 titles
# #     column_label = element.get_text(separator=" ", strip=True)
# #     table_columns.append(column_label)
# #     print (column_label)
#
# # #List creation
# # n = 5
# # lists = [[] for _ in range(n)]
# # print (type(lists[1]))
# # print (lists)
#
#
# # for element in head_table: # Selecting the first 5 titles
# #     column_label = element.get_text(separator=" ", strip=True)
# #     table_columns.append(column_label)
# #     print (column_label)
#
#
# # print ("---------")
# # print (table_columns)
#
# # table_columns = []
# # for element in head_table[0 : 5]:
# #     column_label = element.get_text(separator=" ", strip=True)
# #     column_label =  column_label.replace(" ", "_")
# #     table_columns.append(column_label)
# #     print (column_label)
# #
# # print ("---------")
# # print (table_columns)
for span in soup.find_all("tr td span"):
    print (span)

# if span = united kingdom = skip 
df_list = []
for
	df_list.append(pd.DataFrame(table_data, columns=table_columns))

=======
table_columns = []
for element in head_table: # Selecting the first 5 titles

    column_label = element.get_text(separator=" ", strip=True)
    table_columns.append(column_label)
    print (column_label)


print ("---------")
print (table_columns)

table_columns = []
for element in head_table[0 : 5]:
    column_label = element.get_text(separator=" ", strip=True)
    column_label =  column_label.replace(" ", "_")
    table_columns.append(column_label)
    print (column_label)

print ("---------")
print (table_columns)
#
>>>>>>> 81d8140bee4f32b7883826c1708ed5917f6a48a4:beautifulsoup/basics/scripts/beautiful_1.py
regex=re.compile("_\[\w\]")
table_columns = []
for element in head_table[0 : 5]:
    column_label = element.get_text(separator=" ", strip=True)
    column_label =  column_label.replace(" ", "_")
    column_label =  regex.sub("", column_label)
    table_columns.append(column_label)
    print (column_label)
print ("---------")
print (table_columns)

<<<<<<< HEAD:beautifulsoup/basics/beautifuls4.py
=======


>>>>>>> 81d8140bee4f32b7883826c1708ed5917f6a48a4:beautifulsoup/basics/scripts/beautiful_1.py
# Extract the table data
rows = table_60_3.select("tr")
print (rows)

table_data = []
for index, element in enumerate(rows):
    if index > 0:
        row_list = []
        values = element.select("td")
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)
print (table_data)

<<<<<<< HEAD:beautifulsoup/basics/beautifuls4.py
# #Creating the DataFrame
# df = pd.DataFrame(table_data, columns=table_columns)
# print (df.head())
# print (df["Title"])
=======
#Creating the DataFrame
df = pd.DataFrame(table_data, columns=table_columns)
print (df.head())
print (df["Title"])
>>>>>>> 81d8140bee4f32b7883826c1708ed5917f6a48a4:beautifulsoup/basics/scripts/beautiful_1.py
