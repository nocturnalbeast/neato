import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
for drive in drives:
	print(drive)

#print (os.path.expanduser('~\Desktop'))
#print (os.environ['LocalAppData'])
#
#path = os.environ['SystemRoot']
#print (path)
#files = os.listdir(os.path.join(path))
#for file in files:
#	print(os.path.join(path,file))
#
#
#path = os.path.join(os.environ['AppData'])
#list = os.listdir(path)
#for file in list:
	#print(file)

