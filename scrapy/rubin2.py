import re
import json
import scrapy
import requests
from datetime import datetime
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess

class Pagination(scrapy.Spider):
    name = 'pagination_rubin'
    start_urls = ["https://schifferstadt.more-rubin1.de/sitzungskalender.php"] #, "https://andernach.more-rubin1.de/sitzungskalender.php"]
    # start_urls = ["https://andernach.more-rubin1.de/sitzungskalender.php"] #, "https://andernach.more-rubin1.de/sitzungskalender.php" , "https://schifferstadt.more-rubin1.de/sitzungskalender.php", "https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://amt-sylt.more-rubin1.de/sitzungskalender.php", "https://stadtfehmarn.more-rubin1.de/sitzungskalender.php"]

    # # Make the asynchron stopping (Requests one by one)
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 0,                    #Secs
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1    #Secs
    # }

    def __init__(self):
        # pass
        new_starturl = []
        for new_link in self.start_urls:
            trial_url = urlparse(new_link)
            trial_url =  trial_url._replace(query="skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft=")
            base_url = trial_url.geturl()
            for month_num in range(1, 4):
                url = urlparse(base_url)
                month = url.query.split('=')[3].split('&')[0].split('-')[1]
                parts = url.query
                parts = parts.replace(month, "0" + str(month_num))
                url = url._replace(query=parts)
                url = url.geturl()
                new_starturl.append(url)
                self.start_urls = new_starturl
        # Control flag
        # print (self.start_urls)

    def parse(self, response):
        # pass
        get = response.css("form[method=get]")
        sid = get.css("input[name='sid']::attr(value)").getall()
        for link in sid:
            parse_url = urlparse(response.url)
            parse_url = parse_url._replace(path="meeting.php")
            parse_url = parse_url._replace(query="sid=")
            parse_url = parse_url.geturl()
            parse_url = parse_url + link
            print (parse_url)

            if parse_url is not None:
                yield scrapy.Request(parse_url, callback=self.parse_doc)


    def parse_doc(self, response):
        # pass
        div = response.css("div[id='content']")
        for links in div:
            querys = links.css("div[component='MeetingPage']::attr(vue-passed-meeting)").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
            for query_new in querys:
                parse_url = urlparse(response.url)
                parse_url = parse_url._replace(path="documents.php")
                parse_url = parse_url._replace(query=query_new)
                parse_url = parse_url.geturl()
                print (parse_url)

# run scraper
process = CrawlerProcess()
process.crawl(Pagination)
process.start()
