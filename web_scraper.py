import urllib.request
from bs4 import BeautifulSoup
from print_to_pdf import print_to_pdf

url = "https://golangcode.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

for page in range(1, 12):
    request = urllib.request.Request(url+'page/%s' % page, None, headers)
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html.read(), "lxml")
    for item in soup.findAll('a', {'class': 'post-title'}):
        print_to_pdf(item['href'])
