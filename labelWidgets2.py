from tkinter import *
from widget import Widget
from tkinter.scrolledtext import ScrolledText
from datetime import time, date, datetime


class Textbox(Widget):

	def __init__(self, **kwargs):
		try:
			self.text = kwargs['text']
			self.repr = kwargs['repr']
		except:
			print("widget could not be loaded")

		self.height = 1
		self.width = 2

	def config(self, **kwargs):

		try:
			s = StringVar()
			s.set(kwargs['text'])
			self.entry.config(textvariable=s)
		except:
			print("the widget could not be configured")		


	#helpers
	def OnValidate(self, d, i, P, s, S, v, V, W):
		#all formats are allowed in textbox
		return True

	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.label = Label(self.parent, text=self.text)
		self.entry = Entry(self.parent, relief=GROOVE)

		self.label.grid(row=self.row, column=self.column)
		self.entry.grid(row=self.row, column=self.column+1)

		self.bind()


	def bind(self):
		vcmd = (self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=vcmd)


	def getData(self):
		return self.entry.get()


	def setData(self, data):
		self.config(text=data)


class IntTextbox(Textbox):

	#helpers
	def OnValidate(self, d, i, P, s, S, v, V, W):
		try:
			int(S)
			return True
		except ValueError:
			return False
		return False


	#def bind(self):
	#	vcmd = (self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
	#	self.entry.config(validate="all", validatecommand=vcmd)


class Datebox(IntTextbox):

	def config(self, **kwargs):

		try:
			m, d, y = StringVar(), StringVar(), StringVar()
			m.set(kwargs['m'])
			d.set(kwargs['d'])
			y.set(kwargs['y'])
			self.mEntry.config(textvariable=m)
			self.dEntry.config(textvariable=d)
			self.yEntry.config(textvariable=y)
		except:
			print("the widget could not be configured")


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.selfframe = Frame(self.parent)
		self.label = Label(self.parent, text=self.text)
		self.mLabel = Label(self.selfframe, text='MM')
		self.dLabel = Label(self.selfframe, text='DD')
		self.yLable = Label(self.selfframe, text='YY')

		self.mEntry = Entry(self.selfframe, relief=GROOVE, width=4)
		self.dEntry = Entry(self.selfframe, relief=GROOVE, width=4)
		self.yEntry = Entry(self.selfframe, relief=GROOVE, width=4)


		self.selfframe.grid(row=self.row, column=self.column+1)

		self.label.grid(row=self.row, column=self.column)
		self.mLabel.grid(row=0, column=1)
		self.dLabel.grid(row=0, column=2)
		self.yLable.grid(row=0, column=3)

		self.mEntry.grid(row=1, column=1)
		self.dEntry.grid(row=1, column=2)
		self.yEntry.grid(row=1, column=3)

		self.bind()


	def bind(self):
		vcmd = (self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.mEntry.config(validate="all", validatecommand=vcmd)
		self.dEntry.config(validate="all", validatecommand=vcmd)
		self.yEntry.config(validate="all", validatecommand=vcmd)


	def getData(self):
		return self.mEntry.get() + '/' + self.dEntry.get() + '/' + self.yEntry.get()


	def setData(self, data):
		date = data.split('/')
		m, d, y = date[0], date[1], date[2]

		self.config(m=m, d=d, y=y)


class MoneyTextbox(IntTextbox):

	#helpers
	def OnValidate(self, d, i, P, s, S, v, V, W):
		try:
			int(S)
			return True
		except ValueError:
			return S == '.' or False
		return False

	def config(self, **kwargs):
		return


class Separator(Widget):

	def __init__(self, **kwargs):
		try:
			self.repr = kwargs['repr']
		except:
			print("widget could not be loaded")

		#self.height = 2
		#self.bd = 1
		#self.relief = SUNKEN
		#self.sticky = W+E


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")


		self.fr = Frame(self.parent, height=2, bd=1, relief=SUNKEN)
		self.fr.grid(row=self.row, column=self.column, sticky=W+E, columnspan=100, pady=10)


class Picker(Textbox):

	def __init__(self, **kwargs):
		try:
			self.repr = kwargs['repr']
			self.text = kwargs['text']
			self.rads = kwargs['rads']
		except:
			print("widget could not be loaded")


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.selfframe = Frame(self.parent)
		self.label = Label(self.parent, text=self.text)
		self.entry = Entry(self.parent, relief=GROOVE)

		self.b, r = StringVar(), []
		self.b.set(self.rads[0][0])
		for rad in self.rads:
			r.append(Radiobutton(self.parent, text=rad[0], variable=self.b, value=rad[1], indicatoron=0))

		self.rads = r

		self.label.pack()
		self.entry.pack()
		for rad in self.rads:
			rad.pack(side=LEFT)


	def getData(self):
		return self.b.get(), self.entry.get()


class LongTextbox(Textbox):

	def config(self, **kwargs):

		try:
			self.sentry.config(height=kwargs['height'])
		except:
			pass
#			print("the widget could not be configured")

		try:
			self.sentry.config(width=kwargs['width'])
		except:
			pass
			#print("the widget could not be configured")

		try:
			self.sentry.delete(1.0, END)
			self.sentry.insert(END, kwargs['text'])
		except:
			pass
			#print("the widget could not be configured")		


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.label = Label(self.parent, text=self.text)
		self.sentry = ScrolledText(self.parent, relief=GROOVE)

		self.label.grid(row=self.row, column=self.column)
		self.sentry.grid(row=self.row, column=self.column+1, sticky=W+E, columnspan=100)


	def getData(self):
		return self.sentry.get(1.0, END)


	def setData(self, data):
		self.sentry.delete(1.0, END)
		self.sentry.insert(END, self.text)
#		self.config(text=data)