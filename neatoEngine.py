import os
import shutil
import glob

def rmoove(path):

    for path in os.listdir(path):
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
                print(path, " Deleted!")
        except:
            print("what!!")


def check(path):

    if os.path.exists(path):
        rmoove(path)

def remove(path):

    if os.path.exists(path):
        print(path, " deleted!")
        shutil.rmtree(path, ignore_errors=True)

def globexpander(path):

    for globbed in glob.iglob(path, recursive=True):
        try:
            print (globbed)
            files = os.listdir(os.path.join(globbed))
            for file in files:
                print (os.path.join(globbed,file))
        except:
            print ("Error!")

#windir = os.environ['WinDir']
#localappdata = os.environ['LocalAppData']
#f = open('recursewindir.txt', 'r')
#lines = f.readlines()
#f.close()
#for line in lines:
#    try:
#        path = os.path.join(windir, line)
#        print(path)
#        matchlines = glob.glob(path, recursive=True)
#        for matchline in matchlines:
#            try:
#                print(matchline)
#            except:
#                print("")
#    except:
#        print("")
