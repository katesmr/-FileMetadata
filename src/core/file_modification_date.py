import time
import logging
from src.core.FileInfo import FileInfo


def file_modification_date(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: str - creation data
    """
    assert isinstance(file_info, FileInfo)
    try:
        return time.asctime(time.localtime(file_info.stat.st_mtime))
    except AttributeError as err:
        logging.error(err)
