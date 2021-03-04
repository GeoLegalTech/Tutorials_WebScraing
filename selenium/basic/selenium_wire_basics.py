# import requests
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Path chromedriver & get url
url = "https://en511pk9v2dyt.x.pipedream.net/"
# url = "https://www.fuerstenwalde-spree.de/amtsblatt/index.php"
path = "/Users/mr/Desktop/chromedriver"
browser = webdriver.Chrome(path)
browser.get(url)

# Click button
elem = browser.find_element_by_xpath("/html//div[@id='content']/div[4]/table//form[@name='gazette_52963']/a[@href='#gazette_52963']")
elem.click()

# Access requests via the `requests` attribute
for request in browser.requests:
#It captures all the request data chronologica order
    if request.response.headers:
        print(
            request.path,
            request.response.status_code,
            request.response.headers,
			request.body,
			# request.params.url,
            type(request.params) # It should be a dictionary
	    )
