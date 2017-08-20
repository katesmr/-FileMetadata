import logging
from src.core.FileInfo import FileInfo
from src.core.base.compute_file_size import compute_file_size


def file_size(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: int - count of bytes of file
    """
    assert isinstance(file_info, FileInfo)
    try:
        size = file_info.stat.st_size
        if size == 0:
            size = compute_file_size(file_info.file)
        return size
    except AttributeError as err:
        logging.error(err)
