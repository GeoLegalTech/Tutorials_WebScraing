# import requests
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# from selenium import webdriver

# options = {
#     'proxy': {
#         'http': 'http://username:password@host:port',
#         'https': 'https://username:password@host:port',
#         'no_proxy': 'localhost,127.0.0.1' # excludes
#     }
# }

# # Path chromedriver & get url
# url = "https://andernach.more-rubin1.de/sitzungskalender.php"
# # url = "https://www.fuerstenwalde-spree.de/amtsblatt/index.php"
# path = "/Users/mr/Desktop/chromedriver"
#
# browser = webdriver.Chrome(path)
# browser.get(url)


# # Click button
# elem = browser.find_element_by_xpath("//div[@id='content']//table[@class='table_sk']/tbody/tr[6]/td[@class='SKTerminTitel_td']/a[@title='5. Sitzung des Schulträgerausschusses']")
# elem.click()
# elem = browser.find_element_by_xpath("//div[@id='cookiebanner']//button[.='Bestätigen']")
# elem.click()
# # browser.implicitly_wait(10) # seconds
#
# elem = browser.find_element_by_xpath("//div[@id='ajax_sitzungsmappe']/table/tbody/tr[4]/td[6]/form[@action='show_pdf.php']/input[@alt='PDF: Vorlage']")
# elem.click()
#
# # elem = browser.find_element_by_xpath("/html//div[@id='content']//div[@class='button-wrapper']/button[@type='button']/div[@class='button-text']")
# # elem.click()
# https://andernach.more-rubin1.de/show_pdf.php?_typ_432=vorl&_doc_n1=20212402100045.pdf&_nk_nr=2021&_nid_nr=20212402100045&_neu_dok=&status=1&sitzungsnummer=2021-SCHA-48&x=13&y=11
# https://schifferstadt.more-rubin1.de/show_pdf.php?_typ_432=vorl&_doc_n1=222202100017.pdf&_nk_nr=2021&_nid_nr=222202100017&_neu_dok=&status=1&sitzungsnummer=2021-SCHA-48&x=13&y=11
# # schifferstadt.more-rubin1.de
# # form = links.css("input[name='form']::attr(value)").extract()
# # hash = links.css("input[name='hash']::attr(value)").extract()
# #
# # # Push the request parameters & get url
# # response_post = requests.post(link_site, params={'hash':hash, 'form': form})
# # link = response_post.url
#
# # Access requests via the `requests` attribute
# for request in browser.requests:
# #It captures all the request data chronologica order
#     if request.response.headers:
#         print(
#             request.path,
#             request.response.status_code,
#             request.response.headers,
# 			request.body,
# 			request.params,
#             type(request.params) # It should be a dictionary
# 	    )


# options = Options()
# options.page_load_strategy = 'eager'
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

# Path chromedriver & get url
# url = "https://schoenebeck.more-rubin1.de/sitzungskalender.php"
url = "https://www.lokalmatador.de/epaper/ausgabe/wochenblatt-der-stadt-weil-der-stadt-27-2021/"
# url = "https://www.fuerstenwalde-spree.de/amtsblatt/index.php"
path = "/Users/mr/Desktop/chromedriver"

browser = webdriver.Chrome(path)
browser.get(url)
# /html//a[@id='download-hint']
# Click button
# browser.implicitly_wait(10)
elem = browser.find_element_by_xpath("/html//a[@id='download-hint']")
elem.click()
# elem = browser.find_element_by_xpath("/html//div[@id='content']/div[@class='meeting-page']/div/div[4]/div[3]/div[7]/div[@class='agenda-item-content']//a[@href='/vorlagen_details.php?vid=20211612100000']//div[.='Beschlussvorlage']")
# elem.click()
# elem = browser.find_element_by_xpath("/html//div[@id='content']//div[@class='button-wrapper']/button[@type='button']/div[@class='button-text']")
# elem.click()
# # browser.implicitly_wait(10)
# elem = browser.find_element_by_xpath("/html//img[@id='button-download']")
# elem.click()



# Access requests via the `requests` attribute
for request in browser.requests:
#It captures all the request data chronologica order
    if request.response.headers:
        print(

            request.path,
            request.response.status_code,
            request.response.headers,
			request.body,
            request.response,
			request.params,

            type(request.params) # It should be a dictionary
	    )

# # browser.implicitly_wait(10) # seconds
#
# elem = browser.find_element_by_xpath("//div[@id='ajax_sitzungsmappe']/table/tbody/tr[4]/td[6]/form[@action='show_pdf.php']/input[@alt='PDF: Vorlage']")
# elem.click()
