from uiHandler2 import *
from dataHandler import *
from preBuilts import *
import importwiz


def main(top=False, lang):

	def cdb():
		try:
			p = filedialog.askopenfile().name.split('/')[-1]
			if p[-3:] != '.db':
				print("invalid file")
				return
			else:
				curdb.setData(p)
		except:
			print("error opening file.")

	def ss():
		def z():
			s.config['dbFile'] = curdb.getData()
		s.saveSettings(lambda: z())
		w.dw()


	def it():
		return


	d.loadData()

	w = Window(top=top, geometry='500x400')

	w.lang = lang

	w.newFrame("First Frame", (0, 0))
	w.newFrame("Fifth Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (0, 1))
	w.newFrame("Fourth Frame", (3, 1))


	w.frames["First Frame"].addWidget(imp, (0, 0))
	w.frames["First Frame"].addWidget(sepr, (1, 0))
	w.frames["First Frame"].addWidget(bimp, (2, 0))

	w.frames["Fifth Frame"].addWidget(impt, (0, 0))
	w.frames["Fifth Frame"].addWidget(sepr, (1, 0))
	w.frames["Fifth Frame"].addWidget(bimpt, (2, 0))

	w.frames["Second Frame"].addWidget(exp, (0, 0))
	w.frames["Second Frame"].addWidget(sepr, (1, 0))
	w.frames["Second Frame"].addWidget(bexp, (2, 0))

	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	w.frames["Third Frame"].addWidget(curdb, (1, 0))
	w.frames["Third Frame"].addWidget(bcdb, (2, 0))
	#w.frames["Third Frame"].addWidget(sepr, (1, 0))
	#w.frames["Third Frame"].addWidget(bexp, (2, 0))

	Button(w.frames["Fourth Frame"], text="     Save     ", command=ss).grid()
	Button(w.frames["Fourth Frame"], text="   Cancel   ", command=w.dw).grid()

	bimp.config(cmd=importwiz.main)
	bcdb.config(cmd=cdb)
	curdb.config(text=s.config['dbFile'])
	#exp.config(cmd=importwiz.main)

	w.start()


if __name__ == '__main__':
	main()
	print('abcd.db'[-3:])