from os.path import exists
from os.path import basename


def file_name(file_path):
    """
    :return: str - file name
    """
    assert isinstance(file_path, str)
    if exists(file_path):
        return basename(file_path)
