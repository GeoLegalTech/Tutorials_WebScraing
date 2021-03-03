import requests
from requests.exceptions import HTTPError
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
# # Path chromedriver & get url
# path = "/Users/mr/Desktop/chromedriver"
# browser = webdriver.Chrome(path)

# # # Create the response from the actions
# # for request in browser.requests:
# # 	# print (request.get)
# # browser.get("https://www.myeblaettle.de/?group=1289")
# # browser.implicitly_wait(10)
#
# def get_headers(s, sep=': ', strip_cookie=False, strip_cl=True, strip_headers: list = []) -> dict():
#     d = dict()
#     for kv in s.split('\n'):
#         kv = kv.strip()
#         if kv and sep in kv:
#             v=''
#             k = kv.split(sep)[0]
#             if len(kv.split(sep)) == 1:
#                 v = ''
#             else:
#                 v = kv.split(sep)[1]
#             if v == '\'\'':
#                 v =''
#             # v = kv.split(sep)[1]
#             if strip_cookie and k.lower() == 'cookie': continue
#             if strip_cl and k.lower() == 'content-length': continue
#             if k in strip_headers: continue
#             d[k] = v
#     return d
#
# # Custom headers
# h = get_headers('''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
# Cache-Control: max-age=0
# Connection: keep-alive
# Cookie: _ga=GA1.2.1973768868.1614089083;
# Host: www.myeblaettle.de
# If-Modified-Since: Tue, 12 Jan 2021 15:07:30 GMT
# If-None-Match: W/"5ffdbb32-16d9"
# sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
# sec-ch-ua-mobile: ?0
# Sec-Fetch-Dest: document
# Sec-Fetch-Mode: navigate
# Sec-Fetch-Site: none
# Sec-Fetch-User: ?1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
#
# ''')
#
# url = "https://www.myeblaettle.de/?group=1289"
# make HTTP GET rewquests

# Path chromedriver & get url
path = "/Users/mr/Desktop/chromedriver"
browser = webdriver.Chrome(path)
response = browser.get(url)
# print (response)

# print (WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click())
WebDriverWait(browser,50).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click()
elem = browser.find_element_by_xpath("//span")
