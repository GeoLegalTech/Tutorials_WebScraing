import requests
import pandas as pd

# Functions
def get_headers(s, sep=': ', strip_cookie=False, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d

# URL & headers
# urls = ['https://www.lokalmatador.de/epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/deckenpfronner-wochenblatt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-bad-ueberkingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-kuchen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-schlat/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-waeschenbeuren/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-wangen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-gingen-an-der-fils/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/suessener-mitteilungen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-stadt-uhingen-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-hessigheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/aktuell-amtsblatt-der-gemeinde-mundelsheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/neckartal-anzeiger/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/benninger-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-auenwald/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/die-bruecke-amtliches-bekanntmachungsblatt-der-gemeinde-oppenweiler/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-kaisersbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/leute-amtsblatt-der-gemeinde-leutenbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gundelsheimer-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/friedrichshaller-rundblick/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-oedheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-offenau/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-grossen-kreisstadt-bad-rappenau/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-cleebronn/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/fleiner-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-talheim-heilbronn/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/lauffener-bote/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtliches-mitteilungsblatt-der-gemeinde-nordheim-mit-ortsteil-nordhausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/moeckmuehler-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/nachrichten-aus-erlenbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-untereisesheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-hardthausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/neuenstadter-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/loewensteiner-chronik/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/obersulmer-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/abstatt-im-schozachtal-aktuell-ortsnachrichten-der-gemeinde-abstatt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/beilsteiner-mitteilungen-amtsblatt-der-stadt-beilstein/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/die-bruecke-amtsblatt-der-gemeinde-untergruppenbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/eberstaedter-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/ellhofener-heimatschau/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/lehrensteinsfeld-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtliches-mitteilungsblatt-gemeinde-kupferzell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-zweiflingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtliche-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/oestringer-stadtnachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-eggenstein-leopoldshafen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-stadt-waghaeusel/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/stutensee-woche-amtsblatt-der-grossen-kreisstadt-stutensee/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-kronau/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-hambruecken/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/karlsdorf-neutharder-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/graben-neudorf-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/dettenheimer-anzeige/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-mit-ortsnachrichten-der-gemeinde-hassmersheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-hueffenhardt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/kleiner-odenwald-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-neckarzimmern/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-sandhausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-stadt-schriesheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/walldorfer-rundschau/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-st-leon-rot/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/hemsbacher-woche/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/lussheimer-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/lussheimer-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/reilinger-nachrichten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/sinsheimer-stadtanzeiger/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-angelbachtal/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-zuzenhausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/nachrichtenblatt-brunnenregion/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/calwjournal/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeine-ebhausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-stadt-haiterbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/buergerblatt-amtsblatt-der-gemeinde-rohrdorf/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/hoefener-chronik/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-gemeinde-neuhausen-im-enzkreis/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amts-und-mitteilungsblatt-der-gemeinde-glatten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-gemeinde-empfingen-mit-den-gemeindeteilen-wiesenstetten-und-dommelsberg/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gemeinde-eutingen-im-gaeu-eutingen-goettelfingen-rohrdorf-weitingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-horb-am-neckar/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-fluorn-winzeln/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/stadt-rottweil-mitteilungsblatt-fuer-die-stadtteile/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/dietinger-nachrichten-zwischen-schwarzwald-und-schwaebischer-alb/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/aichhalder-nachrichten-amtsblatt-der-gemeinde-aichhalden/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/buerger-gemeinde-amtsblatt-und-gaeste-journal-von-lauterbach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-stadt-sulz-am-neckar/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-voehringen-mit-ortsteil-wittershausen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/bad-duerrheimer-nachrichten-amtliches-mitteilungsblatt-der-stadt-bad-duerrheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-des-heilklimatischen-kurortes-schoenwald-im-schwarzwald/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/schonacher-nachrichten-mitteilungsblatt-der-gemeinde-schonach-im-schwarzwald/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gemeinde-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/tuninger-bote-das-amtsblatt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-bubsheim/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-deilingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/duerbheim-aktuell/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gunninger-nachrichten-amtliches-mitteilungsblatt-der-gemeinde-gunningen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-der-gemeinde-talheim-tuttlingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-trossingen-musikstadt/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/mitteilungsblatt-gemeinde-seitingen-oberflacht/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-der-gemeinde-ammerbuch/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gemeindebote-amtsblatt-der-gemeinde-nehren/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gemeindebote-ofterdingen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/gemeindebote-amtsblatt-der-gemeinde-neustetten/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/rottenburger-mitteilungen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/starzach-bote-amtsblatt-der-gemeinde-starzach/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/nusplinger-mitteilungen/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/amtsblatt-stadt-schoemberg/',
# 'https://www.lokalmatador.de/epaper/lokalzeitung/weingarten-im-blick-amtsblatt-der-stadt-weingarten/']
# url = "https://enzrlspj3web.x.pipedream.net/"
# url = "https://www.fuerstenwalde-spree.de/amtsblatt/index.php"
# url = "https://www.lokalmatador.de/epaper/lokalzeitung/wochenblatt-der-stadt-weil-der-stadt/"
url = "https://www.lokalmatador.de/epaper/ausgabe/wochenblatt-der-stadt-weil-der-stadt-27-2021/"

h = get_headers('''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
If-Modified-Since: Tue, 12 Jan 2021 15:07:30 GMT
If-None-Match: W/"5ffdbb32-16d9"
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
''')

# for url in urls:
#     requ = requests.get(url, headers=h)
#     if requ.status_code != 200:
#         print ("The website is not accesible")
#         print (requ.url + "   ----->   " + str(requ.status_code))

# Request the website (single url)
requ = requests.get(url, headers=h)
print (requ.headers)
print (requ)
# Headers and info
# print (requ.status_code)
# print (requ.headers)
# # Static webpage text
# print (requ.text)
# # Non text requests, same as text
# print (requ.content)
# print (requ.status_code)
