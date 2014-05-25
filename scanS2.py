from uiHandler2 import *
from dataHandler import *
from preBuilts import *


def main(top=False):

	d.loadData()

	w = Window(top=top, geometry='1300x600')



	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (1, 2))
	w.newFrame("Fifth Frame", (2, 1))


	w.frames["First Frame"].addWidget(sby, (0, 0))


	w.frames["Second Frame"].addWidget(firstName, (0, 0))
	w.frames["Second Frame"].addWidget(lastName, (1, 0))
	w.frames["Second Frame"].addWidget(chineseName, (2, 0))
	w.frames["Second Frame"].addWidget(parentName, (3, 0))
	w.frames["Second Frame"].addWidget(pup, (4, 0))

	w.frames["Second Frame"].addWidget(sepr, (5, 0))

	w.frames["Second Frame"].addWidget(bCode, (6, 0))
	w.frames["Second Frame"].addWidget(sid, (7, 0))



	w.frames["Second Frame"].addWidget(dob, (10, 0))
	w.frames["Second Frame"].addWidget(age, (11, 0))

	w.frames["Second Frame"].addWidget(sepr, (12, 0))


	#
	w.frames["Second Frame"].addWidget(addr, (0, 2))
	w.frames["Second Frame"].addWidget(city, (1, 2))
	w.frames["Second Frame"].addWidget(state, (2, 2))
	w.frames["Second Frame"].addWidget(zip, (3, 2))
	w.frames["Second Frame"].addWidget(email, (4, 2))


	w.frames["Second Frame"].addWidget(hPhone, (6, 2))
	w.frames["Second Frame"].addWidget(cPhone, (7, 2))
	w.frames["Second Frame"].addWidget(cPhone2, (8, 2))


	w.frames["Third Frame"].addWidget(portr, (0, 0))

	w.frames["Fourth Frame"].addWidget(attinfo, (0, 0))

	attinfo.editwidget=False

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]


	def s():
		w.s = sby.getData()[1]

		print(sby.getData())


		if sby.getData()[0] != 'bCode':
			sty = sby.getData()[0]
			sdp = sby.getData()[1]

			sl = []

			for s in d.studentList:
				if d.studentList[s].datapoints[sty] == sdp:
					dp = d.studentList[s].datapoints
					sl.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['dob']])


			if len(sl) == 0: return

			w.s = sl[0][0]
			#print(sl)
			if len(sl) > 1:
				sl.sort()
				w.s = spicker(sl)

		w.populate(d.studentList[w.s].datapoints)

		if cs(d.studentList[w.s].datapoints['firstName']): ss()
		#print(d.studentList[w.s].datapoints['attinfo'])
		
		#else:
			#w.populate(d.studentList[sby.getData()[1]].datapoints)


	def ss():
		d.scanStudent(w.s)
		d.saveData()
		#print(d.studentList[w.s].datapoints['attinfo'])
		w.frames['Fourth Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])


	def z():
		try:
			ss() if cs(d.studentList[w.s].datapoints['firstName']) else False
		except:
			print("error-105")


		

		print(sby.getData())

	w.frames["First Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())
	Button(w.frames["First Frame"], text="try", command=s).pack()

	Button(w.frames["Fifth Frame"], text="Scan", command=z).pack()








	w.start()


if __name__ == '__main__':
	main()

