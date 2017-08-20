import logging
import win32api
import win32con
import win32security


def file_author(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: tuple - owner name with user id
    """
    try:
        sd = win32security.GetFileSecurity(file_info.file_path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        owner_name = win32api.GetUserName()
        owner_id = win32security.LookupAccountSid(None, owner_sid)[2]
        return owner_name, owner_id
    except AttributeError as err:
        logging.error(err)
