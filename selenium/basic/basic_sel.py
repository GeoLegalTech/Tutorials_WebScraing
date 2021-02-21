# Modules
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
    return driver

def getPDF(driver, search_keyword):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    driver.get(f"https://www.pluralsight.com/search?q={search_keyword}&categories=course")
    # wait for the element to load
    try:
        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("search-results-category-target").is_displayed())
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None
