import os
import win32api

filetypes = {
    "log": ['.log','.cvr','.etl'],
    "backup": ['.bak'],
    "dump": ['.dmp', '.hdmp'],
    "temp": ['.tmp', '.temp', '._detmp', '.db$', '.###'],
    "thumbs": ['thumbs.db'],
    "old": ['.chk', '.old'],
    "other": ['.DS_Store', '.??$', '.?$?', '.??~', '.?~?', '.___', '.---', '.$$$', '.@@@', '._mp', '.~mp', '._dd', '.$db', '.fts', '.gid', '.ftg', '.err', 'mscreate.dir', '.wbk', ],
    "partial download": ['.crdownload', '.part'],
}


def typeremove(path, filetypes, maxdepth=10):

    cpath = path.count(os.sep)
    for directory in filetypes:
        for r, d, f in os.walk(path):
            if r.count(os.sep) - cpath < maxdepth:
                for files in f:
                    if files.endswith(tuple(filetypes[directory])):
                        print("Deleted", directory, "file", files)
                        #os.remove(os.path.join(r, files))


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
for drive in drives:
    print("Cleaning drive", drive)
    path = os.path.join(drive, '\\')
    typeremove(path, filetypes)
