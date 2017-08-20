def image_description(image):
    """
    :param image: Image
    :return: str - description text
    """
    assert image is not None
    result = {}
    if "description" in image.info:
        result["description"] = image.info["description"]
    return result
