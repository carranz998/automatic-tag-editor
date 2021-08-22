from album_directory import AlbumDirectory
from album_data_scraper import AlbumDataScraper


class Album:
    def __init__(self, path):
        _, self.artist, self.title = path.split('\\')

        directory = AlbumDirectory(path)
        scraper = AlbumDataScraper(self.artist, self.title)

        self.tracks = scraper.tracks

        directory.delete_files(['.flac', '.mp3'])
        directory.write(scraper.cover, 'cover.png')

        print(self.tracks)
