# urllib.request → Fetches the webpage.
# urllib.parse → Helps with URL encoding/decoding (not used here).
# urllib.error → Handles errors (e.g., 404 Not Found).
# BeautifulSoup → Parses and extracts data from HTML/XML documents.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#These 4 lines of code is used if the url is https not http
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('enter url...')
html = urllib.request.urlopen(url, context=ctx).read()

# BeautifulSoup(html, 'html.parser') → Converts the HTML into a structured parse tree for easy extraction.
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')

# .get_text() → Extracts and prints only the visible text, removing any HTML tags.
for tag in tags: 
    print(tag.get_text())