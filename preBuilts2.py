from labelWidgets2 import *
from tableWidget2 import *
from photoWidget2 import *
from languages import *
from mbox2 import *
from tkinter import filedialog

language = languages["english"]

#duplicates of these widgets cannot exist if duplicates are desired, they have to be created by user


#strings
firstName = Textbox(text="First Name", lang=language, repr='firstName')
lastName = Textbox(text="Last Name", lang=language, repr='lastName')
chineseName = Textbox(text="Chinese Name", lang=language, repr='chineseName')
schoolLoc = Textbox(text="School Location", lang=language, repr='schoolLoc')
bCode = Textbox(text="Barcode", lang=language, repr='bCode')
gender = Textbox(text="Gender", lang=language, repr='gender')
parentName = Textbox(text="Parent Name", lang=language, repr='parentName')
pup = Textbox(text="Pick up Person", lang=language, repr='pup')
addr = Textbox(text="Address", lang=language, repr='addr')
state = Textbox(text="State", lang=language, repr='state')
city = Textbox(text="City", lang=language, repr='city')
wkdwknd = Textbox(text="Weekday/Weekend", lang=language, repr='wkdwknd')
email = Textbox(text="E-mail", lang=language, repr='email')
sType = Textbox(text="Service Type", lang=language, repr='sType')


#integers
age = IntTextbox(text="Age", lang=language, repr='age')
sid = IntTextbox(text="Old Student ID", lang=language, repr='sid')
hPhone = IntTextbox(text="Home Phone", lang=language, repr='hPhone')
cPhone = IntTextbox(text="Cell Phone", lang=language, repr='cPhone')
cPhone2 = IntTextbox(text="Cell Phone 2", lang=language, repr='cPhone2')
zip = IntTextbox(text="Zipcode", lang=language, repr='zip')
cAwarded = IntTextbox(text="Classes Awarded", lang=language, repr='cAwarded')
cRemaining = IntTextbox(text="Classes Remaining", lang=language, repr='cRemaining')


#date
dob = Datebox(text="Date of Birth", lang=language, repr='dob')
tpd = Datebox(text="Tuition Paid Day", lang=language, repr='tpd')


#money
tpa = MoneyTextbox(text="Tuition Pay Amount", lang=language, repr='tpa')


#attendance table
attinfo = Table(repr='attinfo', edit=True)
attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
attinfo.build(headers=attinfoh, data=[[]])
attinfo.clast = '#FF99FF'


#student table
stable = Table(repr='stable', edit=False)
stableh = [language['Barcode'], language['First Name'], language['Last Name'], language['Chinese Name'], language['Date of Birth']]
stable.build(headers=stableh, data=[[]])
def sbind(f):
	def fsb(p):
		i = stable.data[p[0]-1][0]
		try:
			f(i)
		except:
			print(stable.data[p[0]-1][0])

	try:
		for pos, cell in stable.cells.items():
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))
	except:
		print("cells could not be bound")



#photo
portr = Photo(repr='portr', path='monet_sm.jpg')

#separator
sepr = Separator(repr='sepr')


#scan
sby = Picker(repr='sby', text='Search By', rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')])


#spicker
def spicker(d):

	def sets(i):
		stable.s = i
		t.destroy()

	t = Toplevel()
	frame = Frame(t)
	frame.pack()

	stable.build(headers=stableh, data=d)
	stable.place(parent=frame, row=0, column=0)

	sbind(lambda i: sets(i=i))

	t.wait_window()

	#return s
	return stable.s


#spicker
def cward():

	def sel():
		t.destroy()
		t.cancel = False

	t = Toplevel()
	t.grab_set()
	t.focus_set()
	t.cancel = True

	frame = Frame(t)
	frame.grid()

	rads = [('Gold', 60, 'This awards the student 60 classes.'), ('Basic', 15, 'This awrards the student 15 classes.')]
	b, r = StringVar(), []
	b.set(rads[0][1])

	info = Label(frame, text=rads[0][2])
	info.grid()


	for rad in rads:
		rb = Radiobutton(frame, text=rad[0], variable=b, value=rad[1], indicatoron=0, width=20)
		rb.bind('<Button-1>', lambda event, r=rad[2]: info.config(text=r))
		r.append(rb)

	rads = r

	#self.protocol('WM_DELETE_WINDOW', t.destroy())


	for rad in rads:
		rad.grid()

	bac = Buttonbox(text='awardclass', lang=language, repr='bac')
	bac.place(parent=frame, row=4, column=0)
	bac.config(cmd=sel)

	t.wait_window()

	return 0 if t.cancel else int(b.get())

def sstype():
	if cAwarded.getData() >= 60:
		sType.setData('Gold')
	else:
		sType.setData('Basic')

def cpicker():
	cAwarded.setData(cward())
	cRemaining.setData(cAwarded.getData())
	sstype()

def cadd():
	cAwarded.setData(cAwarded.getData() + cward())
	cRemaining.setData(cAwarded.getData())
	sstype()

def caddone():
	cAwarded.setData(cAwarded.getData() + 1)
	cRemaining.setData(cAwarded.getData())
	sstype()


#longtexts
findSchool = LongTextbox(text="How did you hear about the school?", lang=language, repr='findSchool')
notes = LongTextbox(text="Notes", lang=language, repr='notes')


#ppicker
def ppicker():
	p = filedialog.askopenfile().name
	portr.config(path=p)


#signs
ws = Photo(repr='portr', path='C:\\Users\\Wasif\\Documents\\GitHub\\tkProject\\ws_sm.png')
hs = Photo(repr='portr', path='C:\\Users\\Wasif\\Documents\\GitHub\\tkProject\\hand_cursor_sm.png')
cm = Photo(repr='portr', path='C:\\Users\\Wasif\\Documents\\GitHub\\tkProject\\check_mark_sm.png')

nostext = Labelbox(text='No student', lang=language, repr='nostext')
context = Labelbox(text='Con student', lang=language, repr='context')
asetext = Labelbox(text='Ase student', lang=language, repr='asetext')
satext = Labelbox(text='Sa student', lang=language, repr='satext')
cstext = Labelbox(text='Cs student', lang=language, repr='cstext')

bok = Buttonbox(text='ok', lang=language, repr='bok')
byes = Buttonbox(text='yes', lang=language, repr='byes')
bno = Buttonbox(text='no', lang=language, repr='bno')


#importexp
imp = Labelbox(text='impdb', lang=language, repr='imp')
impt = Labelbox(text='impt', lang=language, repr='impt')
exp = Labelbox(text='expdb', lang=language, repr='exp')
curfile = Labelbox(text='curfile', lang=language, repr='curfile')
curdbs = Labelbox(text='', lang=language, repr='curdb')
saveto = Labelbox(text='saveto', lang=language, repr='saveto')

bimp = Buttonbox(text='impxls', lang=language, repr='bimp')
bimpt = Buttonbox(text='imptxls', lang=language, repr='bimpt')
bexp = Buttonbox(text='expxls', lang=language, repr='bexp')
bsav = Buttonbox(text='save', lang=language, repr='bsav')
bcdb = Buttonbox(text='choosedb', lang=language, repr='bcdb')

bk = Buttonbox(text='back', lang=language, repr='bk')
nxt = Buttonbox(text='next', lang=language, repr='bimp')


#browsebtn
brw = Buttonbox(text='browse', lang=language, repr='brw')
fpath = Textbox(text='filepath', lang=language, repr='fpath')
brw2 = Buttonbox(text='browse', lang=language, repr='brw2')
fpath2 = Textbox(text='filepath', lang=language, repr='fpath2')
brwp = Buttonbox(text='browsephoto', lang=language, repr='brwp')


#ebox
def nos():

	t = Mbox(geometry='230x200')
	
	t.newFrame("First Frame", (0, 0))

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["First Frame"].addWidget(bok, (2, 0))


	nostext.label.config(bg='grey', fg='white')
	bok.button.config(bg='grey', fg='white')
	bok.config(cmd=t.dw)
	t.config(bg='grey')

	t.root.wait_window()

def con(s):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox(geometry='230x310')

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(context, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	Label(t.frames["First Frame"], text=s, bg='grey', fg='white').grid()

	context.label.config(bg='grey', fg='white')
	byes.button.config(bg='grey', fg='white')
	bno.button.config(bg='grey', fg='white')
	byes.button.grid(sticky=E+W, padx=5)
	bno.button.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True))
	bno.config(cmd=lambda: d(False))
	t.config(bg='grey')

	t.root.wait_window()

	return t.z

def ase(s):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox(geometry='330x290')

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(asetext, (2, 0))

	Label(t.frames["First Frame"], text=s, bg='grey', fg='white').grid()

	asetext.label.config(bg='grey', fg='white')
	byes.button.config(bg='grey', fg='white')
	bno.button.config(bg='grey', fg='white')
	byes.button.grid(sticky=E+W, padx=5)
	bno.button.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True))
	bno.config(cmd=lambda: d(False))
	t.config(bg='grey')

	t.root.wait_window()

	return t.z


def sa(s):


	t = Mbox(geometry='280x230')

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	t.frames["First Frame"].addWidget(cm, (0, 0))
	t.frames["First Frame"].addWidget(bok, (4, 0))

	Label(t.frames["First Frame"], text=s, bg='grey', fg='white').grid(row=3)
	
	t.frames["First Frame"].addWidget(satext, (2, 0))

	satext.label.config(bg='grey', fg='white')
	bok.button.config(bg='grey', fg='white')
	bok.config(cmd=t.dw)
	t.config(bg='grey')

	t.root.wait_window()


def cs(s):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox(geometry='230x310')

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	Label(t.frames["First Frame"], text=s, bg='grey', fg='white').grid()

	cstext.label.config(bg='grey', fg='white')
	byes.button.config(bg='grey', fg='white')
	bno.button.config(bg='grey', fg='white')
	byes.button.grid(sticky=E+W, padx=5)
	bno.button.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True))
	bno.config(cmd=lambda: d(False))
	t.config(bg='grey')

	t.root.wait_window()

	return t.z


#clang
def clang():
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=language)


#bclang
bclang = Buttonbox(text='changelanguage', lang=language, repr='bclang')