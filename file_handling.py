import os


def write_file(content, filepath, filename='artwork.png'):
    target_path = filepath + '\\' + filename
    with open(target_path, 'wb') as f:
        f.write(content)


def delete_files(excluded_extensions, source_path):
    """
    Removes from a specified path all files whose extension is not included in a list.
    :param source_path:
    :param excluded_extensions:
    """
    path_content = os.listdir(source_path)
    for file in path_content:
        _, extension = os.path.splitext(file)
        if extension not in excluded_extensions:
            file = source_path + '\\' + file
            os.remove(file)
