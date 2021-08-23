import requests

site_url="https://www.lokalmatador.de/epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/"
response_params = requests.get(site_url)
print (response_params.url)
