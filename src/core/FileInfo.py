import os
import logging


class FileInfo:
    def __init__(self, file_path):
        """
        :param file_path: str - full path to file
        """
        assert isinstance(file_path, str)
        self.file_path = file_path
        try:
            self.stat = os.stat(self.file_path)
            self.file = open(file_path, "rb")
        except (IOError, OSError) as err:
            logging.error(err)

    def __del__(self):
        try:
            self.file.close()
        except AttributeError as err:
            logging.error(err)
