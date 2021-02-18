from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests


# class Gazetteseleium()
# Download and parse the html
gazzete_url = "https://www.holzwickede.de/amtsblatt/index.php"

# Download the html from the gazzete_url
download_url = requests.get(gazzete_url)

# Parse the html with beautiful soup and create object
soup = BeautifulSoup(download_url.text, features="html.parser")

# Create a Local Copy.
with open("download_gazzete.html", "w") as file:
	file.write(soup.prettify())

# Path chromedriver & get url
path = "/Users/mr/Desktop/chromedriver"
browser = webdriver.Chrome(path)
browser.get("https://www.holzwickede.de/amtsblatt/index.php")
# browser.implicitly_wait(10)

ban = WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='cc_btn_accept_all']"))).click()


elem = browser.find_element_by_xpath("//div[@id='content']/div[7]/table//form[@name='gazette_52430']/a[@href='#gazette_52430']")
elem.click()
print (browser.current_url)
print (elem.get_attribute('onclick'))
# time.sleep(0.2)

# out_html = browser.find_element_by_xpath("//*")
# print (elem.get_attribute("outerHTML"))
# print (requered_url)
