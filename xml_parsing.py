# urllib.request → Handles opening URLs and fetching data from the internet.
# urllib.error → Handles errors like "Page Not Found" or "Server Not Available."
# urllib.parse → Helps with manipulating URLs (not used in this code).
# xml.etree.ElementTree (ET) → A module for parsing XML data.
import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET

xml = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2147516.xml')
data = xml.read()
print(type(data))


# ET.fromstring(data) → Converts the binary XML data into a tree structure that Python can navigate.
tree = ET.fromstring(data)


# Finds all <count> elements in the XML, no matter where they are.
values = tree.findall('.//count')
lst = []

for value in values:
    
    lst.append(int(value.text))
print(sum(lst))