from os import walk


def process_files_in_folder(path, filenames):

    for fn in filenames: 
        file_name = str(fn)
        if (file_name.endswith('opf')):
            #f = open(path + "\\" + fn, "r")
            #print(f.read())
            print(path + "\\" + fn)


def dicover_folders_in_folder(folder_path):
    for (dirpath, dirnames, filenames) in walk(folder_path):
        # print(folder_path) 
        process_files_in_folder(path=folder_path, filenames=filenames)
        for dir in dirnames: 
            print(folder_path + "\\" + dir) 
            dicover_folders_in_folder(folder_path + dir)
        break    
    
# path = "D:\\personal\\books\\Calibre Library\\A. Roth, Ariel\\La ciencia descubre a dios (23924)\\"
path = "D:\\personal\\books\\Calibre Library\\Aames, Lani"

dicover_folders_in_folder(path)

