from urllib.parse import urlparse

url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?"
parts = urlparse(url)
parts = parts._replace(query = 'skc_zeitraum=1&skc_ansicht=k&d_von=HOLA&d_bis=2021-01&koerperschaft=')
print (parts.geturl())


url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft="
parts = urlparse(url)
url =  parts.geturl()
print (url)
base_url = urlparse(base)
base_url._replace(query="query=skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft=")
base_url = base_url.geturl()




base_url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft="
for month_num in range(1, 5):
    url = urlparse(base_url)
    month = url.query.split('=')[3].split('&')[0].split('-')[1]
    parts = url.query
    parts = parts.replace(month, "0" + str(month_num))
    url = url._replace(query=parts)
    url = url.geturl()
    print (url)
