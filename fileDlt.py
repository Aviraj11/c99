import os
import shutil
import time

def main():
    path = "/PATH_TO_DELETE"
    days = 30
    seconds = time.time() - (days*24*60*60)

    if (os.path.exists(path)):
        for root_folder, folders, files in os.walk(path):
            if(seconds >= get_file_or_folder_age(root_folder)):
                remove_folder(root_folder)
            else:
                for file in files:
                    files_path = os.path.join(root_folder,file)
                    if(seconds >= get_file_or_folder_age(files_path)):
                        remove_file(files_path)
                
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if(seconds >= get_file_or_folder_age(folder_path)):
                        remove_folder(folder_path)
    else:
        print("Path not Found") 

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path Removed Succesfully")
    else: 
        print("Unable to Delete the Path")

def remove_file(path):
    if not os.remove(path):
        print("Path Removed Succesfully")
    else: 
        print("Unable to Delete the Path")
        
main()
