import os
import shutil
from_dir="C:/Users/user/Downloads"
to_dir="C:/Users/user/Documents/Document files"
list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    root, extension= os.path.splitext(file_name)
    print("extension of the file is", extension)

