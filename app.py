from os import walk
import xml.etree.ElementTree as ET

def process_xml_content(xmlFileName):
    try:
        root = ET.parse(xmlFileName).getroot()
        for country in root.findall('{http://www.idpf.org/2007/opf}metadata'):
            for title in country.findall('{http://purl.org/dc/elements/1.1/}title'):
                print (title.text)
    except:
        # TODO: Create a log for each filed file
        print("An exception occurred with OPF: ", xmlFileName)
        

def process_files_in_folder(path, filenames):
    for fn in filenames: 
        file_name = str(fn)
        if (file_name.endswith('.opf')):
            process_xml_content(path + "\\" + fn)

            # f = open(path + "\\" + fn, "r")
            # print(f.read())


def dicover_folders_in_folder(folder_path):
    for (dirpath, dirnames, filenames) in walk(folder_path):
        # print(folder_path) 
        process_files_in_folder(path=folder_path, filenames=filenames)
        for dir in dirnames: 
            # print(folder_path + "\\" + dir) 
            dicover_folders_in_folder(folder_path + "\\" + dir)
        break    
    
# path = "D:\\personal\\books\\Calibre Library\\A. Roth, Ariel\\La ciencia descubre a dios (23924)\\"
path = "D:\\personal\\books\\Calibre Library"

dicover_folders_in_folder(path)

