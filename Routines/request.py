import requests


def get_headers(s, sep=': ', strip_cookie=False, strip_cl=True, strip_headers: list = []) -> dict():
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

# Custom headers
h = get_headers('''
Accept: application/json, text/javascript, */*; q=0.01
Referer: https://www.myeblaettle.de/frontend/getcatalog.do?catalogId=191056&catalogVersion=1&lang=de
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36
X-Requested-With: XMLHttpRequest
''')

# URL poiting
url = "https://www.myeblaettle.de/?group=1289"
# url = "https://en65r2x3w2axx.x.pipedream.net"

# Response website
response = requests.get(url, headers=h)
print (response)
print (response.text)




# browser.get("https://www.myeblaettle.de/?group=1289")


# url = ["https://www.myeblaettle.de/?group=1289"]
#
# # Access requests via the `requests` attribute
# for request in url.requests:      #browser is a selenium driver, should be alone
#  #It captures all the requessin chronologica order
#     if request.response.headers:
#         print(
#             # request.path,
#             # # request.response.status_code,
#             # request.response.headers,
# 			# request.body,
# 			request.params,
#
# 	    )
