from uiHandler2 import *
from dataHandler import *
import addS2
import scanS2
import sDb2
import tools

def main():

	d.loadData()

	w = Window(geometry='300x200')

	w.newFrame("First Frame", (0, 0))

	Button(w.frames["First Frame"], text='Add Students', command=lambda: addS2.main(top=True)).grid()
	Button(w.frames["First Frame"], text='Scan Students', command=lambda: scanS2.main(top=True)).grid()
	Button(w.frames["First Frame"], text='Student Database', command=lambda: sDb2.main(top=True)).grid()
	Button(w.frames["First Frame"], text='Tools', command=lambda: tools.main(top=True)).grid()

	w.start()


main()