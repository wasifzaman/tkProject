from uiHandler22 import *
import editS2
from dataHandler import *
from preBuilts2 import *


def main(t, lang):

	d.loadData()

	w = AppWindow(t)

	w.lang = lang


	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (2, 1))

	#widget for scan
	#w.frames["First Frame"].addWidget(sby, (0, 0))


	w.frames["Second Frame"].addWidget(stable, (0, 0))

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]

	sL = []
	for s in d.studentList.values():
		dp = s.datapoints
		sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL.sort()
	stable.setData((stableh, sL))
	stable.canvas.config(width=700, height=700)

	sbind(lambda i: editS2.main(w.lang, top=True, i=i))



	def s():
		print(sby.getData())
		editS2.main(top=True, i=sby.getData()[1])

	#button for scan
	#Button(w.frames["First Frame"], text="try", command=s).grid()




if __name__ == '__main__':
	t = Window()
	main(t, language)

	t.mainloop()


