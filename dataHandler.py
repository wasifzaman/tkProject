from datetime import datetime, time, timedelta
from settingsHandler import *
import pickle
import xlrd

#log all changes






#colorCode = {5: {time(10, 59): "#ff00ff",
#                 time(12, 29): "#9900ff",
#                 time(14, 29): "#073763",
#                 time(15, 59): "#0000ff",
#                 time(17, 29): "#4a86e8",
#                 time(23, 59): "#000000"},
#             
#             6: {time(10, 59): "#ff0000",
#                 time(12, 29): "#980000",
#                 time(14, 29): "#783f04",
#                 time(15, 59): "#274e13",
#                 time(17, 29): "#6aa84f",
#                 time(23, 59): "#000000"},
#
#             0: {time(23, 59): "#000000"},
#             1: {time(23, 59): "#000000"},
#             2: {time(23, 59): "#000000"},
#             3: {time(23, 59): "#000000"},
#             4: {time(23, 59): "#000000"}}
#
#sortedColorCode = {key: [t for t in value] for (key, value) in colorCode.items()}
#for v in sortedColorCode.values(): v.sort()




class StudentInfo(object):

    '''

    Class info: Handles information of students.

    student_attr:
        DICTIONARY of student attributes.
        Correlates to "fields".

    attendance:
        LIST of attendance dates and times.

    add_attendance():
        Appends to "attendance" as a 2D array,
        current date and time.

    '''

    def __init__(self):
        self.datapoints = {
            "lastName": '',
            "firstName": '',
            "chineseName": '',
            "schoolLoc": '',
            "bCode": '',
            "sid": 0,
            "dob": '1/1/1900',
            "age": 0,
            "gender": '',
            "parentName": '',
            "hPhone": 0,
            "cPhone": 0,
            "cPhone2": 0,
            "pup": '',
            "addr": '',
            "state": '',
            "city": '',
            "zip": 0,
            "wkdwknd": '',
            "tpd": '1/1/1900',
            "tpa": 0,
            "email": '',
            "sType": '',
            "cAwarded": 0,
            "cRemaining": 0,
            "findSchool": '',
            "notes": '',
            "attinfo": [],
            "portr": ''
            }

        self.dpalias = {
            "Last Name": "lastName",
            "First Name": "firstName",
            "Chinese Name": "chineseName",
            "School Location": "schoolLoc",
            "Barcode": "bCode",
            "Old Student ID": "sid",
            "Date of Birth": "dob",
            "Age": "age",
            "Gender": "gender",
            "Parent Name": "parentName",
            "Home Phone": "hPhone",
            "Cell Phone": "cPhone",
            "Cell Phone 2": "cPhone2",
            "Pick up Person": "pup",
            "Address": "addr",
            "State": "state",
            "City": "city",
            "Zipcode": "zip",
            "Weekday/Weekend": "wkdwknd",
            "Tuition Paid Day": "tpd",
            "Payment Method": "Payment Method: ",
            "Tuition Pay Amount": "tpa",
            "E-mail": "email",
            "Service Type": "sType",
            "Classes Awarded": "cAwarded",
            "Classes Remaining": "cRemaining",
            "How did you hear about the school?": "findSchool"
        }


class StudentDB(object):

    '''

    Class info: Handles student database.

    studentList:
        DICTIONARY item of students.
        Key = barcode
        Value = StudentInfo

    scan_student:
        Scans the students by calling the
        "add_attendance()" function of StudentInfo.

    add_student:
        Adds a new student to the "studentList".

        ##needs fix, should ask for confirmation in UI
        If the barcode already exists, it will
        overwrite the existing student.

    pickle_list:
        Pickles "studentList" for storage into a file.

    unpickle_list:
        Unpickles filename and stores it in "studentList".

    export:
        Exports the list into an Excel(xls) file.

    import:
        ##not implemented yet
        Imports an Excel (xls) file.

    '''

    def __init__(self, **kwargs):
        
        try:
            self.file = kwargs['file']
        except:
            print("file not found")

        self.studentList = {}

        try:
            self.loadData()
            print("database loaded")
        except:
            self.saveData()
            print("database could not be loaded, new database created")
        
        



    def checkDate(self, barcode):
        checkedInToday = 0

        today = '{:%m/%d/%Y}'.format(datetime.now())
        attinfo = self.studentList[barcode].datapoints['attinfo']

        for att in attinfo:
            print(att[0])
            if att[0] == today: checkedInToday += 1

        if checkedInToday > 0: return checkedInToday
        return True


    def findTimeSlot(self, time):
        h, m = '{:%H}'.format(time), '{:%M}'.format(time)
        m = int(m)

        if m > 40:
            m = '00'
        elif m > 10:
            m = '30'
        else:
            m = '00'

        return h + ':' + m


    def scanStudent(self, barcode):
        #try:
        cdt = datetime.now()

        timeslot = self.findTimeSlot(cdt)
        time = '{:%H:%M}'.format(cdt)
        date = '{:%m/%d/%Y}'.format(cdt)

        self.studentList[barcode].datapoints['attinfo'].append([date, time, timeslot])
        #except:
            #return print("Student doesn't exist")


    def addStudent(self, barcode, student):
        self.studentList[barcode] = student

    #def edit_student(self, barcode, student_attr):
        #self.studentList[barcode].student_attr = student_attr


    def saveData(self):
        pickle.dump(self.studentList, open(self.file, "wb"))


    def loadData(self):
        self.studentList = pickle.load(open(self.file, "rb"))


    def format(self, ctype, value):
        try:
            return self.fcell[ctype](value)
        except:
            print("cell could not be formatted")


    def exportxlsx(self, filename):
        #to excel file
        return


    def importxlsx(self, filename):

        self.fcell = {1: lambda y: str(y), 2: lambda y: int(y), 3: lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%y")}

        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)

        repr, headers = {}, [cell.value for cell in worksheet.row(0)]
        for h in headers:
            repr[headers.index(h)] = StudentInfo().dpalias[h]


        sraw = [worksheet.row(rx) for rx in range(1, worksheet.nrows)]
        sinfo = [[self.format(cell.ctype, cell.value) for cell in row] for row in sraw]

        for info in sinfo:
            newS = StudentInfo()
            for dp in info:
                newS.datapoints[repr[info.index(dp)]] = dp
            self.addStudent(newS.datapoints['bCode'], newS)


        #print(repr, headers, sinfo)

        self.saveData()

        return


    #def modData(self):
    #    self.loadData()
    #    self.saveData()
    #    self.loadData()
        



#Pull settings.
#settings = Settings()

#file is unused
#file = settings.config["dbFile"]

#rybDB = StudentDB()


#s = StudentInfo()
#s.datapoints['barcode'] = '1234'

#d = StudentDB(file='tdb.db')
#d.addStudent(s.datapoints['barcode'], s)
#d.scanStudent('1234')
#d.scanStudent('1234')

#print(d.checkDate('1234'))
#print(d.studentList['1234'].datapoints['attinfo'])
#print(['05/20/2014', '02:21', '02:30'][0])

#d.importxlsx('sdt.xls')

#date = datetime.strptime('1/1/1900', "%m/%d/%Y")
#edate = date + timedelta(days=38779-2)

#print(edate)

#print(d.studentList['FLU-000-002'].datapoints)
#x = {'1': lambda y: str(y), '2': lambda y: int(y), '3': lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%y")}

#print(x['3'](41653.0))
#print(datetime.strftime)
#print(d.studentList['FLU-000-006'].datapoints['firstName'])