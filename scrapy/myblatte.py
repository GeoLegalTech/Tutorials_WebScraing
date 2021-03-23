import scrapy
import json
from urllib.parse import urlparse
from PyPDF2 import PdfFileReader
from datetime import datetime

# Define functions
def get_headers(s, sep=': ', strip_cookie=False, strip_cl=True, strip_headers: list = []) -> dict():
    """ Function adapted and taken from GitHub """
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d



class MyblatteSpider(scrapy.Spider):
    name = 'myblatte'
    start_urls = ['https://www.myeblaettle.de/?group=1289', 'https://www.myeblaettle.de/?group=1281']
    headers = get_headers('''
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6
    Connection: keep-alive
    Cookie: JSESSIONID=1C8FB6174CE3B4A7E3D827033026D902; _ga=GA1.2.416603156.1614336675; _gid=GA1.2.567457664.1614593357; _gat=1
    Host: www.myeblaettle.de
    Referer: https://www.myeblaettle.de/
    sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
    sec-ch-ua-mobile: ?0
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36
    X-Requested-With: XMLHttpRequest
    ''')

    def parse(self, response):
        # url = "https://www.myeblaettle.de/frontend/mvc/issueFeed/groupsAndIssues?&position=0&group=1289&allMode=false&mode=public"
        for issue_num in range(1289, 1427):
            base_url = "https://www.myeblaettle.de/frontend/mvc/issueFeed/groupsAndIssues?&position=0&group=1289&allMode=false&mode=public"
            url = urlparse(base_url)
            issue = url.query.split('=')[2].split('&')[0]
            parts = url.query
            parts = parts.replace(issue, str(issue_num))
            url = url._replace(query=parts)
            url = url.geturl()


            yield scrapy.Request(url,
            callback= self.parse_api,
            headers=self.headers)


    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        for issue in data["issues"]:
            for key in issue:
                if key == 'id':
                    link = 'https://www.myeblaettle.de/frontend/catalogs/'+str(issue[key])+'/1/pdf/complete.pdf'
                    print (link)
                    # path = "/Users/mr/Documents/scrapy_tutorial/Routines/2021-02-24 (34).pdf"

                    with open(link, "rb") as f:
                        pdf = PdfFileReader(f)
                        info = pdf.getDocumentInfo()
                        number_pages = pdf.getNumPages()
                        # date = datetime.strptime(info["/ModDate"],'%y/%m/%d %H:%M:%S')

                    print (info)
                    print (date)

                else :
                    pass

        yield {
        "linkid" : link
        }
