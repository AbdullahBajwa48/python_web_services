# rllib.request → Fetches the webpage.
# urllib.parse → Helps with URL handling (not used here).
# urllib.error → Handles errors (like 404 Not Found).
# BeautifulSoup → Parse and extracts data from HTML.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Asfhan.html'
html = urllib.request.urlopen(url).read()


for x in range(7):

    # Opens the current url and reads the HTML.
    # Parses it using BeautifulSoup.
    # Finds all <a> (anchor) tags (which contain links).
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    
    lst = []
    tags = soup('a')

    for tag in tags:
        #Extracts each hyperlink (href) from the <a> tags.
        url = (tag.get('href',None))
        if len(lst)<18:
            lst.append(url)
        else:
            break
    url = (lst[17])
print(url)

