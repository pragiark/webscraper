import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse


url = 'https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits'
r = requests.get(url, headers={'user-agent': 'kamil.kwapisz.pl'})
soup = BeautifulSoup(r.text, "lxml")

body = soup.body
div = body.find('div', {'class': 'md wiki'})
div.table.extract()
ul = div.ul.extract()
links = div('a', {'rel': 'nofollow'})
for link in links[:10]:
    print(link.get('href'))

for relative_link in links[:7]:
    absolute_link = urljoin(url, relative_link.get('href'))
    print(absolute_link)

print(type(div.find('table')))

netloc = urlparse(url).netloc
protocol = urlparse(url).scheme
print(protocol)
print(netloc)

for link in links:
    href: str = link.get('href')
    if href.startswith("/r"):
        print(urljoin(url, href))

def get_absolute_link(relative_link: str) -> str:
    protocol = urlparse(url).scheme  # url jest zmienną globalną
    netloc = urlparse(url).netloc
    absolute_link: str = protocol + "://" + netloc + relative_link
    return absolute_link