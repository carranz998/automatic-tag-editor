from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


def get_file_content(web_address):
    response = requests.get(web_address)
    return response.content


def get_album_tracks(album_data_address):
    response = requests.get(album_data_address)
    soup = BeautifulSoup(response.text, "html.parser")

    tracks = [track.text for track in soup.find_all('span', class_='tracklist_track_title')]
    return tracks


def get_artwork_address(album_data_address):
    response = requests.get(album_data_address)
    soup = BeautifulSoup(response.text, "html.parser")

    for image in soup.find_all('img'):
        if 'album cover' in image['alt']:
            return image['src']
    return None


def get_search_page_address(artist, album):
    text_queried = '%s %s' % (artist, album)
    quoted = quote(text_queried)

    request = 'https://www.discogs.com/search/?q=%s&type=master' % quoted
    return request


def get_album_page_address(search_page_address):
    response = requests.get(search_page_address)
    soup = BeautifulSoup(response.text, "html.parser")

    href = soup.find_all(class_='thumbnail_link', href=True)[0]['href']
    address = 'https://www.discogs.com/%s' % href

    return address
