from tkinter import *
from uiHandler22 import *
from dataHandler import *
import addS22
import scanS22
import sDb22
import tools2

def main():

	d.loadData()

	t = Window(top=False)

	def showWindow(f):
		w.frames["First Frame"].grid_forget()
		f(w.frames["Second Frame"])
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()


	def showMain():
		w.frames['Second Frame'].grid_forget()
		w.frames['Second Frame'].destroy()
		w.newFrame("Second Frame", (1, 0))
		w.frames['Second Frame'].grid_forget()

		w.frames["First Frame"].grid()
		w.frames['Third Frame'].grid_forget()
		


	w = AppWindow(t.mainFrame)

	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (2, 0))

	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

	Button(w.frames["First Frame"], text='Add Students', command=lambda: showWindow(addS22.main)).grid()
	Button(w.frames["First Frame"], text='Scan Students', command=lambda: showWindow(scanS22.main)).grid()
	Button(w.frames["First Frame"], text='Student Database', command=lambda: showWindow(sDb22.main)).grid()
	Button(w.frames["First Frame"], text='Tools', command=lambda: showWindow(tools2.main)).grid()
	Button(w.frames["Third Frame"], text='Back to Main Window', command=showMain).grid()
	Button(w.frames["First Frame"], text='Exit', command=t.destroy).grid()

	
	t.mainloop()


if __name__ == '__main__':
	main()

	