import os
import sys
import time
from unittest import TestLoader, TextTestRunner, TestSuite
"""
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
"""
from src.FileTypes.BaseFile import BaseFile
from src.FileTypes.ImageFile import ImageFile
from tests.FileTypesTest.BaseFileTest import BaseFileTest
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../"))


if __name__ == "__main__":
    """loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(BaseFileTest),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
    """
    """
    file = BaseFile("/home/kate/Documents/FileMetadata/tests/__init__.py")
    print(file.get_type())
    print(file.get_permission())
    print(file.get_creation_date())
    print(file.get_modification_date())
    print(file.get_size())
    print(file.get_owner())
    print(file.get_name())
    """
    i = ImageFile('/home/kate/Pictures/Untitled.png')
    print(i.get_width())
    print(i.get_height())
    print(i.get_permission())
    print(i.get_most_commonly_color())
    print(i.get_description())
    print(i.get_comment())
    print(i.get_color_list())
    print(i.get_repeatable_files("/home/kate/Pictures/"))

    i1 = ImageFile('/home/kate/Pictures/1(1).jpg')
    c = i1.get_color_list()
    print(c[:100])

