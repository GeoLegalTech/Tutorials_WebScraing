# Script to pass cookies along with HTTP request
#         using"requests" package
#
#        Code by GeoMario

# Packages
import scrapy
from scrapy.crawler import CrawlerProcess

# spider class
class HeadersCookies(scrapy.Spider):
    name = "headerscookies"
    url = "https://enbph9omv9wjj.x.pipedream.net/"
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,es;q=0.8,de;q=0.7,en-GB;q=0.6",
    "cache-control": "max-age=0",
    "cookie": "_gcl_au=1.1.1265878579.1614168471; _ga=GA1.2.1821975775.1614168471; _gid=GA1.2.911280566.1614168471; _hjid=a6e226a3-de63-43f8-af00-2edfd0a06016; _hjFirstSeen=1; ki_r=; _hjAbsoluteSessionInProgress=1; ki_t=1614168471370%3B1614168471370%3B1614168745665%3B1%3B4; _gat_UA-128559955-1=1; amplitude_id_eadd7e2135597c308ef5d9db3651c843requestbin.com=eyJkZXZpY2VJZCI6ImNiNGY3MGIyLTNjNmMtNDA5MC1iZTg1LTA4Mzc0Y2NjNjk3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYxNDE2ODQ3MTE1NiwibGFzdEV2ZW50VGltZSI6MTYxNDE2ODc0NzMyMSwiZXZlbnRJZCI6NSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjV9; _uetsid=f262bde0769811ebbd4b11ab02b4aaa1; _uetvid=f262d560769811eb9bd2b7fefe560a9d",
    "sec-ch-ua":"'Chromium';v='88', 'Google Chrome';v='88', ';Not A Brand';v='99'",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

    }

    def start_requests(self):
        # mAKE hTTP GET REQUEST TO 'requestbin.com'
        yield scrapy.Request(
            url = self.url,
            headers=self.headers,
            callback= self.parse
            )

    def parse(self, response):
        print (response.text)

#Main driver

if __name__== '__main__':
    process = CrawlerProcess()
    process.crawl(HeadersCookies)
    process.start()
