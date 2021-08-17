import requests
from bs4 import BeautifulSoup


def get_media_url(artist_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; '
                      'WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    }
    url = 'https://www.allmusic.com/search/artist/' + artist_name
    response = requests.request('GET', url, headers=headers, data={})
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    if len(images) < 1:
        return None
    return images[0]['src']
