from album_data_scraper import AlbumDataScraper
from album_directory import AlbumDirectory
from metadata_editor import MetadataEditor


class Album:
    def __init__(self, path):
        _, self.artist, self.title = path.split('\\')

        directory = AlbumDirectory(path)
        scraper = AlbumDataScraper(self.artist, self.title)

        directory.normalize_file_structure()
        directory.write(scraper.cover, 'cover.png')

        print(scraper.tracks_name)

        with open(directory.cover, 'rb') as cover:
            cover_content = cover.read()

        for path, name in zip(directory.tracks_path, scraper.tracks_name):
            metadata_editor = MetadataEditor(path)
            tags = {
                'TALB': self.title,
                'TPE2': self.artist,
                'APIC': [directory.cover, open(directory.cover, 'rb').read()]
            }
            metadata_editor.tag(tags)
