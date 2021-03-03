from urllib.parse import urlparse

url = "https://www.myeblaettle.de/frontend/mvc/issueFeed/groupsAndIssues?&position=0&group=1289&allMode=false&mode=public"
parts = urlparse(url)
# for query in range(1289, 1427):
    # print (query)

print (parts) #url parts are printed
print (parts.geturl()) #the completed url is parsed
print (parts.query) # query division is added
print (type(parts.query)) # query is string

# print (parts.query.split('=')) # the entire url is divided
print (parts.query.split('=')[2].split('&')) # split the query
print (parts.query.split('=')[2].split('&')[0])
# print (parts.query.split('&'))

print ('-------')
n = parts.query.split('=')[2].split('&')[0]
print (n)

# x is the entire query
x = parts.query
x = x.replace(n, str(1600))
print ("This is my new link")
print (x)

print ("This is then my new link")
parts = parts._replace(query=x)
print (parts.geturl())


url = "https://www.myeblaettle.de/frontend/mvc/issueFeed/groupsAndIssues?&position=0&group=1289&allMode=false&mode=public"
parts = urlparse(url)


base_url = "https://www.myeblaettle.de/frontend/mvc/issueFeed/groupsAndIssues?&position=0&group=1289&allMode=false&mode=public"
for issue_num in range(1289, 1427):
    url = urlparse(base_url)
    issue = url.query.split('=')[2].split('&')[0]
    parts = url.query
    parts = parts.replace(issue, str(issue_num))
    url = url._replace(query=parts)
    url = url.geturl()
    print (url)



url = 'https://www.myeblaettle.de/?group=1289'
parts = urlparse(url)

print (parts.query)
print (parts.query.split('='))
issu= parts.query.split('=')[1]
print (parts.query.split('=')[1])

print (parts._replace(issu, "1281")
    # print (url, query)



    # print (query)
