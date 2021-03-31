from helium import *
# import requests
# from seleniumwire import webdriver
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

browser = start_chrome("https://vgloreley.more-rubin1.de/sitzungskalender.php")
# browser = got_to("https://vgloreley.more-rubin1.de/sitzungskalender.php")
click('Sitzung des Ausschusses')
click('2021-vg-015 Auftragsvergabe der')
print (type(browser))


# # Access requests via the `requests` attribute
# for request in browser.requests:
# #It captures all the request data chronologica order
#     if request.response.headers:
#         print(
#             request.path,
#             request.response.status_code,
#             request.response.headers,
# 			request.body,
# 			request.params,
#             type(request.params) # It should be a dictionary
# 	    )
