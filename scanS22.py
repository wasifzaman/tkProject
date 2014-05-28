from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang):

#language changer
	def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)

	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	w.newFrame("L Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (0, 2))
	w.newFrame("Fifth Frame", (3, 0))


#language changer button
	w.frames["L Frame"].addWidget(bclang, (0, 0))
	w.frames["L Frame"].grid(sticky=E)
	bclang.config(cmd=clang)


#add widget to search for students
	w.frames["First Frame"].addWidget(sby, (0, 0))

#basic info widgets
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
	w.frames["Fourth Frame"].grid(rowspan=100, sticky=W)

	attinfo.editwidget=False
	attinfo.canvas.config(width=500, height=500)

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]


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

			#reset portrait
			portr.setData('monet_sm.jpg')
			
			w.populate(d.studentList[w.s].datapoints)

			if cs(d.studentList[w.s].datapoints['firstName'], w.lang): ss()
		except:
			nos(w.lang)
			pass


	def ss():
		d.scanStudent(w.s)
		d.saveData()
		w.frames['Fourth Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])


	def z():
		try:
			ss() if cs(d.studentList[w.s].datapoints['firstName'], w.lang) else False
		except:
			print("error-105")


		

		print(sby.getData())

	w.frames["First Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	w.frames["First Frame"].addWidget(bsearch, (1, 0))
	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

	bcheck = Buttonbox(text='cinstudent', lang=language, repr='bcheck')
	w.frames["Fifth Frame"].addWidget(bcheck, (1, 0))
	bcheck.config(cmd=z)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)







	


if __name__ == '__main__':
	t = Window()

	main(t, language)

	t.mainloop()

