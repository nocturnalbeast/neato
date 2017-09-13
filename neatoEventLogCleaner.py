import os
import subprocess


def EventLogBatFilePopulate():

    with open("eventlogtemp.txt", mode="w+") as tempfile:
        subprocess.call(["wevtutil", "el"], stdout=tempfile)


def EventLogBatFileGenerate():

    prefix = 'wevtutil cl '
    with open('eventlogtemp.txt', 'r+') as tempsrc:
        with open('eventlogbat.txt', 'w+') as tempdest:
            for line in tempsrc:
                tempdest.write('%s%s\n' % (prefix, line.rstrip('\n')))
    os.rename('eventlogbat.txt', 'neventlog.bat')
    os.remove('eventlogtemp.txt')


def EventLogBatFileExecute():

	#printing for now. repl with true deletion when ready.
	#subprocess.call("./neventlog.bat")
    with open('neventlog.bat', 'r+') as tempfile:
        for line in tempfile:
            print(line)
    print("Event Logs Cleared!")

EventLogBatFilePopulate()
EventLogBatFileGenerate()
EventLogBatFileExecute()
