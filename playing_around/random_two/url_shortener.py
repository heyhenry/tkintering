# source: https://www.tutorialspoint.com/python-url-shortener-using-tinyurl-api

import requests

def shorten(url):
    base_url = 'http://tinyurl.com/api-create.php?url='
    response = requests.get(base_url+url)
    short_url = response.text
    return short_url

long_url = 'https://www.youtube.com/watch?v=t8OZPJfpcTM'
short_url = shorten(long_url)
print(short_url)