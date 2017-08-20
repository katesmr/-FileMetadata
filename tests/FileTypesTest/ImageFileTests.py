import unittest
from src.FileTypes.ImageFile import ImageFile


class ImageFileTests(unittest.TestCase):
    def setUp(self):
        self.image_file = ImageFile("/home/kate/Pictures/Untitled.png")

    def test_image_width(self):
        self.assertEqual(self.image_file.get_width(), 255)

    def test_image_height(self):
        self.assertEqual(self.image_file.get_height(), 255)

    def test_color_list(self):
        self.assertEqual(self.image_file.get_color_list(),
                         [(39747, (255, 255, 255)), (16983, (255, 0, 252)),
                          (4500, (0, 78, 255)), (3795, (0, 255, 222))])

    def test_most_commonly_color(self):
        self.assertEqual(self.image_file.get_most_commonly_color(), [(255, 255, 255)])

    def test_repeatable_files(self):
        self.assertEqual(self.image_file.get_repeatable_files("/home/kate/Pictures/"),
                         ['/home/kate/Pictures/Untitled.png', '/home/kate/Pictures/Untitled.jpg'])

    def test_description(self):
        self.assertEqual(self.image_file.get_description(), {})

    def test_comment(self):
        self.assertEqual(self.image_file.get_comment(), {'Comment': 'Created with GIMP'})

if __name__ == "__main__":
    unittest.main()
