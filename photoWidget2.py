import os.path
from tkinter import Label
from widget import Widget
from PIL import Image, ImageTk


class Photo(Widget):

	def __init__(self, **kwargs):

		try:
			self.repr = kwargs['repr']
			self.path = kwargs['path']
		except:
			print("widget could not be loaded")

		self.script_dir = os.path.dirname(os.path.abspath(__file__))


	def config(self, **kwargs):

		try:
			self.path = kwargs['path']
			self.picture = Image.open(os.path.join(self.script_dir, self.path))
			self.image = ImageTk.PhotoImage(self.picture)
			self.label.config(image=self.image)
		except:
			pass
			#print("the widget could not be configured")

		try:
			self.bgc = kwargs['bg']
			self.label.config(bg=self.bgc)
		except:
			pass
			#print("the widget background color could not be changed")


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.picture = Image.open(os.path.join(self.script_dir, self.path))
		self.image = ImageTk.PhotoImage(self.picture)

		self.label = Label(self.parent, image=self.image)
		self.label.grid(row=self.row, column=self.column)


	def getData(self):
		return self.path


	def setData(self, data):
		if data == '': return
		self.config(path=data)