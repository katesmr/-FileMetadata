import logging
from src.core.FileInfo import FileInfo
from src.utils.utils import permission
from src.utils.utils import split_on_bit


def file_permission_number(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: str - permission number in octal numeral system
    """
    assert isinstance(file_info, FileInfo)
    try:
        return oct(file_info.stat.st_mode)[-3:]
    except AttributeError as err:
        logging.error(err)


def file_permission(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: dict - dictionary key is mode, value is permissions of file
    """
    assert isinstance(file_info, FileInfo)
    permission_number = file_permission_number(file_info)
    split_permission = split_on_bit(permission_number, 3)
    result = permission(split_permission)
    return result
