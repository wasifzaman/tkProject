#test ui
from uiHandler2 import *
from dataHandler import *
from preBuilts import *



w = Window(geometry='700x500')
w.newFrame("First Frame", (0,0))
w.newFrame("Second Frame", (1,0))
w.newFrame("Third Frame", (0,1))
w.newFrame("Fourth Frame", (1,1))


w.frames["First Frame"].addWidget(firstName, (0, 0))
w.frames["First Frame"].addWidget(lastName, (1, 0))
w.frames["First Frame"].addWidget(sepr, (6, 0))
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

w.frames["Second Frame"].addWidget(attinfo, (0, 0))

#attinfo.update(headers=['e', 'f', 'g'], data=[['hello!', 'world!'], ['updatess'], ['getting', 'crazy', '!']])

attinfo.setData((attinfoh, [['hello!', 'world!'], ['updatess'], ['getting', 'crazy', '!']]))



w.frames["Third Frame"].addWidget(portr, (0, 0))
portr.setData('monet_sm.jpg')

w.frames["Fourth Frame"].addWidget(stable, (1, 0))

stable.setData((stableh, [['1234', 'Johnny', 'Test', '10/07/1988']]))

w.start()

