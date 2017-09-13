import os
import shutil

print("neatoWindowsTempCleaner started!")


def tempRemove(temp_path,file_list):
    for file in file_list:
        file_path = os.path.join(temp_path, file)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path, ignore_errors=True, onerror=None)
        else:
            try:
                os.remove(file_path)
            except WindowsError:
                continue

    try:
        if os.listdir(temp_path) == []:
            print("neato! just terminated all files!")
        else:
            print("Some of these files couldn't be removed.\nTry closing any active applications and running it again.\n")
            for file in os.listdir(temp_path):
                print("%s" % file)

    except:
        "Directory not found!"
    print("END!")

path = os.path.expanduser('~') + '\AppData\Local\\Temp'
list = os.listdir(path)
tempRemove(path, list)
path = os.path.join(os.environ['SystemRoot'], 'TEMP')
list = os.listdir(path)
tempRemove(path, list)
