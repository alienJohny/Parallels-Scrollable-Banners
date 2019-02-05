import requests
with open('./img.png', 'wb') as f:
    f.write(requests.get('http://0.0.0.0:9000/ship10.png').content)