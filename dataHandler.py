from datetime import datetime, time
from settingsHandler import *
import pickle

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
            "attinfo": []
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

    def __init__(self, studentList={}):
        self.studentList = studentList


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


    def pickleData(self, filename):
        pickle.dump(self.studentList, open(filename, "wb"))


    def unpickleData(self, filename):
        self.studentList = pickle.load(open(filename, "rb"))


    def export(self, filename):
        #to excel file
        return


    def saveData(self, filename, func=lambda:False):
        self.unpickleData(filename)
        func()
        self.pickleData(filename)
        self.unpickleData(filename)
        



#Pull settings.
#settings = Settings()

#file is unused
#file = settings.config["dbFile"]

#rybDB = StudentDB()


#s = StudentInfo()
#s.datapoints['barcode'] = '1234'

#d = StudentDB()
#d.addStudent(s.datapoints['barcode'], s)
#d.scanStudent('1234')
#d.scanStudent('1234')

#print(d.checkDate('1234'))
#print(d.studentList['1234'].datapoints['attinfo'])
#print(['05/20/2014', '02:21', '02:30'][0])