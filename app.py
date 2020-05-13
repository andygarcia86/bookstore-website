from os import walk
import logging
import xml.etree.ElementTree as ET
from database import BookDao, AuthorDao

def parse_fields_in_opf_file(xmlFileName):
    try:
        root = ET.parse(xmlFileName).getroot()

        metadata = root.findall('{http://www.idpf.org/2007/opf}metadata')[0]
        title = metadata.findall('{http://purl.org/dc/elements/1.1/}title')[0].text
        creator = metadata.findall('{http://purl.org/dc/elements/1.1/}creator')[0].text
        description = metadata.findall('{http://purl.org/dc/elements/1.1/}description')[0].text
        language = metadata.findall('{http://purl.org/dc/elements/1.1/}language')[0].text
        subjects = []
        for subject in metadata.findall('{http://purl.org/dc/elements/1.1/}subject'):
            subjects.append(subject.text)

        """
        print (subjects)
        """

        author = AuthorDao().get(creator)
        author_id = AuthorDao().put(creator) if author is None else author.id

        BookDao().put(author_id, title, description, language)

    except Exception as e:
        # TODO: Create a log for each filed file
        # print("An exception occurred with OPF: ", xmlFileName)
        logging.error('Error at %s', exc_info=e)


def process_files_in_folder(path, filenames):
    for fn in filenames:
        file_name = str(fn)
        if (file_name.endswith('.opf')):
            parse_fields_in_opf_file(path + "\\" + fn)


def discover_folders_in_folder(folder_path):
    for (dirpath, dirnames, filenames) in walk(folder_path):
        process_files_in_folder(path=folder_path, filenames=filenames)
        for dir in dirnames:
            discover_folders_in_folder(folder_path + "\\" + dir)
        break

# TODO: Move this to config file
path = "D:\\Andy\\books\\! Library\\Aames, Lani"
discover_folders_in_folder(path)


