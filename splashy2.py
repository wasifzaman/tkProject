from tkinter import *
from uiHandler22 import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
import addS22
import scanS22
import sDb22
import tools2

def main():

#clang
	def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)

	d.loadData()

	t = Window(top=False)

	def showWindow(f):
		w.frames["First Frame"].grid_forget()
		w.t = f(w.frames["Second Frame"], w.lang)
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()


	def showMain():
		w.frames['Second Frame'].grid_forget()
		try:
			w.t.destroy()
		except:
			pass
		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.frames['Second Frame'].destroy()
		w.newFrame("Second Frame", (1, 0))
		w.frames['Second Frame'].grid_forget()

		w.frames["First Frame"].grid()
		w.frames['Third Frame'].grid_forget()
		


	w = AppWindow(t.mainFrame)
	w.lang = languages['english']

	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (2, 0))


	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

	bsadd = Buttonbox(text='Add Students', lang=w.lang, repr='bsadd')
	bsscan = Buttonbox(text='Scan Students', lang=w.lang, repr='bsscan')
	bssdb = Buttonbox(text='Student Database', lang=w.lang, repr='bssdb')
	bstools = Buttonbox(text='Tools', lang=w.lang, repr='bstools')
	bsbmm = Buttonbox(text='Back to Main Menu', lang=w.lang, repr='bsbmm')
	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit')
	bclang = Buttonbox(text='changelanguage', lang=w.lang, repr='bclang')

	w.frames["First Frame"].addWidget(bsadd, (0, 0))
	w.frames["First Frame"].addWidget(bsscan, (1, 0))
	w.frames["First Frame"].addWidget(bssdb, (2, 0))
	w.frames["First Frame"].addWidget(bstools, (3, 0))
	w.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	w.frames["First Frame"].addWidget(bsexit, (5, 0))
	w.frames["First Frame"].addWidget(bclang, (4, 0))
	
	bsadd.config(cmd=lambda: showWindow(addS22.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=showMain)
	bsexit.config(cmd=t.destroy)
	bclang.config(cmd=clang)
	
	t.mainloop()


if __name__ == '__main__':
	main()

	