from tkinter import *
from uiHandler22 import *
from dataHandler import *
import addS22
import scanS2
import sDb2
import tools

def main():

	d.loadData()

	t = Window()

		


	w = AppWindow(t)

	w.newFrame("First Frame", (0, 0))

	Button(w.frames["First Frame"], text='Add Students', command=lambda: addS22.main(t)).grid()
	Button(w.frames["First Frame"], text='Scan Students', command=lambda: scanS2.main(top=True)).grid()
	Button(w.frames["First Frame"], text='Student Database', command=lambda: sDb2.main(top=True)).grid()
	Button(w.frames["First Frame"], text='Tools', command=lambda: tools.main(top=True)).grid()

	
	t.mainloop()

main()