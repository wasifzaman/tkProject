from uiHandler2 import *
from dataHandler import *
import addS2
import scanS2
import sDb2

def main():

	d.loadData()

	w = Window(geometry='300x200')

	w.newFrame("First Frame", (0, 0))

	Button(w.frames["First Frame"], text='Add Students', command=addS2.main).grid()

	w.start()


main()