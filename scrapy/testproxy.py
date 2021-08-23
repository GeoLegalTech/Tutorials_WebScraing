from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_extension("proxy.zip")

driver = webdriver.Chrome(executable_path="/Users/mr/Desktop/chromedriver", chrome_options=chrome_options)
driver.get("http://google.com")
driver.close()
