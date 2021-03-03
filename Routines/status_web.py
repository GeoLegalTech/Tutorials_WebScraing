import requests
from requests.exceptions import HTTPError
from elasticsearch import Elasticsearch

df = pd.read_excel("/Users/mr/Documents/glt/pdfcrawl/ES/GLT_Quellen_all.xlsx")
print (df.head())
print (df.info())



# df = df.apply(pd.to_numeric)
# print (df.head())

# site_url = 'https://www.holzwickede.de/amtsblatt/index.php'
# key_para = {'hash': '78e0b577cc3f4cda791b8c414070495e', 'form': 'gazette_52430'}
#
# for url in ['https://www.holzwickede.de/amtsblatt/index.php']:
#     try:
#         response = requests.post(site_url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')
#
# response_params = requests.post(site_url)
# print (response_params.text)
# print (type(response_params))
#
# response = requests.post(site_url, params=key_para)
# print (response.url)
