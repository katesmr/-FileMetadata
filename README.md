# FileMetadata

Provide file data.

# Usage 

```
from src.FileTypes.BaseFile import BaseFile
from src.FileTypes.ImageFile import ImageFile


if __name__ == "__main__":
```
Create BaseFile object
```
    file = BaseFile("PATH_TO_YOUR_FILE")
    print(file.get_type())
    print(file.get_permission())
    print(file.get_creation_date())
    print(file.get_modification_date())
    print(file.get_size())
    print(file.get_owner())
    print(file.get_name())
```
Create ImageFile object
```
    image = ImageFile("PATH_TO_YOUR_IMAGE")
    print(image.get_permission())
    print(image.get_most_commonly_color())
    print(image.get_description())
    print(image.get_comment())
    print(image.get_color_list())
    print(image.get_repeatable_files("PATH_TO_FOLDER_FOR_SEARCH"))
```

# Dependencies
1) Install PIL library
```
python3 -m pip install Pillow
```
2) Install magic libray
For Unix:
```
python3 -m pip install python-magic
```
For Windows:
```
...
```

