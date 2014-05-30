from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
import importwiz


def main(t, lang):

	def cdb():
		try:
			p = filedialog.askopenfile().name.split('/')[-1]
			if p[p.rfind('.'):]!= '.db':
				print("invalid file")
				return
			else:
				curdb.config(text=p)
		except:
			print("error opening file.")


	def ctdb():
		try:
			p = filedialog.askopenfile().name.split('/')[-1]
			ext = p[p.rfind('.'):]
			if ext != '.xls' and ext != '.xlsx':
				print("invalid file")
				return
			else:
				d.loadData()
				d.importtimexlsx(p)
				d.saveData()
		except:
			print("error opening file.")


	def ss():
		def z():
			s.config['dbFile'] = curdb.cget('text')
		s.saveSettings(lambda: z())
		dbs(w.lang)


		


	def it():
		return


	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Fifth Frame", (2, 0))
	w.newFrame("Second Frame", (3, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (4, 1))

#import export widgets
	w.frames["First Frame"].addWidget(imp, (0, 0))
	w.frames["First Frame"].addWidget(sepr, (1, 0))
	w.frames["First Frame"].addWidget(bimp, (2, 0))

	w.frames["Fifth Frame"].addWidget(impt, (0, 0))
	w.frames["Fifth Frame"].addWidget(sepr, (1, 0))
	w.frames["Fifth Frame"].addWidget(bimpt, (2, 0))

	w.frames["Second Frame"].addWidget(exp, (0, 0))
	w.frames["Second Frame"].addWidget(sepr, (1, 0))
	w.frames["Second Frame"].addWidget(bexp, (2, 0))

	curdb = Label(w.frames['Third Frame'], text=s.config['dbFile'])
	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	curdb.grid(row=1, column=0)

	w.frames["Third Frame"].addWidget(bcdb, (2, 0))


	w.frames['Fourth Frame'].addWidget(bsav, (0, 0))

	bsav.config(cmd=ss)
	bimp.config(cmd=lambda: importwiz.main(w.lang))
	bcdb.config(cmd=cdb)
	bimpt.config(cmd=ctdb)
	#curdb.config(text=s.config['dbFile'])
	#exp.config(cmd=importwiz.main)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)


if __name__ == '__main__':
	t = Window()
	main(t, language)
	
	t.mainloop()