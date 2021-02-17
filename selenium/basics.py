from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/mr/Desktop/chromedriver")
browser.get("https://www.holzwickede.de/amtsblatt/index.php")

elem = browser.find_element_by_xpath("//div[@id='content']/div[7]/table//form[@name='gazette_52430']/a[@href='#gazette_52430']")
elem.click()
time.sleep(0.2)

elem = browser.find_element_by_xpath("//*")
print (elem.get_attribute("outerHTML"))


# from selenium import webdriver
#
# URL = 'https://www.holzwickede.de/amtsblatt/index.php'
# CSS_SELECTOR = '.close'
#
# browser = webdriver.Chrome("/Users/mr/Desktop/chromedriver")
# browser.implicitly_wait(10)
# browser.get(URL)
# close = browser.find_element_by_css_selector(CSS_SELECTOR)
# close.click()
#
