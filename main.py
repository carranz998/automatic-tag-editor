import os
import sys

from album import Album


def album_folders(root_path):
    folders = []

    for artist in os.listdir(root_path):
        artist_folder_path = os.path.join(root_path, artist)

        for album in os.listdir(artist_folder_path):
            album_folder_path = os.path.join(artist_folder_path, album)
            folders.append(album_folder_path)

    return folders


def __main():
    root_path = sys.argv[1]
    for folder in album_folders(root_path):
        album = Album(folder)


if __name__ == '__main__':
    __main()
