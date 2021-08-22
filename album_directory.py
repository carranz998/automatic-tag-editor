import os


class AlbumDirectory:
    """
    Functionalities of the physical directory in which the songs of an album are stored.
    """
    def __init__(self, path):
        self.path = path

    def write(self, data, filename):
        """
        Writes data in a file.
        :param data: Data to be written.
        :param filename: File where the data will be written.
        """
        target_path = '%s\\%s' % (self.path, filename)
        with open(target_path, 'wb') as f:
            f.write(data)

    def delete_files(self, excluded_extensions):
        """
        Removes from a specified path all files whose extension is not included in a list.
        :param excluded_extensions:
        """
        path_content = os.listdir(self.path)
        for file in path_content:
            _, extension = os.path.splitext(file)
            if extension not in excluded_extensions:
                file = self.path + '\\' + file
                os.remove(file)

