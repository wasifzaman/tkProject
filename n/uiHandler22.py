from tkinter import *



class AppFrame(Frame):

	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.curRow = 0
		self.curColumn = 0

		#widgets
		self.widgets = {}

	def addWidget(self, widget, pos):
		self.widgets[widget.repr] = widget
		self.widgets[widget.repr].place(parent=self, row=pos[0], column=pos[1])

class AppWindow(Frame):

	def __init__(self, parent, *args, **kwargs):
		#if top: self = Toplevel()
		#else: self = Tk()

		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		#self.protocol('WM_DELETE_WINDOW', self.dw)

		#self.attributes('-fullscreen', True)

		#root options
		#self.option_add("*Font", "")
		#self.option_add("*Background", "")


		#self.title(title)
		#self.geometry(geometry)
		#self.config(bg="#9FB6CD")

		self.oframe = Frame(self)
		self.mainFrame = Frame(self.oframe)
		self.oframe.pack(fill="both", expand=True, padx=20, pady=20)
		self.mainFrame.place(in_=self.oframe, anchor="c", relx=.5, rely=.5)


		#frames
		self.frames = {}
		self.framePadding = (20, 10)

		#
		#self.update_idletasks()
		#self.after_idle(lambda: self.minsize(self.winfo_width(), self.winfo_height()))	

		self.grid()
		self.oframe.grid()
		self.mainFrame.grid()


		#self.widgets = {}

	def newFrame(self, frameName, gridpos=(0,0)):
		gridRow = gridpos[0]
		gridColumn = gridpos[1]

		self.frames[frameName] = AppFrame(self.mainFrame)

		self.frames[frameName].grid(
			row=gridRow, column=gridColumn,
			padx=self.framePadding[0], pady=self.framePadding[1])

	#def start(self):
		#self.mainloop()

	def collect(self, relevant):

		crossed = {}

		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.repr in relevant:
					crossed[widget.repr] = widget.getData()

		return crossed

	def populate(self, info):

		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.repr in info:
					widget.setData(info[widget.repr])

	def dw(self):
		self.destroy()
		

class Window(Tk):

	def __init__(self):
		#if top: self = Toplevel()
		#else: self = Tk()

		Tk.__init__(self)
		
	

		
		
if __name__ == "__main__":

	w = Window()
	w.newFrame("First Frame")

	f = w.frames["First Frame"]

	w.start()





