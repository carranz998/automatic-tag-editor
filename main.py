import os
import sys

from album import Album


def _main():
    root_path = sys.argv[1]
    for subdir, dirs, files in os.walk(root_path):
        if not dirs:
            a = Album(subdir)


if __name__ == '__main__':
    _main()