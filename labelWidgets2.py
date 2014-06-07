from tkinter import *
from widget import Widget
import inspect
from tkinter.scrolledtext import ScrolledText
from datetime import time, date, datetime


class Textbox(Widget):

	def __init__(self, **kwargs):
		try:			
			self.text = kwargs['text']
			self.repr = kwargs['repr']
			self.lang = kwargs['lang']
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
			pass
			#print("the widget could not be configured")

		try:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		except:
			pass


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

		#self.textvar = StringVar()
		#self.textvar.set(self.text)
		self.label = Label(self.parent, text=self.lang[self.text], width=20, anchor=E)
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


	def hide(self):
		self.label.grid_forget()
		self.entry.grid_forget()


class IntTextbox(Textbox):

	#helpers
	def OnValidate(self, d, i, P, s, S, v, V, W):
		try:
			int(S)
			return True
		except ValueError:
			return False
		return False


	def getData(self):
		e = self.entry.get()
		if e == '': return 0
		try:
			return int(e)
		except:
			return 0

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
			pass
			#print("the widget could not be configured")

		try:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		except:
			pass


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.selfframe = Frame(self.parent)
		self.label = Label(self.parent, text=self.text, width=20, anchor=E)
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
			print(self.getData())
			return S == '.' and '.' not in self.entry.get()# or False
		return False


	#def config(self, **kwargs):
		#return


	def getData(self):
		e = self.entry.get()
		if e == '': return 0.00
		try:
			return float(e)
		except:
			return 0.00


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


	def config(self, **kwargs):
		pass


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


	def config(self, **kwargs):

		try:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
			i = 0
			for rad in self.brads:
				rad.config(text=self.lang[self.rads[i][0]])
				i += 1
		except:
			pass


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.selfframe = Frame(self.parent)
		self.label = Label(self.selfframe, text=self.text)
		self.entry = Entry(self.selfframe, relief=GROOVE)

		self.b, r = StringVar(), []
		self.b.set(self.rads[0][1])
		for rad in self.rads:
			r.append(Radiobutton(self.selfframe, text=rad[0], variable=self.b, \
				value=rad[1], indicatoron=0, width=15))

		self.brads = r

		self.selfframe.grid()
		self.label.pack()
		self.entry.pack()
		for rad in self.brads:
			rad.pack(side=LEFT, padx=2)


	def getData(self):
		return self.b.get(), self.entry.get()


class LongTextbox(Textbox):

	def config(self, **kwargs):

		try:
			self.sentry.config(height=kwargs['height'])
		except:
			pass
			#print("the widget could not be configured")

		try:
			self.sentry.config(width=kwargs['width'])
		except:
			pass
			#print("the widget could not be configured")

		try:
			#self.text = kwargs['text']
			#self.sentry.delete(1.0, END)
			self.sentry.insert(END, kwargs['text'])
		except:
			pass
			#print("the widget could not be configured")
			
		try:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		except:
			pass


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.label = Label(self.parent, text=self.lang[self.text])
		self.sentry = ScrolledText(self.parent, relief=GROOVE)

		self.label.grid(row=self.row, column=self.column)
		self.sentry.grid(row=self.row, column=self.column+1, sticky=W+E, columnspan=100)


	def getData(self):
		return self.sentry.get('1.0', END + '-1c')


	def setData(self, data):
		self.sentry.delete('1.0', END)
		self.config(text=data)

	#def setData(self, data):
		#self.sentry.delete('1.0', END)
		#self.sentry.insert(END, self.text)
		#self.config(text=data)


class Labelbox(Textbox):

	def config(self, **kwargs):

		try:
			self.text=kwargs['text']
			self.label.config(text=self.text)
		except:
			pass

		try:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		except:
			pass


	def getData(self):
		return self.text


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.label = Label(self.parent, text=self.lang[self.text])
		self.label.grid(row=self.row, column=self.column)


	def hide(self):
		self.label.grid_forget()


	def show(self):
		self.label.grid()


class Buttonbox(Textbox):

	def __init__(self, **kwargs):
		try:			
			self.text = kwargs['text']
			self.repr = kwargs['repr']
			self.lang = kwargs['lang']
		except:
			print("widget could not be loaded")

		self.width = 30


	def config(self, **kwargs):

		try:
			self.lang = kwargs['lang']
			self.button.config(text=self.lang[self.text])
		except:
			pass

		try:
			self.cmd = kwargs['cmd']
			self.button.config(command=self.cmd)
		except:
			pass


	def setData(self, data):
		self.config(text=data)


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.button = Button(self.parent, text=self.lang[self.text], width=self.width)
		self.button.bind('<Enter>', self.config(bg='blue'))
		self.button.grid(row=self.row, column=self.column)


class Buttonbox2(Textbox):

	def __init__(self, **kwargs):
		try:
			self.text = kwargs['text']
			self.repr = kwargs['repr']
			self.lang = kwargs['lang']
		except:
			print("widget could not be loaded")

		self.width = 30


	def config(self, **kwargs):
		
		try:
			self.lang = kwargs['lang']
			self.button.config(text=self.lang[self.text])
		except:
			pass

		try:
			self.cmd = kwargs['cmd']
			self.args = inspect.getargspec(kwargs['cmd']).args
			#print(inspect.getargspec(kwargs['cmd']).args)
			if len(self.args) > 0 and self.args[0] != 'self':
				self.button.bind('<ButtonRelease-1>', self.cmd)	
			else:
				self.button.bind('<ButtonRelease-1>', lambda e: self.cmd())
		except:
			pass


	def enter(self, event):

		try:
			self.button.config(bg='#5C85FF', fg='white')
			self.selfframe.config(bg='#195CBF')
		except:
			pass


	def leave(self, event):

		try:
			self.button.config(bg='white', fg='black')
			self.selfframe.config(bg='#CCE0FF')
		except:
			pass


	def setData(self, data):
		self.config(text=data)


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.selfframe = Frame(self.parent, bg='#CCE0FF', bd=1)
		self.button = Label(self.selfframe, text=self.lang[self.text], width=self.width, bg='white', \
			font=('Verdana', 11), pady=10)

		self.button.bind('<Enter>', self.enter)
		self.button.bind('<Leave>', self.leave)

		self.selfframe.grid(row=self.row, column=self.column, pady=2)
		self.button.pack()