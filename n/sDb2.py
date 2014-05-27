from uiHandler2 import *
import editS2
from dataHandler import *
from preBuilts import *


def main(top=False):

	d.loadData()

	w = Window(top=top, geometry='900x600')



	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (2, 1))


	w.frames["First Frame"].addWidget(sby, (0, 0))


	w.frames["Second Frame"].addWidget(stable, (0, 0))

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]

	sL = []
	for s in d.studentList.values():
		dp = s.datapoints
		sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL.sort()
	stable.setData((stableh, sL))

	sbind(lambda i: editS2.main(top=True, i=i))



	def s():
		print(sby.getData())
		editS2.main(top=True, i=sby.getData()[1])

	Button(w.frames["First Frame"], text="try", command=s).pack()



	w.start()

if __name__ == '__main__':
	main()


