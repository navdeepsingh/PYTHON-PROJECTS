import os

def rename_files():
    #(1) get files from the folder
    file_list = os.listdir(r"/Users/navdeepsingh/Projects/udacity/python/prank/")
    saved_path = os.getcwd();
    os.chdir('/Users/navdeepsingh/Projects/udacity/python/prank/')
    #(2) rename those files
    for filename in file_list:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        newfilename = filename.translate(translation_table)
        os.rename(filename, newfilename)
        print(newfilename)

rename_files()
