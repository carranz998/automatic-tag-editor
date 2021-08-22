from album_directory import AlbumDirectory
from album_data_scraper import AlbumDataScraper


class Album:
    def __init__(self, path):
        _, self.artist, self.title = path.split('\\')

        directory = AlbumDirectory(path)
        scraper = AlbumDataScraper(self.artist, self.title)

        directory.flat()
        directory.delete_all_subdirectories()
        directory.delete_non_audio_files()
        directory.write(scraper.cover, 'cover.png')

        print(scraper.tracks)
