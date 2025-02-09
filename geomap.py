# urllib.request → Sends HTTP requests to get data from the web.
# urllib.parse → Encodes URL parameters.
# urllib.error → Handles potential errors (e.g., network issues).
# json → Parses JSON responses.
# ssl → Handles secure HTTPS connections (avoiding certificate issues).
import  urllib.error, urllib.request, urllib.parse
import json, ssl


serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Disables SSL certificate verification to avoid HTTPS errors.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('enter address.....')
    address = address.strip()
    parms = {}

#     Creates a dictionary parms and adds the user-inputted address as the query parameter (q).
#     This is necessary for sending parameters in the URL.
    parms['q']= address
    print(parms)

    # converts the dictionary into a URL-encoded string
    url = serviceurl + urllib.parse.urlencode(parms)
    raw = urllib.request.urlopen(url, context=ctx)

    data = raw.read().decode()

    # converts the string into a Python dictionary
    js = json.loads(data)

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat',lat,'lon',lon)
    location = js['features'][0]['properties']['formatted']
    print(location)


# Understand the Process 🧠

# "Input → Encode URL → Send Request → Get JSON → Extract Data → Print"