import os
from src.FileTypes.BaseFile import BaseFile
from src.FileTypes.ImageFile import ImageFile


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
    i = ImageFile(os.path.abspath("/home/kate/Documents/FileMetadata/tests/FileTypesTest/Untitled.png"))
    print(i.get_width())
    print(i.get_height())
    print(i.get_permission())
    print(i.get_most_commonly_color())
    print(i.get_description())
    print(i.get_comment())
    print(i.get_color_list())

