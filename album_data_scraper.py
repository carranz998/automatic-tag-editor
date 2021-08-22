from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


class AlbumDataScraper:
    """
    Scraper of information from the information web page of an album.
    """
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.soup = BeautifulSoup(
            requests.get(self.__album_data_page).text, 'html.parser'
        )

    @property
    def __album_data_page(self):
        """
        Gets the web address of the album information page.
        :return: Web address of the album information page.
        """
        request = 'https://www.discogs.com/search/?q=%s&type=master' % self.__quote_artist_title()
        response = requests.get(request)
        soup = BeautifulSoup(response.text, "html.parser")

        href = soup.find_all(class_='thumbnail_link', href=True)[0]['href']
        address = 'https://www.discogs.com/%s' % href

        return address

    def __quote_artist_title(self):
        return quote('%s %s' % (self.artist, self.title))

    @property
    def cover(self):
        """
        Extracts the byte representation of the album cover.
        :return: Byte representation of the album cover.
        """
        for image in self.soup.find_all('img'):
            if 'album cover' in image['alt']:
                cover_address = image['src']
                return requests.get(cover_address).content
        return None

    @property
    def tracks(self):
        """
        Extracts the names of the album tracks.
        :return: List with the names of the tracks.
        """
        return [track.text for track in self.soup.find_all('span', class_='tracklist_track_title')]
