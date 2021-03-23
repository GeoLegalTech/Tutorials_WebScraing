# import requests
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver

# options = {
#     'proxy': {
#         'http': 'http://username:password@host:port',
#         'https': 'https://username:password@host:port',
#         'no_proxy': 'localhost,127.0.0.1' # excludes
#     }
# }

# Path chromedriver & get url
url = "https://andernach.more-rubin1.de/sitzungskalender.php"
# url = "https://www.fuerstenwalde-spree.de/amtsblatt/index.php"
path = "/Users/mr/Desktop/chromedriver"

browser = webdriver.Chrome(path)
browser.get(url)

# Click button
elem = browser.find_element_by_xpath("//div[@id='content']//table[@class='table_sk']/tbody/tr[6]/td[@class='SKTerminTitel_td']/a[@title='5. Sitzung des Schulträgerausschusses']")
elem.click()
elem = browser.find_element_by_xpath("//div[@id='cookiebanner']//button[.='Bestätigen']")
elem.click()
# browser.implicitly_wait(10) # seconds

elem = browser.find_element_by_xpath("//div[@id='ajax_sitzungsmappe']/table/tbody/tr[4]/td[6]/form[@action='show_pdf.php']/input[@alt='PDF: Vorlage']")
elem.click()

# elem = browser.find_element_by_xpath("/html//div[@id='content']//div[@class='button-wrapper']/button[@type='button']/div[@class='button-text']")
# elem.click()
https://andernach.more-rubin1.de/show_pdf.php?_typ_432=vorl&_doc_n1=20212402100045.pdf&_nk_nr=2021&_nid_nr=20212402100045&_neu_dok=&status=1&sitzungsnummer=2021-SCHA-48&x=13&y=11
# form = links.css("input[name='form']::attr(value)").extract()
# hash = links.css("input[name='hash']::attr(value)").extract()
#
# # Push the request parameters & get url
# response_post = requests.post(link_site, params={'hash':hash, 'form': form})
# link = response_post.url

# Access requests via the `requests` attribute
for request in browser.requests:
#It captures all the request data chronologica order
    if request.response.headers:
        print(
            request.path,
            request.response.status_code,
            request.response.headers,
			request.body,
			request.params,
            type(request.params) # It should be a dictionary
	    )
