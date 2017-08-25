import os
import unittest
from src.FileTypes.ImageFile import ImageFile


class ImageFileTests(unittest.TestCase):
    def setUp(self):
        self.image_file = ImageFile(os.path.abspath("Untitled.png"))

    def test_image_width(self):
        self.assertEqual(self.image_file.get_width(), 512)

    def test_image_height(self):
        self.assertEqual(self.image_file.get_height(), 512)

    def test_color_list(self):
        self.assertEqual(self.image_file.get_color_list(),
                         [(104755, (255, 255, 255)), (36488, (0, 30, 255)), (27528, (0, 0, 0)), (20464, (255, 0, 0)),
                          (18328, (0, 255, 6)), (18283, (255, 222, 0)), (15042, (0, 255, 222)), (10336, (255, 144, 0)),
                          (5681, (255, 0, 204)), (5239, (0, 255, 132))])

    def test_most_commonly_color(self):
        self.assertEqual(self.image_file.get_most_commonly_color(), [(255, 255, 255)])

    def test_repeatable_files(self):
        self.assertEqual(self.image_file.get_repeatable_files(os.path.abspath("../../tests")),
                         ["/home/kate/Documents/FileMetadata/tests/FileTypesTest/Untitled.png"])

    def test_description(self):
        self.assertEqual(self.image_file.get_description(), {})

    def test_comment(self):
        self.assertEqual(self.image_file.get_comment(), {'Comment': 'Created with GIMP'})

if __name__ == "__main__":
    unittest.main()
