import json
import scrapy
import datetime
import requests
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from dateutil.relativedelta import relativedelta

# Define functions

def get_years_months(my_date, num_months):
    cur_month = my_date.month
    cur_year = my_date.year

    result = []
    for i in range(num_months):
        if cur_month == 0:
            cur_month = 12
            cur_year -= 1
        result.append((cur_year, cur_month))
        cur_month -= 1

    return result


class Pagination(scrapy.Spider):
    name = 'pagination_rubin'
    start_urls = ["https://andernach.more-rubin1.de/sitzungskalender.php"] # , "https://schifferstadt.more-rubin1.de/sitzungskalender.php", "https://schoenebeck.more-rubin1.de/sitzungskalender.php", "https://amt-sylt.more-rubin1.de/sitzungskalender.php", "https://stadtfehmarn.more-rubin1.de/sitzungskalender.php"]

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
            # print (trial_url)
            trial_url =  trial_url._replace(query="skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft=")
            base_url = trial_url.geturl()
            months = get_years_months(datetime.date.today(), 4)
            for month in months:
                (month, day) = month
                new_date = str(month) + "-" + str(day)
                url = urlparse(base_url)
                old_date = url.query.split('=')[3].split('&')[0]
                parts = url.query
                parts = parts.replace(old_date, new_date)
                url = url._replace(query=parts)
                url = url.geturl()
                new_starturl.append(url)
                self.start_urls = new_starturl

        # Control flag
        print (self.start_urls)

    def parse(self, response):
        # print (response)
        # pass
        # # print('response url:', response.url) #Control flag
        #
        post = response.css("form[method=post]")
        # print (post)
        hash = post.css("input[name='sid']::attr(value)").extract()
        print (hash)
        #
        # for link in hash:
        #     parse_url = urlparse(response.url)
        #     parse_url = parse_url._replace(path="sitzungen_top.php")
        #     parse_url = parse_url._replace(query="sid=")
        #     parse_url = parse_url.geturl()
        #     parse_url = parse_url + link
        #     # print ("Test URL: ")
        #     # print (parse_url)
        #
        #     # for link in parse_url:
        #     if parse_url is not None:
        #         yield scrapy.Request(parse_url, callback=self.parse_doc)

    def parse_doc(self, response):
        pass
        # print (self.response)
        # div = response.css("div[id='content']")
        # for links in div:
        #     querys = links.xpath("//script/text()").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
        #     ''' Old system '''
        #     # print (len(links.xpath("//script/text()").getall()))
        #     # querys = links.css("div[component='MeetingPage']::attr(vue-passed-meeting)").re(r'document_type_id+=\d+&[a-zA-Z]+[_a-zA-Z]+=[a-zA-Z_\d\w\.\-\%\&\=]+')
        #     ''' Old system '''
        #     for query_new in querys:
        #         parse_url = urlparse(response.url)
        #         parse_url = parse_url._replace(path="documents.php")
        #         parse_url = parse_url._replace(query=query_new)
        #         parse_url = parse_url.geturl()
        #         print (parse_url)

        # get = response.css("form[method=get]")
        # for links in get:
        #     parse_url = urlparse(response.url)
        #     typ = links.css("input[name='_typ_432']::attr(value)").get()
        #     doc = links.css("input[name='_doc_n1']::attr(value)").get()
        #     nk  = links.css("input[name='_nk_nr']::attr(value)").get()
        #     nid = links.css("input[name='_nid_nr']::attr(value)").get()
        #     neu = links.css("input[name='_neu_dok']::attr(value)").get()
        #     stat = links.css("input[name='status']::attr(value)").get()
        #     sitzung = links.css("input[name='sitzungsnummer']::attr(value)").get()
        #     params = {
        #     '_typ_432' : typ,
        #     '_doc_n1' : doc,
        #     '_nk_nr' : nk,
        #     '_nid_nr': nid,
        #     '_neu_dok':neu,
        #     'status': stat,
        #     'sitzungsnummer' : sitzung
        #     }
        #     site_path = "/show_pdf.php"
        #     parse_url = urlparse(response.url)
        #     site_url = parse_url.scheme + '://' + parse_url.netloc + site_path
        #     print ("site url")
        #     print (site_url)
        #     link = requests.get(site_url, params=params)
        #     # print (response.url)
        #     print ("There is no docus")
        #     print ('URL:', link.url)

# run scraper
process = CrawlerProcess()
process.crawl(Pagination)
process.start()
