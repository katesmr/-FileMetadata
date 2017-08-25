import os
import unittest
from src.FileTypes.BaseFile import BaseFile


class BaseFileTest(unittest.TestCase):
    def setUp(self):
        self.file1 = BaseFile(os.path.abspath("__init__.py"))
        self.file2 = BaseFile(os.path.abspath("test.txt"))

    def test_file_size(self):
        self.assertEqual(self.file1.get_size(), 0)
        self.assertEqual(self.file2.get_size(), 27)

    def test_file_name(self):
        self.assertEqual(self.file1.get_name(), "__init__.py")
        self.assertEqual(self.file2.get_name(), "test.txt")

    def test_file_type(self):
        self.assertEqual(self.file1.get_type(), "inode/x-empty")
        self.assertEqual(self.file2.get_type(), "text/plain")

    def test_file_creation_date(self):
        self.assertEqual(self.file1.get_creation_date(), "Thu Aug 17 12:58:03 2017")
        self.assertEqual(self.file2.get_creation_date(), "Fri Aug 25 17:17:04 2017")

    def test_file_modification_date(self):
        self.assertEqual(self.file1.get_modification_date(), "Thu Aug 17 12:58:03 2017")
        self.assertEqual(self.file2.get_modification_date(), "Fri Aug 25 17:17:04 2017")

    def test_file_owner(self):
        pass

    def test_file_permission(self):
        self.assertEqual(self.file1.get_permission(),
                         {'other': ['read'], 'group': ['read', 'write'], 'user': ['read', 'write']})
        self.assertEqual(self.file2.get_permission(),
                         {'other': ['read'], 'group': ['read', 'write'], 'user': ['read', 'write']})


if __name__ == "__main__":
    unittest.main()
