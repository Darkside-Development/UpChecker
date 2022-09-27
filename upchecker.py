import requests as r


req = r.get('https://memeify.pythonanywhere.com')


if req.status_code == 200:
    print('Success! (Status Code 200)')

if req.status_code == 403:
    print('Forbidden. (Status Code 403)')

if req.status_code == 301:
    print('Moved Permanently. (Status Code 301)')

if req.status_code == 302:
    print('Temporary Redirect. (Status Code 302)')

if req.status_code == 410:
    print('Gone. (Status Code 410)')
    
if req.status_code == 429:
    print('Too Many Requests. (Status Code 429)')
    
if req.status_code == 400:
    print('Bad Request. (Status Code 400)')

if req.status_code == 401:
    print('Unauthorized. (Status Code 401)')
    
if req.status_code == 500:
    print('Internal Server Error. (Status Code 500')
    
if req.status_code == 503:
    print('Service Unavailable. (Status Code 503)')

elif req.status_code == 404:
    print('Website not found. (Status Code 404)')
    
