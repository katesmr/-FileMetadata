def image_comment(image):
    """
    :param image: Image
    :return: str - comment text
    """
    assert image is not None
    result = {}
    if "Comment" in image.info:
        result["Comment"] = image.info["Comment"]
    return result
