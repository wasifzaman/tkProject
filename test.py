#test ui
from uiHandler2 import *
from dataHandler import *
from preBuilts import *
from tableWidget2 import *


w = Window(geometry='500x500')
w.newFrame("First Frame", (0,0))
w.newFrame("Second Frame", (1,0))


w.frames["First Frame"].addWidget(firstName, (0, 0))
w.frames["First Frame"].addWidget(lastName, (1, 0))
w.frames["First Frame"].addWidget(age, (3, 0))
w.frames["First Frame"].addWidget(dob, (4, 0))
w.frames["First Frame"].addWidget(tpa, (5, 0))



print(w.frames)
print(w.frames["First Frame"].widgets)

def collect():
	student = StudentInfo()
	#w.frames["First Frame"].widgets["dob"].setData('10/07/88')
	print(w.collect(student.datapoints))

Button(w.frames["First Frame"], text="try", command=collect).grid(row=100)

w.frames["Second Frame"].addWidget(attinfo, (6, 0))

#attinfo.update(headers=['e', 'f', 'g'], data=[['hello!', 'world!'], ['updatess'], ['getting', 'crazy', '!']])

attinfo.setData((['e', 'f', 'g'], [['hello!', 'world!'], ['updatess'], ['getting', 'crazy', '!']]))


w.start()

