from file_handling import delete_files, write_file
from web_scraping import get_album_page_address, get_artwork_address, get_search_page_address, get_album_tracks, \
    get_file_content


class Album:
    def __init__(self, path):
        _, self.artist, self.title = path.split('\\')

        delete_files(['.flac', '.mp3'], path)
        search_page_link = get_search_page_address(self.artist, self.title)
        link = get_album_page_address(search_page_link)
        artwork_address = get_artwork_address(link)

        self.tracks = get_album_tracks(link)
        self.artwork = get_file_content(artwork_address)

        write_file(self.artwork, path)

        print(link, self.tracks)

        self.resources = {'search': search_page_link, 'album': link, 'artwork': artwork_address}
