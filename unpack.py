import zipfile
import os

FILES_PATH = 'files/full'

for file in os.listdir(os.path.abspath(FILES_PATH)):
    abs_file = os.path.abspath(FILES_PATH+'/'+file)
    if zipfile.is_zipfile(abs_file):
        print("{} is a valid zipfile. Unpack!".format(abs_file))
        with zipfile.ZipFile(os.path.abspath(abs_file), 'r') as zip_ref:
            zip_ref.extractall('./extracted')

