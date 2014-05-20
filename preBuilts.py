from labelWidgets2 import *
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
attinfo.build(headers=[language['Date'], language['Check-In Time'], language['Class Time']], data=[[]])




