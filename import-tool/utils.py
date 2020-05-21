# Python standard libraries
import logging

# Third-party libraries
import xml.etree.ElementTree as ET

# Internal imports
from database import BookDao, AuthorDao, SubjectDao, BooksSubjectDao


class XML_helper:

    def parse_fields_in_opf_file(self, xmlFileName):
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
            # print("An exception occurred with OPF: ", xmlFileName)
            logging.error("Error at %s", exc_info=e)