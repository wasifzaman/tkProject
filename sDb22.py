from uiHandler22 import *
import editS2
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

	d.loadData()

	w = AppWindow(t)

	w.lang = lang


	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (2, 1))

	#widget for scan
	w.frames["First Frame"].addWidget(sby, (0, 0))
	w.frames["First Frame"].addWidget(bsearch, (1, 0))
	


	w.frames["Second Frame"].addWidget(stable, (2, 0))

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]

	sL = []
	for s in d.studentList.values():
		dp = s.datapoints
		sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL.sort()
	stable.setData((stableh, sL))
	stable.canvas.config(width=700, height=700)

	sbind(lambda i: editS2.main(w.lang, top=True, i=i, d=d))



	def s():
		try:
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


				if len(sl) == 0:
					nos(w.lang)
					return

				w.s = sl[0][0]
				if len(sl) > 1:
					sl.sort()
					w.s = spicker(sl)
					if not w.s: return

			print(w.s)
			editS2.main(w.lang, top=True, i=w.s)
		except:
			nos(w.lang)
			pass


	w.frames["First Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

	#button for scan
	#Button(w.frames["First Frame"], text="try", command=s).grid()




if __name__ == '__main__':
	t = Window()
	main(t, language)

	t.mainloop()


