from uiHandler2 import *
from dataHandler import *
from preBuilts import *


def main():

	d.loadData()

	w = Window(geometry='900x600')



	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (2, 1))


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



	def s():
		#w.populate(d.studentList[sby.getData()[1]].datapoints)
		print(sby.getData())

	Button(w.frames["First Frame"], text="try", command=s).pack()








	w.start()


if __name__ == '__main__':
	main()

