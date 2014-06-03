from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

	d.loadData()

	w = AppWindow(t)

	w.bind("<Destroy>", lambda event: t2.destroy)

	w.lang = lang

#attendance table
	w.attinfo = Table(repr='attinfo', edit=True)
	w.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
	w.attinfo.build(headers=w.attinfoh, data=[[]])
	w.attinfo.clast = '#FF99FF'

#frame initialization
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (0, 2))
	w.newFrame("Fifth Frame", (3, 0))

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

#award class widgets
	w.frames["Second Frame"].addWidget(sType, (16, 0))
	w.frames["Second Frame"].addWidget(cAwarded, (17, 0))
	w.frames["Second Frame"].addWidget(cRemaining, (16, 2))

	w.frames["Second Frame"].addWidget(sepr, (18, 0))

#special
	spec = Labelbox(text='spec', lang=w.lang, repr='spec')
	w.frames["Second Frame"].addWidget(spec, (19, 0))

	w.portr = portr = Photo(repr='portr', path='monet_sm.jpg')
	w.frames["Third Frame"].addWidget(w.portr, (0, 0))

	w.frames["Fourth Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Fourth Frame"].grid(rowspan=100, sticky=W)

	w.attinfo.editwidget=False
	w.attinfo.canvas.config(width=500, height=500)

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
			w.portr.setData('monet_sm.jpg')
			portr2.setData('monet_sm.jpg')

			#reset classes rem
			spec.setData("")

			#temp workaround while table is fixed
			for child in w.frames["Fourth Frame"].winfo_children():
				child.destroy()

			w.attinfo.build(headers=w.attinfoh, data=[[]])
			w.frames["Fourth Frame"].addWidget(w.attinfo, (0, 0))
			w.frames["Fourth Frame"].grid(rowspan=100, sticky=W)

			w.attinfo.editwidget=False
			w.attinfo.canvas.config(width=500, height=500)
			#

			#temp workaround while table is fixed
			for child in w2.frames["Third Frame"].winfo_children():
				child.destroy()

			w2.attinfo.build(headers=w2.attinfoh, data=[[]])
			w2.frames["Third Frame"].addWidget(w2.attinfo, (0, 0))
			w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

			w2.attinfo.editwidget=False
			w2.attinfo.canvas.config(width=500, height=500)
			#

			w.populate(d.studentList[w.s].datapoints)
			w2.populate(d.studentList[w.s].datapoints)

			if cs(d.studentList[w.s].datapoints['firstName'], w.lang): ss()
		except:
			nos(w.lang)
			pass


	def ss():
		d.scanStudent(w.s, xtra=w.lang['Auto'] if sby.getData()[0] == 'bCode' else w.lang['Manual'])
		d.saveData()
		
		#show alert if classes remaining is less than 2
		cRem = d.studentList[w.s].datapoints['cRemaining']
		if cRem <= 2:
			spec.setData(w.lang['Classes remaining for this student'] + ': ' + str(cRem))
			spec.label.config(bg='yellow')

		#update cRemaining
		cRemaining.setData(str(cRem))

		w.frames['Fourth Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])
		w2.frames['Third Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])


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

#t2 window
	t2 = Window(top=True)
	t2.attributes('-fullscreen', False)
	t2.geometry('1200x800')

#remove close button function
	t2.protocol('WM_DELETE_WINDOW', lambda: False)

#set minimum height
	t2.update_idletasks()
	t2.after_idle(lambda: t2.minsize(t2.winfo_width(), t2.winfo_height()))

	w2 = AppWindow(t2.mainFrame)

	w2.lang = lang

#attendance table
	w2.attinfo = Table(repr='attinfo', edit=True)
	w2.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
	w2.attinfo.build(headers=w2.attinfoh, data=[[]])
	w2.attinfo.clast = '#FF99FF'

#frame initialization
	w2.newFrame("First Frame", (0, 0))
	w2.newFrame("Second Frame", (1, 0))
	w2.newFrame("Third Frame", (0, 1))

	firstName2 = Textbox(text="First Name", lang=language, repr='firstName')
	lastName2 = Textbox(text="Last Name", lang=language, repr='lastName')
	chineseName2 = Textbox(text="Chinese Name", lang=language, repr='chineseName')
	bCode2 = Textbox(text="Barcode", lang=language, repr='bCode')
	sid2 = IntTextbox(text="Old Student ID", lang=language, repr='sid')
	dob2 = Datebox(text="Date of Birth", lang=language, repr='dob')
	portr2 = Photo(repr='portr', path='monet_sm.jpg')

	w2.frames["First Frame"].addWidget(portr2, (0, 0))

#basic info widgets
	w2.frames["Second Frame"].addWidget(firstName2, (0, 0))
	w2.frames["Second Frame"].addWidget(lastName2, (1, 0))
	w2.frames["Second Frame"].addWidget(chineseName2, (2, 0))

	w2.frames["Second Frame"].addWidget(sepr, (5, 0))

	w2.frames["Second Frame"].addWidget(bCode2, (6, 0))
	w2.frames["Second Frame"].addWidget(sid2, (7, 0))

	w2.frames["Second Frame"].addWidget(sepr, (8, 0))

	w2.frames["Second Frame"].addWidget(dob2, (10, 0))

#att table widget
	w2.frames["Third Frame"].addWidget(w.attinfo, (0, 0))
	w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

	w2.attinfo.editwidget=False
	w.attinfo.canvas.config(width=500, height=500)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)
	for frame in w2.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	return t2


	





	


if __name__ == '__main__':
	t = Window()
	t.attributes('-fullscreen', False)
	t.geometry('1000x700')

	main(t.mainFrame, language)

	t.mainloop()

	print('abcd'[:3])

