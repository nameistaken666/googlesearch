import requests
import urllib
from reqeusts_html import HTMLSession

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    
    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 'https://google.',
    'https://webcache.googleusercontent.',
    'http://webcache.googleusercontent.',
    'https://policies.google.',
    'https://support.google.',
    'https://maps.google.')
    
    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)
            
    return links
    
print(scrape_google("health"))
