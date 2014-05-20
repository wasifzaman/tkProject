from tkinter import Label
from widget import Widget
from PIL import Image, ImageTk


class Photo(Widget):

	def __init__(self, **kwargs):

		try:
			self.repr = kwargs['repr']
		except:
			print("widget could not be loaded")


	def config(self, **kwargs):

		try:
			self.path = kwargs['path']
			picture = Image.open(path)
			self.image = ImageTk.PhotoImage()
		except:
			print("the widget could not be configured")