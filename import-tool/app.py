# Python standard libraries
from os import walk
import logging

# Internal imports
from utils import XML_helper

def process_files_in_folder(path, filenames):
    """This function iterates over the list of files inside the folder finding the .opf files

        Args:
        path (str): Path that contains the list of files
        filenames (array): Array of filenames inside the path
    """

    logging.info("Procesing folder: " + path)

    for fn in filenames:
        file_name = str(fn)
        if file_name.endswith(".opf"):
            XML_helper().parse_fields_in_opf_file(path + "\\" + fn)


def discover_folders_in_folder(folder_path):
    """This function iterates over an specific folder and search for all subfolders

        Args:
        folder_path (str): Initial path for start search
    """
    for (dirpath, dirnames, filenames) in walk(folder_path):
        process_files_in_folder(path=folder_path, filenames=filenames)
        for dir in dirnames:
            discover_folders_in_folder(folder_path + "\\" + dir)
        break

def setup_login_config():
    logging.basicConfig(filename="logs/log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def main():
    # TODO: Move this to config file or parameter
    path = "D:\\personal\\books\\Calibre Library"
    discover_folders_in_folder(path)

if __name__ == "__main__":
    main()
