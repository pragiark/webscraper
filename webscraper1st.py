import requests
from bs4 import BeautifulSoup

# connetct with webstie
url = 'https://'
url = url.rstrip("//")
r = requests.get(url)
# parse html
soup = BeautifulSoup(r.text, 'lxml')
links = soup.find_all('a')
wwwlist = {}
if url.startswith("http") and url not in wwwlist:
    wwwlist[url] = []
for link in links:
    link = str(link.get('href')).rstrip("//")
    if link not in wwwlist[url] and link.startswith("http"):
        wwwlist[url].append(link)

# itteration list in dictionary
for listlink in wwwlist[url]:
    if listlink not in wwwlist.keys() and listlink.startswith("https://"):
        wwwlist[listlink] = []
        r = requests.get(listlink)
        soup = BeautifulSoup(r.text, 'lxml')
        souplist = soup.find_all('a')
        for link in souplist:
            link = str(link.get('href')).rstrip("//")
            if link.startswith("http") and link not in wwwlist[listlink]:
                wwwlist[listlink].append(link)

# write list in vertical if want only external links
# for k ,v in wwwlist.items():
#     print("Na postronie: " + str(k) + " sa linki:")
#     for linkasy in v:
#         if not linkasy.startswith("https://furia.org.pl"):
#             print(linkasy)

# write list in vertical
for k, v in wwwlist.items():
    print("Na postronie: " + str(k) + " sa linki:")
    for linkasy in v:
        print(linkasy)
