import requests
from bs4 import BeautifulSoup

# connetct with webstie
url = 'https://furia.org.pl/'
r = requests.get(url)
print("Teraz sprawdzam: " + str(url) + " i są tu linki:")
# parse html
soup = BeautifulSoup(r.text, 'lxml')
links = soup.find_all('a')
wwwlist = []
for link in links:
    if link.get('href') not in wwwlist and str(link.get('href')).startswith("http"):
        wwwlist.append(link.get('href'))
        #print(link.get('href'))
        if str(link.get('href')).startswith("http"):
            wwwlist.append(link.get('href'))
            print(link.get('href'))

# write list in vertical
# for i in wwwlist:
#      print(i)

#read links
for rlink in wwwlist:
    print(str(rlink) + " posiada linki: ")
    if str(rlink).startswith("https://furia.org.pl/"):
        url = rlink
        r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a')
    for link in links:
        if link.get('href') not in wwwlist and str(link.get('href')).startswith("http"):
            wwwlist.append(link.get('href'))
            print(link.get('href'))

# write list in vertical
# for i in wwwlist:
#     print(i)
