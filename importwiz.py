from uiHandler2 import *
from dataHandler import *
from preBuilts import *
from tkinter import filedialog

def main(top=False):

	def odb():
		try:
			fpath.setData(filedialog.askopenfile().name)
		except:
			pass

#		nd = StudentDB(file='temp.db')

	def pvdb():

		w.frames["First Frame"].grid_forget()
		w.frames["Second Frame"].grid_forget()
		w.frames["Third Frame"].grid_forget()

		w.frames["Fourth Frame"].grid()
		w.frames["Fifth Frame"].grid()

		nd = StudentDB(file='temp.db')
		nd.importxlsx(fpath.getData())

		sL = []
		for s in nd.studentList.values():
			dp = s.datapoints
			sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

		sL.sort()
		stable.setData((stableh, sL))

	def pdb():
		try:
			fpath2.setData(filedialog.asksaveasfilename())
		except:
			pass

	def sav():
		f = fpath2.getData().split('/')[-1] + '.db'
		nd = StudentDB(file=f)
		nd.importxlsx(fpath.getData())
		w.dw()



	d.loadData()

	w = Window(top=top, geometry='500x700')

	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (2, 0))

	w.newFrame("Fourth Frame", (3, 0))
	w.newFrame("Fifth Frame", (4, 0))

	w.frames["Fourth Frame"].grid_forget()
	w.frames["Fifth Frame"].grid_forget()


	Label(w.frames["First Frame"], text="Welcome to the Import wizard.\n\n\nPlease select the xls or xlsx file below.\nThen click Next.").grid()


	w.frames["Second Frame"].addWidget(fpath, (0, 0))
	w.frames["Second Frame"].addWidget(brw, (0, 3))
	#w.frames["Third Frame"].addWidget(bk, (0, 0))
	w.frames["Third Frame"].addWidget(nxt, (0, 1))
	w.frames["Fourth Frame"].addWidget(stable, (0, 0))
	w.frames["Fifth Frame"].addWidget(fpath2, (0, 0))
	w.frames["Fifth Frame"].addWidget(brw2, (0, 3))
	w.frames["Fifth Frame"].addWidget(sepr, (1, 0))
	w.frames["Fifth Frame"].addWidget(bsav, (2, 1))


	brw.config(cmd=odb)
	brw2.config(cmd=pdb)

	nxt.config(cmd=pvdb)
	bsav.config(cmd=sav)


	
	w.start()

if __name__ == '__main__':
	main()
