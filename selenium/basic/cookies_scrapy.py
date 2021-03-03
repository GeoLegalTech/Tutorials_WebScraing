# packages
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


# class SpiderSpider(CrawlerSpider):
#     # This spider does not parse the HTML directly
#     name = "catalog"
#     a
#
#



# scraper class
class Scraper(scrapy.Spider):
    # name
    name = 'scraper'

    # custom headers
    headers = {'''
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _ga=GA1.2.416603156.1614336675; _gid=GA1.2.567457664.1614593357
Host: www.myeblaettle.de
If-Modified-Since: Tue, 12 Jan 2021 15:07:30 GMT
If-None-Match: W/"5ffdbb32-16d9"
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36
    '''}

    # custom settings
    custom_settings = {
        'COOKIES_ENABLED': False,
    }

    # crawler's entry point
    def start_requests(self):
        # cookie string
        cookies_raw = 'PHPSESSID=je2ihl1lhr92jech7j13bind4m; currentCurrency=EUR; _pubcid=27fb85ca-08bd-451b-b530-24d82ecb19ac; _ga=GA1.2.1782779244.1591116926; _fbp=fb.1.1591116927166.1660527984; __beaconTrackerID=bjslrvk08; pbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMO-IfC2hLDioNVmEbVWDvFJy2lmvjGeshZ0iR8SQ%22%2C%22ID5ID_CREATED_AT%22%3A%222020-01-21T16%3A44%3A03.879Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D; _gid=GA1.2.320661592.1591258798; spitogatosHomepageMap=0; __gads=ID=1be9586193cfdbf7:T=1591258837:S=ALNI_Mbk6BSxt8QA47TPFhU2Gkm8M-kgeg; spitogatosS=areaIDs%255B0%255D%3D2022%26areaIDs%255B1%255D%3D2038%26areaIDs%255B2%255D%3D2610%26areaIDs%255B3%255D%3D2616%26areaIDs%255B4%255D%3D3011%26areaIDs%255B5%255D%3D6007%26areaIDs%255B6%255D%3D6013%26areaIDs%255B7%255D%3D6116%26areaIDs%255B8%255D%3D6119%26areaIDs%255B9%255D%3D384410%26propertyCategory%3Dresidential%26listingType%3Dsale%26priceHigh%3D30000; PHPSESSID=fs93223qkf61k8c6a5f589bsdh; eupubconsent=BO0eApgO0eApgAKAiAENAAAAgAAAAA; euconsent=BO0eApgO0eApgAKAiBENDM-AAAAv5r_7__7-_9f-_f__9uj3Gr_v_f__32ccL5tv3h_7v-_7fi_-0nV4u_1vft9ydk1-5ctDztp507iakiPHmqNeb1n_mz1eZpRP58E09j5335Ew_v8_v-b7BCPN9Y3v-8K94A; _hjid=43265493-46ec-47f4-91bc-c39f2bcbcf8c; _hjAbsoluteSessionInProgress=1; pbjs-id5id_last=Thu%2C%2004%20Jun%202020%2011%3A49%3A32%20GMT; _cmpQcif3pcsupported=1; reese84=3:jxqIwTqiLz8mKueAzd9aow==:H0PTobQNDZdcAR/lsI4iYLAs63+mGPfIKbiYt7F1CvBOj2Tx2Qkoj20WvmGThGOy8ocix50Oute8jr0EXxf/zsBOUcC6hTDEaXWnTzpX0fgDHcLiFSwhZg3ywQreC8VN2baA1u2mjDyaLWt5H1gla6hxqCghCr8FgWNAKHulvILcztPdUnSZ50yCcPPU9jXgZV5hMim2/1KoU1thQWkLNHzveT7D7qxiqte5L1+kwSxAcU8FHmHZAYqZU/Z9iRdTOZK7rn09F3LipA/Cl2SAaTQ8Jmn78AKLUGNHA1AOYgLMZ8Y5SOrVFteQSDeCBDQXB+NIWAIHRCTTIB/Jn0dweVg/zbt2G1Q7SAwkQ8Rbd2LxcYASPOLMdP4tXrqZ3AeIGyVP//jyQcZzqnSHkH43812sXiby4zdfKaUs2UABwrc=:fsX7D49p3eP8J1+p8RQM6zmrYt0iU1xFMo4tuVKk28g=; openedTabs=1; cto_bidid=3OI-NV9walJpTEZQNng3WUVENEsydG50ZlBYcSUyQjhaUk9kWldvZ1R2YWx5Ujc2RlZndjZmaG1kdFZHTTVwaTZFVXVkJTJCWmNRWVhLVzFjNzZWcW4weUc5cEdNSG9majBVdktjSWZqU2VDRHowOXZMeHclM0Q; cto_bundle=wX9lHl9wd2h5JTJCNDRTZSUyQmlVODJxUjNFbXdkJTJGMmJ4ZDVaSjVpSUMyRjk4JTJGUjlZdEE4TWk3TndTSTFtUTlxckJrOFpQSEZ6TnlMMXdJJTJCbXc1emh4emEzYklRc3hZNXQyUUE1SFhEdVA3OXJ5djFqWU9icWo0dko4N01VZjMxTXF0YW5BMXBObUVKRHYzJTJCOUZSd1BIU2xXVkRMbFElM0QlM0Q; DigiTrust.v1.identity=eyJpZCI6IlVGcWFTZVNZR3NaYXN6ZEY1UzYwM3VLT25FaGl2WmRSN0VGRDBhRHl5Rm15L2E1RHdORzZwdlNnWHRXSHRIK2ZUbXFWaGkwOWxERWtZYmRwRThBckMwNUo5OWhoWVgyZFp4Zk11eW1IaVpRZkdRSWtoS1VMT2swVC9sVk9hVk5EdVM4VGhtdFZKYU4rYXdyN2o2ZjJYMzB5QlUwUWhSOWdIVXlmdVFTMmJwdllGWVNnUXZrVWxHNDZYZ3l3cEh6Q00vUzFwMGd2aXN5cnRSbnNTM3V2Slg4czQzb0tYTzUyYXk5MFhGMHlRNG1Jc0VYVXl2TDRpSGMxaEcvRUJTdjF3YzVWMTI1SGQrUzFseVJ1V0c1NGppVkw1ZklYWTE3dDNMZUo0dkxBNm54eWhjOVhjR2h0eFhvRGFlRDFtZWtOTkVHU3V3c0hnb1NwcjlxcnVNK2dwdz09IiwidmVyc2lvbiI6MiwicHJvZHVjZXIiOiIxQ3JzZFVOQW82IiwicHJpdmFjeSI6eyJvcHRvdXQiOmZhbHNlfSwia2V5diI6NH0%3D; _gat_UA-3455846-10=1; _gat_UA-3455846-3=1'

        # cookies dictionary
        cookies = {}

        # lop over cookies string
        for cookie in cookies_raw.split(';'):
            # init key value pairs
            key = cookie.strip().split('=')[0]
            val = cookie.strip().split('=')[-1]

            # init cookies
            cookies[key] = val

        print(json.dumps(cookies, indent=2))

        # rules = [Rule(LinkExtractor(allow=(), restrict_xpaths=("//button[@id='cookieNoticeAcceptAllButton']",)), callback="parse", follow= True),]

        # make HTTP request
        yield scrapy.Request(
            # url='https://enz1wja3z814s.x.pipedream.net/',
            url='https://www.myeblaettle.de/?group=1289',
            headers=self.headers,
            #cookies=cookies,
            callback=self.parse
        )

    # parse response
    def parse(self, response):
        # print (WebDriverWait(response,15).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='cookieNoticeAcceptAllButton']"))).click())
        print('\n\nResponse:', response.text)
        print('\n\nStatus:', response.status)

# main driver
if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Scraper)
    process.start()
