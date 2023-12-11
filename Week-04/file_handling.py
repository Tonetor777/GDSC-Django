"""
Create a Python script that identifies and collects files (both created and modified) in the last 24 hours from the current directory. Update these files in some way and move them to a folder named "last_24hours."

Requirements:

Listing Files:
Use the os module to list all files in the current directory.

Identification of Files:
Implement a function to determine whether a file has been created or modified in the last 24 hours.
Consider both the modification time (st_mtime) and creation time (st_ctime) of the file.

Update Files:
Create a function to update the identified files. For example, append a timestamp to the content of each file.

Create "last_24hours" Folder:
Check if a folder named "last_24hours" exists. If not, create it using the os module.

Move Files:
Move the identified and updated files to the "last_24hours" folder using different method
Combine the functions to achieve the main objective.

Feel free to seek clarification on any part of the task. The primary goal is to enhance your understanding of file handling, time-based operations, and module usage in Python.

"""
import os, datetime , shutil
def listFiles():
    files = []
    for (path , dir , file) in os.walk(os.getcwd()):
        files.extend([os.path.join(path, filename) for filename in file if filename.endswith('txt')])
    return files


def Identify_files():
    modified_files = []
    for file in listFiles():
        mod_time = datetime.datetime.fromtimestamp(os.stat(file).st_mtime)
        created_time = datetime.datetime.fromtimestamp(os.stat(file).st_ctime)
        mdiff = (datetime.datetime.now() - mod_time )
        cdiff = ( datetime.datetime.now() - created_time)
        if mdiff.total_seconds() / 3600 < 24 or cdiff.total_seconds() / 3600 < 24:
            modified_files.append(file)
    return modified_files

def update_files ():
    for file in Identify_files():
        with open(file , 'a') as update:
            update.write(f'\nCurrent Time Stamp:{datetime.datetime.now()}')

def create_folder():
    try:
        os.mkdir('last_24hours')
    except FileExistsError:
        return 'Folder already exists'
    except Exception as e:
        return f'Error: ' , e

def move_modified_files():
    update_files()
    create_folder()
    destination = os.getcwd() + '\last_24hours'
    for file in Identify_files():
        shutil.move(file , destination)


#TEST CODE
move_modified_files()


