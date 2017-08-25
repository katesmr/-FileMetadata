import os
import math
import operator
import functools
from PIL import Image


def is_equal_image(image1, image2):
    """
    :param image1: Image
    :param image2: Image
    :return: boolean - is equal image
    """
    assert image1 is not None
    assert image2 is not None
    h1 = image1.histogram()
    h2 = image2.histogram()
    # calculate the root-mean-square
    rms = math.sqrt(functools.reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms == 0


def find_repeatable_images(path, image):
    """
    :param path: str - path to folder for search
    :param image: Image
    :return: list - list of paths of equal images
    """
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            child = os.path.join(root, file)
            try:
                # get any image type
                comparison_image = Image.open(child)
            except IOError:
                continue
            if is_equal_image(image, comparison_image):
                result.append(child)
    return result

"""
def find_repeatable_images(path, image):
    def scan_dir(parent, image_obj):
        for token in os.listdir(parent):
            child = os.path.join(parent, token)
            if os.path.isdir(child):
                scan_dir(child, image_obj)
            try:
                # get any image type
                comparison_image = Image.open(child)
            except IOError:
                continue
            if is_equal_image(image_obj, comparison_image):
                res.append(child)
    assert isinstance(path, str)
    assert image is not None
    res = []
    scan_dir(path, image)
    return res
"""
