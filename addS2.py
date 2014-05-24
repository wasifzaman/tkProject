from uiHandler2 import *
from dataHandler import *
from preBuilts import *


def main():

	d.loadData()

	w = Window(geometry='900x700')



	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (0, 1))
	w.newFrame("Third Frame", (1, 1))



	w.frames["First Frame"].addWidget(firstName, (0, 0))
	w.frames["First Frame"].addWidget(lastName, (1, 0))
	w.frames["First Frame"].addWidget(chineseName, (2, 0))
	w.frames["First Frame"].addWidget(parentName, (3, 0))
	w.frames["First Frame"].addWidget(pup, (4, 0))

	w.frames["First Frame"].addWidget(sepr, (5, 0))

	w.frames["First Frame"].addWidget(bCode, (6, 0))
	w.frames["First Frame"].addWidget(sid, (7, 0))



	w.frames["First Frame"].addWidget(dob, (10, 0))
	w.frames["First Frame"].addWidget(age, (11, 0))

	w.frames["First Frame"].addWidget(sepr, (12, 0))

	w.frames["First Frame"].addWidget(findSchool, (13, 0))
	w.frames["First Frame"].addWidget(notes, (14, 0))

	findSchool.config(height=3, width=10)
	notes.config(height=3, width=10)

	w.frames["First Frame"].addWidget(sepr, (15, 0))


	w.frames["First Frame"].addWidget(sType, (16, 0))
	w.frames["First Frame"].addWidget(cAwarded, (17, 0))
	w.frames["First Frame"].addWidget(cRemaining, (17, 0))
	w.frames["First Frame"].widgets['cRemaining'].hide()
	w.frames["First Frame"].addWidget(tpd, (16, 2))
	w.frames["First Frame"].addWidget(tpa, (17, 2))
	Button(w.frames["First Frame"], text="Award Classes", command=cpicker).grid()
	Button(w.frames["First Frame"], text="Award One Classe", command=caddone).grid()
	Button(w.frames["First Frame"], text="Award Additional Classes", command=cadd).grid()


	#
	w.frames["First Frame"].addWidget(addr, (0, 2))
	w.frames["First Frame"].addWidget(city, (1, 2))
	w.frames["First Frame"].addWidget(state, (2, 2))
	w.frames["First Frame"].addWidget(zip, (3, 2))
	w.frames["First Frame"].addWidget(email, (4, 2))


	w.frames["First Frame"].addWidget(hPhone, (6, 2))
	w.frames["First Frame"].addWidget(cPhone, (7, 2))
	w.frames["First Frame"].addWidget(cPhone2, (8, 2))


	w.frames["Second Frame"].addWidget(portr, (0, 0))



	def collect():
		ns = StudentInfo()
		ns.datapoints = dict(list(ns.datapoints.items()) + list(w.collect(ns.datapoints).items()))
		print(ns.datapoints)

		nsbcode = ns.datapoints['bCode']

		if d.checkCode(nsbcode):
			if not ase(d.studentList[nsbcode].datapoints['firstName']):
				return
		else:
			if not con(ns.datapoints['firstName']):
				return

		d.addStudent(ns.datapoints['bCode'], ns)
		d.saveData()

		sa(ns.datapoints['firstName'])

		print(w.collect(StudentInfo().datapoints))

	Button(w.frames["Third Frame"], text="Add Student to Database", command=collect).grid()

	Button(w.frames["Second Frame"], text="Browse Photo", command=ppicker).grid()








	w.start()


if __name__ == '__main__':
	main()
