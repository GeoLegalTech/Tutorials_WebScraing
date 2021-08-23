from urllib.parse import urlparse

url = "https://www.lokalmatador.de/epaper/lokalzeitung/deckenpfronner-wochenblatt/"
parts = urlparse(url)
print (parts.netloc)
