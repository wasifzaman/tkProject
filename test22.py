#test ui
from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from languages import *
#import goslate


def main():

	t = Window(top=False)
	t.attributes('-fullscreen', False)
	t.geometry('700x700')
	
	w = AppWindow(t.mainFrame)

	w.lang = language

	w.newFrame("First Frame", (0, 0))
	

	


	sL = [['abc', 'bcd', '123'],\
		['abc', 'def', '123'],\
		['x', 'y', 'zprevis']]

	sL2 = list(sL)

	w.attinfo = Table(repr='attinfo', edit=True)
	w.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
	w.attinfo.build(headers=w.attinfoh, data=[[]])
	w.attinfo.clast = '#FF99FF'

	w.frames["First Frame"].addWidget(w.attinfo, (0, 0))
	
	w.attinfo.setData((w.attinfoh, sL))
	w.attinfo.setData((w.attinfoh, [['def', '345', '565'], ['xyz']]))
	w.attinfo.setData((w.attinfoh, [['def', '345', '565'], ['xyz'], ['123']]))
	w.attinfo.setData((w.attinfoh, [['def', '345', '565'], ['xyz'], ['123'], ['456']]))
	w.attinfo.setData((w.attinfoh, [['def', '345', '565'], ['xyz'], ['123'], ['456'], ['678']]))
	
	w.attinfo.setData((w.attinfoh, [[]]))

	

	
	


	t.mainloop()
if __name__ == '__main__':
	main()