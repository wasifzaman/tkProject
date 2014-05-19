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

class Window:

	def __init__(self, top=False, title='', geometry='200x200'):
		if top: self.root = Toplevel()
		else: self.root = Tk()

		#self.root.attributes('-fullscreen', True)

		#root options
		#self.root.option_add("*Font", "")
		#self.root.option_add("*Background", "")


		self.root.title(title)
		self.root.geometry(geometry)
		self.root.config(bg="#9FB6CD")

		self.mainFrame = Frame(self.root)
		self.mainFrame.pack(fill=Y, expand=1, anchor=S)


		#frames
		self.frames = {}
		self.framePadding = (20, 10)


		self.widgets = {}

	def newFrame(self, frameName, gridpos=(0,0)):
		gridRow = gridpos[0]
		gridColumn = gridpos[1]

		self.frames[frameName] = AppFrame(self.mainFrame)

		self.frames[frameName].grid(
			row=gridRow, column=gridColumn,
			padx=self.framePadding[0], pady=self.framePadding[1])

	def start(self):
		self.root.mainloop()

	def collect(self, relevant):

		crossed = {}

		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.repr in relevant:
					crossed[widget.repr] = widget.getData()

		return crossed

	

		
		
if __name__ == "__main__":

	w = Window()
	w.newFrame("First Frame")

	f = w.frames["First Frame"]

	w.start()





