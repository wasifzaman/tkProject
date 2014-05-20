from tkinter import *
from tkinter import messagebox
from widget import Widget




class Cell(Widget):

	def __init__(self, **kwargs):

		try:
			self.text = kwargs['text']
			self.pos = kwargs['pos']
		except:
			print("widget could not be loaded")
		
		self.bgcolor = 'white'
		self.bd = 1
		self.relief = SUNKEN

	
	def config(self, **kwargs):
		
		try:
			self.label.config(width=kwargs['width'])
		except:
			pass
			#print("the widget could not be config")

		try:
			self.label.config(text=kwargs['text'])
		except:
			pass
			#print("the widget could not be configured")

		try:
			btn = kwargs['bind'][0]
			cmd = kwargs['bind'][1]
			#print(btn, cmd)
			self.label.bind(btn, cmd)
		except:
			pass
			#print("the widget could not be configured")


	def getData(self):
		return self.label.cget('text')


	def trytoplace(self, **kwargs):

		self.parent = kwargs['parent']
			

	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")
		
		self.label = Label(self.parent, text=self.text, relief=self.relief, bd=self.bd, bg=self.bgcolor)

		self.label.grid(row=self.pos[0], column=self.pos[1])


	def delete(self, **kwargs):

		try:
			self.label.destroy()
		except:
			print("widget could not be deleted")


class Table(Widget):

	#remove attribute in final version
	def __init__(self, **kwargs):

		try:
			self.repr = kwargs['repr']
			self.editwidget = kwargs['edit']
		except:
			print("widget could not be loaded")

		'''self.data = data
		self.parent = parent
		self.headers = headers
		self.rowNumbers = rowNumbers
		self.cellpadding = 2
		self.cells = []

		self.setData(self.data)
		

		#temp variables
		self.canvasWidth = w
		self.canvasHeight = h
		self.attribute = attribute
		self.current = 0'''

	def edit(self, pos):

		if not self.editwidget: return

		#skip if headers or numbers
		if pos[0] == 0 or pos[1] == 0: return

		def kill(event):
			self.data[pos[0]-1][pos[1]-1] = self.temp.get()
			self.update(data=self.data, headers=self.headers)
			self.temp.destroy()

		t = StringVar()
		t.set(self.cells[pos].getData())

		self.temp = Entry(self.innerframe, textvariable=t, width=self.cwids[pos[1]])
		self.temp.grid(row=pos[0], column=pos[1])
		self.temp.focus_set()
		self.temp.grab_set()
		self.temp.bind("<Return>", kill)
		#print(pos)


	def trytoplace(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.container = Frame(self.parent)
		self.canvas = Canvas(self.container)
		self.outerframe = Frame(self.canvas)
		self.innerframe = Frame(self.outerframe)		

		self.xscrollbar = Scrollbar(self.container, orient="horizontal", command=self.canvas.xview)
		self.yscrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
		self.canvas.config(xscrollcommand=self.xscrollbar.set)
		self.canvas.config(yscrollcommand=self.yscrollbar.set)


	def build(self, **kwargs):

		self.headers = kwargs['headers']
		self.data = kwargs['data']
		self.cells = {}

		r, l = 1, 0
		for row in self.data:
			c = 1
			for data in row:
				self.cells[(r, c)] = Cell(text=data, pos=(r, c))
				c += 1
			r += 1
			l = max(l, len(row))

		self.headers = self.headers[:l]

		tr, r, c = r, 1, 0
		for n in range(1, tr):
			self.cells[(r, c)] = Cell(text=str(n), pos=(r, c))
			r += 1

		r, c = 0, 1
		for data in self.headers:
			self.cells[(r, c)] = Cell(text=data, pos=(r, c))
			c += 1


	def intersect(self, newdata, olddata):

		cross = {}
		deprecated = {}
		
		r = 0
		for row in olddata:
			c = 0
			for data in row:
				try:
					newdata[r][c] != data
					cross[(r+1, c+1)] = data
				except:
					deprecated[(r+1, c+1)] = data
				c += 1
			r += 1

		return cross, deprecated


	def update(self, **kwargs):

		self.previous = self.data
		self.previouscells = self.cells
		self.previousheaders = self.headers

		self.build(data=kwargs['data'], headers=kwargs['headers'])

		cross, deprecated = self.intersect(self.data, self.previous)
		hcross, hdeprecated = self.intersect(self.headers, self.previousheaders)

		for cell in hdeprecated:
			self.previouscells[(0, cell[0])].delete()

		for cell in deprecated:
			self.previouscells[cell].delete()

		for key, value in cross.items():
			self.previouscells[key].config(text=self.data[key[0]-1][key[1]-1])

		for key, value in hcross.items():
			self.previouscells[(0, key[0])].config(text=self.headers[key[0]-1])

		for n in range(len(self.data), len(self.previous)):
			self.previouscells[(n+1, 0)].delete()

		for pos, cell in self.cells.items():
			#merge previous cells with new cells
			if pos in cross:
				self.cells[pos] = self.previouscells[pos]

		try:
			for pos, cell in self.cells.items():
				if pos not in cross:
					cell.place(parent=self.innerframe, pos=cell.pos)
		except:
			print("cells could not be placed")

		try:
			for pos, cell in self.cells.items():
				cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: self.edit(pos)))
			#print("bound")
		except:
			print("cells cannot be edited")

		self.resize()


	def resize(self):

		try:
			self.cwids = {}
			for cell in self.cells:
				self.cwids[cell[1]] = 0

			#0 corresponds to the numbers column
			self.cwids[0] = 4
		except:
			print("cells could not be resized")

		for key, value in self.cells.items():
			self.cwids[key[1]] = max(self.cwids[key[1]], len(value.getData()))
		
		#print(self.cwids)
		for key, value in self.cells.items():
			value.config(width=self.cwids[key[1]])


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		def makeScroll(event):
			self.canvas.config(scrollregion=self.canvas.bbox("all"))
			self.xscrollbar.pack(side=BOTTOM, fill=X)
			self.canvas.pack(side=LEFT)			
			self.yscrollbar.pack(side=RIGHT, fill=Y)

		try:
			for cell in self.cells.values():
				cell.place(parent=self.innerframe, pos=cell.pos)
		except:
			print("cells could not be placed")

		self.container.grid()
		self.innerframe.grid(row=0, column=0)
		self.canvas.create_window((0,0), window=self.outerframe, anchor=NW)
		self.parent.bind("<Configure>", makeScroll)
		self.resize()

		#try:
		#	for cell in self.cells.values():
		#		cell.config(bind=('<Double-Button-1>', self.edit))
		#	print("bound")
		#except:
		#	print("cells cannot be edited")



	def getData(self):
		return self.headers, self.data


	def setData(self, data):
		headers = data[0]
		information = data[1]

		self.update(headers=headers, data=information)




	'''def setwidth(self):


	''''''
	def place(self):

		try:
			self.trytoplace(self, **kwargs)
		except:
			print("widget could not be placed")

		self.make()
		self.outerframe.grid(row=0, column=0)
		self.innerframe.grid(row=1, column=1)

		self.canvas.create_window((0,0), window=self.masterFrame, anchor=NW)


		
		

		for i in range(self.maxrows):
			r = []
			for j in range(self.maxcols):
				try:
					cell = Cell(self.inner, self.data[i][j], (i, j), self.colwidth[j])
					r.append(cell)
					cell.label.bind("<Double-Button-1>", lambda event, row=i: self.editRow(row))
					cell.label.bind("<Button-1>", lambda event, row=i: self.select(row))
				except:
					cell = Cell(self.inner, '', (i, j), self.colwidth[j])
					r.append(cell)
					cell.label.bind("<Double-Button-1>", lambda event, row=i: self.editRow(row))
					cell.label.bind("<Button-1>", lambda event, row=i: self.select(row))

			self.cells.append(r)




		if self.headers:
			while len(self.headers) < self.maxcols:
				self.headers.append("Col " + str(len(self.headers)))

			for i in range(len(self.headers)):
				if i not in self.colwidth: continue
				Label(self.headerFrame, text=self.headers[i], bd=1, relief=SUNKEN, width=self.colwidth[i], bg="#5983D6", fg="white").grid(row=0, column=i)

		if self.rowNumbers:
			for i in range(self.maxrows):
				Label(self.numberFrame, text=i+1, bd=1, relief=SUNKEN, bg="#5983D6", fg="white", width=3).grid(row=i, column=0)


		self.parent.bind("<Configure>", self.makeScroll)

		
				

	def makeScroll(self, event):
		#width, height defined by func, determine by max width
		self.canvas.config(scrollregion=self.canvas.bbox("all"), width=self.canvasWidth, height=self.canvasHeight)
		self.xscrollbar.pack(side=BOTTOM, fill=X)
		self.canvas.pack(side=LEFT)
		self.yscrollbar.pack(side=RIGHT, fill=Y)

	def getData(self):
		table = []
		empty = ['' for x in range(len(self.cells[0]))]
        
		for row in self.cells:
			r = []
			for cell in row:
				r.append(cell.label.cget('text').strip())

			if r != empty:
				table.append(r)

		return table

	def setData(self, data):
		self.data = data
		self.cells = []
		self.setTable()
		self.displayTable()

	def clearData(self):
		for row in self.cells:
			for cell in row:
				cell.label.destroy()
		self.cells = []

	def setTable(self):

		#set the table, cell widths, heights
		self.maxrows = len(self.data)
		self.maxcols = 0
		self.colwidth = {}
		
		for row in range(len(self.data)):
			self.maxcols = max(len(self.data[row]), self.maxcols)
			for col in range(len(self.data[row])):
				if col not in self.colwidth: self.colwidth[col] = 0
				
				if self.headers:
					#if header, compare header len
					self.colwidth[col] = max(len(self.data[row][col]),len(self.headers[col]), self.colwidth[col]-self.cellpadding)+self.cellpadding 
				self.colwidth[col] = max(len(self.data[row][col]), self.colwidth[col]-self.cellpadding)+self.cellpadding 

	def setRowColor(self, i, color):
		for cell in self.cells[i]:
			cell.label.config(bg=color)

	def editRow(self, i):
		
		def setCellData():
			for i in range(len(row)):
				row[i].label.config(text=entries[i].get())
			self.data = self.getData()
			#print(self.data)
			self.clearData()
			self.setData(self.data)
			top.destroy()

		def clearAllData():
			result = messagebox.askyesno("Clear?", "Clear all fields?")
			if not result: return

			for entry in entries:
				entry.delete(0, END)
            
            

		top = Toplevel()
		top.grab_set()

		cellFrame = Frame(top)
		buttonFrame = Frame(top)

		cellFrame.grid(row=0,column=0)
		buttonFrame.grid(row=1,column=0)

		row = self.cells[i]
		entries = []

        #place headers
		for i in range(len(self.headers)):
			Label(cellFrame, text=self.headers[i], width=self.colwidth[i]).grid(row=0, column=i, padx=10, pady=3)

		for j in range(len(row)):
			strCellData = StringVar()
			strCellData.set(row[j].label.cget('text'))
			entries.append(Entry(cellFrame, textvariable=strCellData, width=10))
			entries[-1].grid(row=1, column=j, padx=10, pady=4)

		entries[0].focus_set()
		Button(buttonFrame, text='Save', width=5, command=setCellData).grid(row=2, column=0, padx=5, pady=10)
		Button(buttonFrame, text='Clear All', width=8, command=clearAllData).grid(row=2, column=1, padx=5, pady=10)
		Button(buttonFrame, text='Cancel', width=8, command=top.destroy).grid(row=2, column=2, padx=5, pady=10)

	def bindCells(self, button, command):
		for row in self.cells:
			for cell in row:
				cell.label.bind(button, command)

	def select(self, row):
		for cell in self.cells[self.current]:
			cell.label.config(bg="white")
			
		for cell in self.cells[row]:
			cell.label.config(bg='#F0E0FF')

		self.current = row'''