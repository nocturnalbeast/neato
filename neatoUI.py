from tkinter import *
import os
import time
import shutil
#import neatoOperaCleaner
#import neatoChromeCleaner
#import neatoWinTemp
import neatoTypeCleaner
#import neatoDesktop

root = Tk()
root.title('neato!')
root.geometry('600x300')
canvas = Canvas(root, width=600, height=300)

bg = PhotoImage(file='bg.gif')
canvas.create_image(0, 0, anchor=NW, image=bg)
#heading = Label(root, text='neato!', bg='grey', fg='white', font='Abode 36')
#heading.pack(anchor=N, pady=10)
#desc = Label(root, text='a simple, no-frills maintenance utility' , bg='grey' ,fg='white', font='Abode 20')
#desc.pack(anchor=N, pady=10)

def quick():
	print ('Quick Mode.')
	#neatoWinTemp()
	#neatoChromeCleaner()
	#neatoOperaCleaner()

def full():
	quick()
	print ('Full Mode.')
	#neatoDesktop()

def paranoid():
	full()
	print ('Paranoid Mode!')
	neatoTypeCleaner()

button1 = Button(root, text='Quick Mode', fg='black', bg='white', font='Abode 15', command=quick)
button1.place(height=30, width=150, x=25, y=200)
button2 = Button(root, text='Full Mode', fg='black', bg='white', font='Abode 15', command=full)
button2.place(height=30, width=150, x=225, y=200)
button3 = Button(root, text='Paranoid Mode', fg='black', bg='white', font='Abode 15', command=paranoid)
button3.place(height=30, width=150, x=425, y=200)

canvas.pack()
root.mainloop()