import threading
from src.core.base.sorted_by_decrease import sorted_by_decrease


def image_color_list(image, width, height):
    """
    :param image: Image
    :param width: int
    :param height: int
    :return: list - list of tuples, where first value is color count, second value - tuple - color rgb value
    """
    assert image is not None
    assert isinstance(width, int)
    assert isinstance(height, int)
    colors = image.getcolors(width * height)
    sorted_by_decrease(colors)
    return colors
