import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

# Reading the source code and actions
# Path chromedriver & get url
path = "/Users/mr/Desktop/chromedriver"
browser = webdriver.Chrome(path)

browser.get("https://www.myeblaettle.de/?group=1289")
browser.implicitly_wait(10)

# # Create the response from the actions
# for request in browser.requests:
# 	# print (request.get)
print (WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click())


# elem = browser.find_element_by_xpath("//*[@id='content']/div[7]/table/tbody/tr[3]/td[3]/form/a")
elem = browser.find_element_by_xpath("//div[@id='list']/div[1]/div[@class='inner']/div/a[@href='https://www.myeblaettle.de/frontend/getcatalog.do?catalogId=189943&catalogVersion=1&lang=de']").click()
# elem.submit()
print (elem)
print (type(elem))

# url = ["https://www.myeblaettle.de/?group=1289"]
#
# # Access requests via the `requests` attribute
# for request in url.requests:      #browser is a selenium driver, should be alone
#  #It captures all the requessin chronologica order
#     if request.response.headers:
#         print(
#             # request.path,
#             # # request.response.status_code,
#             # request.response.headers,
# 			# request.body,
# 			request.params,
#
# 	    )
