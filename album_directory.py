import os
import shutil


class AlbumDirectory:
    """
    Represents the physical directory where the album is stored and provides basic file management functions within it.
    """
    def __init__(self, path):
        self.root_path = path
        self.audio_extensions = ['.flac', '.mp3']

    def delete_all_subdirectories(self):
        for path, _, _ in os.walk(self.root_path):
            if path != self.root_path:
                shutil.rmtree(path)

    def delete_non_audio_files(self):
        """
        Removes from the root path all files whose extension is not included in a list.
        """
        for file in os.listdir(self.root_path):
            _, extension = os.path.splitext(file)
            if extension not in self.audio_extensions:
                file = self.root_path + '\\' + file
                os.remove(file)

    def flat(self):
        """
        Converts a multidimensional list of archives in a unidimensional list of archives.
        """
        for path, _, files in os.walk(self.root_path):
            for file in files:
                _, extension = os.path.splitext(file)
                if extension in self.audio_extensions:
                    self.move_file(
                        source_path=os.path.join(path, file),
                        target_path=os.path.join(self.root_path, file)
                    )

    @staticmethod
    def move_file(source_path, target_path):
        shutil.move(source_path, target_path)

    def write(self, data, target_file):
        target_file = os.path.join(self.root_path, target_file)
        with open(target_file, 'wb') as f:
            f.write(data)