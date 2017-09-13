import ctypes
import sys

def CheckAdmin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

if CheckAdmin():
	print("Already Elevated!")
else:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
	print("Elevated Now!")