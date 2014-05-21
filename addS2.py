from uiHandler2 import *
from dataHandler import *
from preBuilts import *


w = Window(geometry='900x600')



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
w.frames["First Frame"].addWidget(sid, (8, 0))



w.frames["First Frame"].addWidget(dob, (10, 0))
w.frames["First Frame"].addWidget(age, (11, 0))

#
w.frames["First Frame"].addWidget(addr, (0, 2))
w.frames["First Frame"].addWidget(city, (1, 2))
w.frames["First Frame"].addWidget(state, (2, 2))
w.frames["First Frame"].addWidget(zip, (3, 2))
w.frames["First Frame"].addWidget(email, (4, 2))

w.frames["First Frame"].addWidget(sepr, (5, 2))

w.frames["First Frame"].addWidget(hPhone, (6, 2))
w.frames["First Frame"].addWidget(cPhone, (7, 2))
w.frames["First Frame"].addWidget(cPhone2, (8, 2))


w.frames["Second Frame"].addWidget(portr, (0, 0))



def collect():
	print(w.collect(StudentInfo().datapoints))

Button(w.frames["Third Frame"], text="Add Student to Database", command=collect).grid()








w.start()

