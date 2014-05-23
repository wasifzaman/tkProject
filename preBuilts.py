from labelWidgets2 import *
from tableWidget2 import *
from photoWidget2 import *
from tableWidget2 import *
from languages import *

language = languages["english"]

#duplicates of these widgets cannot exist if duplicates are desired, they have to be created by user


#strings
firstName = Textbox(text=language["First Name"], repr='firstName')
lastName = Textbox(text=language["Last Name"], repr='lastName')
chineseName = Textbox(text=language["Chinese Name"], repr='chineseName')
schoolLoc = Textbox(text=language["School Location"], repr='schoolLoc')
bCode = Textbox(text=language["Barcode"], repr='bCode')
gender = Textbox(text=language["Gender"], repr='gender')
parentName = Textbox(text=language["Parent Name"], repr='parentName')
pup = Textbox(text=language["Pick up Person"], repr='pup')
addr = Textbox(text=language["Address"], repr='addr')
state = Textbox(text=language["State"], repr='state')
city = Textbox(text=language["City"], repr='city')
wkdwknd = Textbox(text=language["Weekday/Weekend"], repr='wkdwknd')
email = Textbox(text=language["E-mail"], repr='email')
sType = Textbox(text=language["Service Type"], repr='sType')
cAwarded = Textbox(text=language["Classes Awarded"], repr='cAwarded')
cRemaining = Textbox(text=language["Classes Remaining"], repr='cRemaining')


#integers
age = IntTextbox(text=language["Age"], repr='age')
sid = IntTextbox(text=language["Old Student ID"], repr='sid')
hPhone = IntTextbox(text=language["Home Phone"], repr='hPhone')
cPhone = IntTextbox(text=language["Cell Phone"], repr='cPhone')
cPhone2 = IntTextbox(text=language["Cell Phone 2"], repr='cPhone2')
zip = IntTextbox(text=language["Zipcode"], repr='zip')


#date
dob = Datebox(text=language["Date of Birth"], repr='dob')
tpd = Datebox(text=language["Tuition Paid Day"], repr='tpd')


#money
tpa = MoneyTextbox(text=language["Tuition Pay Amount"], repr='tpa')


#attendance table
attinfo = Table(repr='attinfo', edit=True)
attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
attinfo.build(headers=attinfoh, data=[[]])


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
portr = Photo(repr='portr', path='C:\\Users\\Wasif\\Documents\\GitHub\\tkProject\\monet_sm.jpg')


#separator
sepr = Separator(repr='sepr')


#scan
sby = Picker(repr='sby', text='Search By', rads=[('Barcode', 'bcode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')])


#spicker
def cpicker():

	def sel():
		t.destroy()
		return b.get()

	t = Toplevel()
	frame = Frame(t)
	frame.pack()

	rads = [('Gold', 60, 'This awards the student 60 classes.'), ('Basic', 15, 'This awrards the student 15 classes.')]
	b, r = StringVar(), []
	b.set(rads[0][0])

	for rad in rads:
		rb = Radiobutton(frame, text=rad[0], variable=b, value=rad[1], indicatoron=0)
		rb.bind('<Button-1>', lambda event, r=rad[2]: info.config(text=r))
		r.append(rb)

	rads = r


	for rad in rads:
		rad.pack()

	info = Label(frame)
	info.pack()

	Button(frame, text='sel', command=sel).pack()


#longtexts
findSchool = LongTextbox(text=language["How did you hear about the school?"], repr='findSchool')
notes = LongTextbox(text=language["Notes"], repr='notes')