#test ui
from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from languages import *
#import goslate


def main():

	t = Window(top=False)
	
	w = AppWindow(t.mainFrame)

	w.lang = language

	w.newFrame("First Frame", (0, 0))

	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit')

	#w.frames["First Frame"].addWidget(bsexit, (5, 0))

	bsexit.config(cmd=t.destroy)

	

	r = Radiobutton(w.frames["First Frame"], text='abcd')
	print(r.cget('text'))


	t.mainloop()
if __name__ == '__main__':
	main()