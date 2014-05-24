from uiHandler2 import *

class Mbox(Window):

	def __init__(self, title='', geometry='300x200'):
		self.root = Toplevel()
		self.root.resizable(0, 0)
		self.root.grab_set()
		self.root.focus_set()

		self.root.protocol('WM_DELETE_WINDOW', self.dw)

		self.root.overrideredirect(1)

		#self.root.attributes('-fullscreen', True)

		#root options
		#self.root.option_add("*Font", "")
		self.root.option_add("*Background", "grey")
		self.root.option_add("*Foreground", "white")

		w = self.root.winfo_screenwidth()
		h = self.root.winfo_screenheight()

		
		print(w, h)

		g = geometry.split('x')

		w, h = w//2 - int(g[0]), h//2 - int(g[1])
		print(g)



		self.root.title(title)
		self.root.geometry(geometry + '+' + str(w) + '+' + str(h))
		self.root.config(bg="#9FB6CD")

		self.mainFrame = Frame(self.root)
		self.mainFrame.pack(fill=Y, expand=1, anchor=S)


		#frames
		self.frames = {}
		self.framePadding = (20, 10)


		#self.widgets = {}

	def dw(self):
		self.root.option_add("*Foreground", "black")
		self.root.destroy()