from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests


# url = 'https://www.holzwickede.de/amtsblatt/index.php'
# myobj = {'form': 'gazette_52374'}
#
# x = requests.post(url, data = myobj)
# print (x)
#
# # class Gazetteseleium()
# # Download and parse the html
# gazzete_url = "https://www.holzwickede.de/amtsblatt/index.php"
#
# # Download the html from the gazzete_url
# download_url = requests.get(gazzete_url)
#
# # Parse the html with beautiful soup and create object
# soup = BeautifulSoup(download_url.text, features="html.parser")
#
# # Create a Local Copy.
# with open("download_gazzete.html", "w") as file:
# 	file.write(soup.prettify())
#
# Path chromedriver & get url
path = "/Users/mr/Desktop/chromedriver"
browser = webdriver.Chrome(path)
browser.get("https://www.holzwickede.de/amtsblatt/index.php")
browser.implicitly_wait(10)
#
ban = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='cc_btn_accept_all']"))).click()
#
elem = browser.find_element_by_xpath("//*[@id='content']/div[7]/table/tbody/tr[3]/td[3]/form/a")
elem = browser.find_element_by_xpath("//div[@id='content']/div[7]/table//form[@name='gazette_52430']/a[@href='#gazette_52430']")
elem.submit()
print (type(elem))

# print (browser.current_url)
# # print (elem.get_attribute('onclick'))
# # # time.sleep(0.2)
# #
# # # r = requests.get("https://www.holzwickede.de/amtsblatt/index.php")
# # # print (r)
# # #


# response = requests.get("https://www.holzwickede.de/amtsblatt/index.php")
# print (response)
# print (type(response))
# print (response.status_code)


# print (browser.requests)

# for request in browser.requests:
# 	print (request.get)
	# print (WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='cc_btn_accept_all']"))).click())

# # 	request_path = request.path
# # 	request_params = request.params
# #
# # # request_path = request.path
# # print (request_path)
# # # print (type(request_path))
# # # print (type(request_params))
# # # print (request_params)
#
# Access requests via the `requests` attribute
for request in browser.requests:      #browser is a selenium driver, should be alone
 #It captures all the requessin chronologica order
    if request.response.headers:
        print(
            # request.path,
            # # request.response.status_code,
            # request.response.headers,
			# request.body,
			request.params,

	    )
# print (type(browser.requests))

# z = None
#
# for r in browser.requests:
# 	if r.path == browser.current_url:
# 		z = r
#
# print (r.response)
# out_html = browser.find_element_by_xpath("//*")
# print (elem.get_attribute("outerHTML"))
# print (requered_url)
