from bs4 import BeautifulSoup
from urllib import request as urlreq
from urllib import error as urlerr

baseURL = "https://harvardlawreview.org/category/articles/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Open File
f = open('strdump.txt', 'w')

def findAbstract(url):
    # Create Request
    req = urlreq.Request(url, headers=hdr)
    page = urlreq.urlopen(req)

    soup = BeautifulSoup(page, "html.parser")

    strings = soup.find(class_="article-txt").strings
    # strings = text.find_all(string=True)

    for string in strings:
        f.write(repr(string))


req = urlreq.Request(baseURL, headers=hdr)

try:
    page = urlreq.urlopen(req)
except urlerr.HTTPError as e:
    print(e.fp.read())

soup = BeautifulSoup(page, "html.parser")

articles = soup.find_all("h2", "tz-h")

articleUrls = []
for article in articles:
    # print(article.a)
    articleUrls.append(article.a['href'])

# print(articleUrls[0])
findAbstract(articleUrls[0])
# for url in articleUrls:
#     findAbstract(url)

# Close File
f.close()