import requests
from requests.exceptions import HTTPError
from elasticsearch import Elasticsearch

# site_url = 'https://www.holzwickede.de/amtsblatt/index.php'
# key_para = {'hash': '78e0b577cc3f4cda791b8c414070495e', 'form': 'gazette_52430'}

# site_url = 'https://schoenebeck.more-rubin1.de/documents.php'
# key_para = {
# 'document_type_id':'13',
# 'submission_attachment_id':'202111502100002.pdf',
# 'id':'69',
# 'json':'1',
# 'platform':'ris'
# }

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

params = {
'_typ_432' : 'vorl',
'_doc_n1' : "20212502100061.pdf",
'_nk_nr' : '2021',
'_nid_nr': '20212502100061',
'_neu_dok':'',
'status': '1',
'sitzungsnummer' : 'ni_2021-KSSS-20'
}
site_url = "https://stadtfehmarn.more-rubin1.de/show_pdf.php"
#https://andernach.more-rubin1.de/show_pdf.php?_typ_432=vorl&_doc_n1=20212402100045.pdf&_nk_nr=2021&_nid_nr=20212402100045&_neu_dok=&status=1&sitzungsnummer=2021-SCHA-48&x=13&y=11

response_params = requests.get(site_url, params=params)
print (response_params.url)

params = {
'_typ_432' : 'vorl',
'sid' : '2021-STV-48',
'_topst': '1',
'_vorl_nr': '20210803100101',
'_doc_n1' : '20210308150434-0.pdf'
}
site_url = "https://stadtfehmarn.more-rubin1.de/anlagen.php"

response_params = requests.get(site_url, params=params)
print (response_params.url)
########


site_url="https://schifferstadt.more-rubin1.de/meeting.php?sid=ni_2021-02-129"
response_params = requests.get(site_url, params="ni_2021-02-129")
print (response_params.url)
