from uiHandler2 import *
from dataHandler import *
from preBuilts import *
import importwiz


def main(top=False):

	d.loadData()

	w = Window(top=top, geometry='500x300')

	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (0, 1))


	w.frames["First Frame"].addWidget(imp, (0, 0))
	w.frames["First Frame"].addWidget(sepr, (1, 0))
	w.frames["First Frame"].addWidget(bimp, (2, 0))

	w.frames["Second Frame"].addWidget(exp, (0, 0))
	w.frames["Second Frame"].addWidget(sepr, (1, 0))
	w.frames["Second Frame"].addWidget(bexp, (2, 0))

	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	#w.frames["Third Frame"].addWidget(sepr, (1, 0))
	#w.frames["Third Frame"].addWidget(bexp, (2, 0))

	bimp.config(cmd=importwiz.main)
	#exp.config(cmd=importwiz.main)

	w.start()


if __name__ == '__main__':
	main()