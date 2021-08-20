import requests
from bs4 import BeautifulSoup


class AlbumDataScraper:
    def __init__(self, album):
        self.soup = None
        self.parsers = album.resources


    def get_file_content(self, resource):
        response = requests.get(resource)
        return response.content
