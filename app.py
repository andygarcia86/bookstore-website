# Python standard libraries
from os import walk
import logging

# Third-party libraries
import xml.etree.ElementTree as ET

# Internal imports
from database import BookDao, AuthorDao, SubjectDao, BooksSubjectDao


def parse_fields_in_opf_file(xmlFileName):
    """This function iterates over the list of files inside the folder finding the .opf files

        Args:
        xmlFileName (str): File name of the opf file, that is an XML file
    """
    try:
        root = ET.parse(xmlFileName).getroot()

        metadata = root.findall("{http://www.idpf.org/2007/opf}metadata")[0]
        title = metadata.findall("{http://purl.org/dc/elements/1.1/}title")[0].text
        creator = metadata.findall("{http://purl.org/dc/elements/1.1/}creator")[0].text
        description = metadata.findall("{http://purl.org/dc/elements/1.1/}description")[
            0
        ].text
        language = metadata.findall("{http://purl.org/dc/elements/1.1/}language")[
            0
        ].text

        author = AuthorDao().get(creator)
        author_id = AuthorDao().put(creator) if author is None else author.id

        book = BookDao().get(title)
        book_id = BookDao().put(author_id, title, description, language) if book is None else book.id

        for item in metadata.findall("{http://purl.org/dc/elements/1.1/}subject"):
            # subjects.append(item.text)

            subject = SubjectDao().get(item.text)
            subject_id = SubjectDao().put(item.text) if subject is None else subject.id

            book_subject = BooksSubjectDao().get(book_id, subject_id)
            if book_subject is None:
                BooksSubjectDao().put(book_id, subject_id)
            

    except Exception as e:
        # TODO: Create a log for each filed file
        # print("An exception occurred with OPF: ", xmlFileName)
        logging.error("Error at %s", exc_info=e)


def process_files_in_folder(path, filenames):
    """This function iterates over the list of files inside the folder finding the .opf files

        Args:
        path (str): Path that contains the list of files
        filenames (array): Array of filenames inside the path
    """
    for fn in filenames:
        file_name = str(fn)
        if file_name.endswith(".opf"):
            parse_fields_in_opf_file(path + "\\" + fn)


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


# TODO: Move this to config file or parameter
path = "D:\\personal\\books\\Calibre Library\\Aames, Lani"
discover_folders_in_folder(path)
