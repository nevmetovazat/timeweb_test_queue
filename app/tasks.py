from flask import current_app
import requests

def scrape(url):
    r = requests.get(url)
    r.raise_for_status()
    return {'headers': r.headers, 'content': r.text}
