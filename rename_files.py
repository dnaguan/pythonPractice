import os
def rename_files():
    #(1) get file names
    file_list = os.listdir(r"C:\CursoPython\prank")
    print("Old list: ")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\CursoPython\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name + "  New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    file_list = os.listdir(r"C:\CursoPython\prank")
    print("New list")
    print(file_list)

rename_files()
