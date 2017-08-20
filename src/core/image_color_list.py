import threading
from src.core.base.sorted_by_decrease import sorted_by_decrease


def image_color_list(image, width, height, create_new_thread=False):
    """
    :param image: Image
    :param width: int
    :param height: int
    :param create_new_thread: boolean - create new thread for sorting color list
    :return: list - list of tuples, where first value is color count, second value - tuple - color rgb value
    """
    assert image is not None
    assert isinstance(width, int)
    assert isinstance(height, int)
    colors = image.getcolors(width * height)
    if create_new_thread:
        thread = threading.Thread(target=sorted_by_decrease, args=(colors,))
        thread.daemon = True
        thread.start()
    else:
        sorted_by_decrease(colors)
    return colors
