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


	def config(self, **kwargs):

		try:
			self.path = kwargs['path']
			picture = Image.open(self.path)
			self.image = ImageTk.PhotoImage(picture)
			self.label.config(image=self.image)
		except:
			print("the widget could not be configured")


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		picture = Image.open(self.path)
		self.image = ImageTk.PhotoImage(picture)

		self.label = Label(self.parent, image=self.image)
		self.label.grid(row=self.row, column=self.column)


	def getData(self):
		return self.path


	def setData(self, data):
		self.config(path=data)