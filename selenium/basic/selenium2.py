from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
# from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import requests

# Create a new instance of the Chrome driver
# Path chromedriver & get url
path = "/Users/mr/Desktop/chromedriver"
options = Options()
driver = webdriver.Chrome(path, options=options)
driver.get("https://www.myeblaettle.de/?group=1289")

driver.implicitly_wait(10)
cookies = driver.find_element(By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']")
cookies.click()
# WebDriverWait(eblaettle,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click()
# eblaettle.implicitly_wait(10)

eblaettle.switch_to_window("tab")
eblaettle.find_element_by_xpath("//a[@href='https://www.myeblaettle.de/frontend/getcatalog.do?catalogId=191056&catalogVersion=1&lang=de']").click()
# eblaettle.switch_to.window(window_handle)

# url = eblaettle.getcurrent_url()

# print (url)

# click

# elements = eblaettle.find_elements(By.CSS_SELECTOR, 'title')
#
#
eblaettle.quit()
#
#
# # Start the driver
# with webdriver.Chrome(path, options=options) as driver:
#     # Open URL
#     driver.get("https://www.myeblaettle.de/?group=1289")
#
#     # Setup wait for later
#     wait = WebDriverWait(driver, 10)
#
#     # Store the ID of the original window
#     original_window = driver.current_window_handle
#
#     # Check we don't have other windows open already
#     assert len(driver.window_handles) == 1
#
#     # Click the link which opens in a new window
#     # driver.find_element(By.LINK_TEXT, "new window").click()
#     WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click()
#
#     # Wait for the new window or tab
#     wait.until(EC.number_of_windows_to_be(2))
#
#     # Loop through until we find a new window handle
#     for window_handle in driver.window_handles:
#         if window_handle != original_window:
#             driver.switch_to.window(window_handle)
#             break
#
#     # Wait for the new tab to finish loading content
#     wait.until(EC.title_is("SeleniumHQ Browser Automation"))
