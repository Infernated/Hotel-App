import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from datetime import date
import sys
import calendar
import guestscalendar
import pandas as pd
from functools import partial

PyQt5.QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

class ShowCheckouts(QtWidgets.QWidget, QtCore.QDate):
    def __init__(self, but_text, roomslist):
        super().__init__()
        self.setGeometry(300, 280, 250, 300)
        self.setWindowTitle("Checkouts")
        self.but_text = but_text
        self.rooms_list = roomslist

        self.lab1 = QtWidgets.QLabel(self)
        self.lab2 = QtWidgets.QLabel(self)
        self.lab3 = QtWidgets.QLabel(self)
        self.lab4 = QtWidgets.QLabel(self)
        self.lab5 = QtWidgets.QLabel(self)
        self.lab6 = QtWidgets.QLabel(self)
        self.lab7 = QtWidgets.QLabel(self)
        self.lab8 = QtWidgets.QLabel(self)
        self.lab9 = QtWidgets.QLabel(self)
        self.lab10 = QtWidgets.QLabel(self)
        self.lab11 = QtWidgets.QLabel(self)
        self.lab12 = QtWidgets.QLabel(self)
        self.initlabels()


    def initlabels(self):
        labelslist = [
            self.lab2,
            self.lab3,
            self.lab4,
            self.lab5,
            self.lab6,
            self.lab7,
            self.lab8,
            self.lab9,
            self.lab10,
            self.lab11,
            self.lab12
        ]
        movey = 60
        for i in labelslist:
            i.move(70,movey)
            movey += 20

        if self.but_text == "Checkouts tomorrow: {0}".format(len(self.rooms_list)):
            self.lab1.move(40, 20)
            self.lab1.setText("Checkouts tomorrow:")
            self.lab1.setFont(QtGui.QFont('Calibri', 15))
            self.lab1.adjustSize()
        elif self.but_text == "Checkouts today: {0}".format(len(self.rooms_list)):
            self.lab1.move(60, 20)
            self.lab1.setText("Checkouts today:")
            self.lab1.setFont(QtGui.QFont('Calibri', 15))
            self.lab1.adjustSize()

        self.lab2.setText("Room Appartment")
        self.lab2.setFont(QtGui.QFont('Calibri', 12))
        self.lab2.adjustSize()

        self.lab3.setText("Room 2")
        self.lab3.setFont(QtGui.QFont('Calibri', 12))
        self.lab3.adjustSize()

        self.lab4.setText("Room 3")
        self.lab4.setFont(QtGui.QFont('Calibri', 12))
        self.lab4.adjustSize()

        self.lab5.setText("Room 4")
        self.lab5.setFont(QtGui.QFont('Calibri', 12))
        self.lab5.adjustSize()

        self.lab6.setText("Room 7")
        self.lab6.setFont(QtGui.QFont('Calibri', 12))
        self.lab6.adjustSize()

        self.lab7.setText("Room 8")
        self.lab7.setFont(QtGui.QFont('Calibri', 12))
        self.lab7.adjustSize()

        self.lab8.setText("Room 9")
        self.lab8.setFont(QtGui.QFont('Calibri', 12))
        self.lab8.adjustSize()

        self.lab9.setText("Room 10")
        self.lab9.setFont(QtGui.QFont('Calibri', 12))
        self.lab9.adjustSize()

        self.lab10.setText("Room 11")
        self.lab10.setFont(QtGui.QFont('Calibri', 12))
        self.lab10.adjustSize()

        self.lab11.setText("Room 12")
        self.lab11.setFont(QtGui.QFont('Calibri', 12))
        self.lab11.adjustSize()

        self.lab12.setText("Room 14")
        self.lab12.setFont(QtGui.QFont('Calibri', 12))
        self.lab12.adjustSize()

        for i in labelslist:
            i.hide()

        if self.but_text == "Checkouts today: 0" or self.but_text == "Checkouts tomorrow: 0":
            self.lab7.show()
            self.lab7.setText("No checkouts!")
            self.lab7.setFont(QtGui.QFont('Calibri', 20))
            self.lab7.setStyleSheet("color:red")
            self.lab7.move(45,150)
            self.lab7.adjustSize()

        for i in self.rooms_list:
            if i == "App":
                self.lab2.show()
            if i == "2":
                self.lab3.show()
            if i == "3":
                self.lab4.show()
            if i == "4":
                self.lab5.show()
            if i == "7":
                self.lab6.show()
            if i == "8":
                self.lab7.show()
            if i == "9":
                self.lab8.show()
            if i == "10":
                self.lab9.show()
            if i == "11":
                self.lab10.show()
            if i == "12":
                self.lab11.show()
            if i == "14":
                self.lab12.show()

class GuestAdding(QtWidgets.QWidget, QtCore.QDate):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 280, 700, 200)
        self.setWindowTitle("Add guest")

        self.lab1 = QtWidgets.QLabel(self)
        self.lab1.move(50, 150)
        self.lab2 = QtWidgets.QLabel(self)
        self.lab2.move(50, 170)

        self.bx_room = QtWidgets.QComboBox(self)
        self.bx_room.move(50, 50)
        self.bx_room.resize(60, 30)
        self.bx_room.addItems(["App", "2", "3", "4", "7", "8", "9", "10", "11", "12", "14"])

        self.bx_firstname = QtWidgets.QTextEdit(self)
        self.bx_firstname.move(150, 50)
        self.bx_firstname.resize(110, 30)

        self.bx_lastname = QtWidgets.QTextEdit(self)
        self.bx_lastname.move(280, 50)
        self.bx_lastname.resize(110, 30)

        self.date = QtCore.QDate(date.today())
        self.bx_date1 = QtWidgets.QDateEdit(self)
        self.bx_date1.move(400, 50)
        self.bx_date1.resize(90, 30)
        self.bx_date1.setDate(self.date)
        self.bx_date1.setCalendarPopup(True)

        self.bx_date2 = QtWidgets.QDateEdit(self)
        self.bx_date2.move(500, 50)
        self.bx_date2.resize(90, 30)
        self.bx_date2.setDate(self.date)
        self.bx_date2.setCalendarPopup(True)

        self.lab3 = QtWidgets.QLabel(self)
        self.lab3.move(50, 20)
        self.lab3.setText("Room:")
        self.lab3.setFont(QtGui.QFont('Calibri', 15))
        self.lab3.adjustSize()

        self.lab4 = QtWidgets.QLabel(self)
        self.lab4.move(150, 20)
        self.lab4.setText("First name:")
        self.lab4.setFont(QtGui.QFont('Calibri', 15))
        self.lab4.adjustSize()

        self.lab5 = QtWidgets.QLabel(self)
        self.lab5.move(280, 20)
        self.lab5.setText("Last name:")
        self.lab5.setFont(QtGui.QFont('Calibri', 15))
        self.lab5.adjustSize()

        self.lab6 = QtWidgets.QLabel(self)
        self.lab6.move(400, 20)
        self.lab6.setText("Checkin:")
        self.lab6.setFont(QtGui.QFont('Calibri', 15))
        self.lab6.adjustSize()

        self.lab7 = QtWidgets.QLabel(self)
        self.lab7.move(500, 20)
        self.lab7.setText("Checkout:")
        self.lab7.setFont(QtGui.QFont('Calibri', 15))
        self.lab7.adjustSize()

        self.b_quit = QtWidgets.QPushButton(self)
        self.b_quit.move(630, 140)
        self.b_quit.resize(50, 40)
        self.b_quit.setText("Quit")
        self.b_quit.clicked.connect(self.but_quit)

        self.b_save = QtWidgets.QPushButton(self)
        self.b_save.move(560, 140)
        self.b_save.resize(50, 40)
        self.b_save.setText("Save")
        self.b_save.clicked.connect(self.but_save)


    def but_quit(self):
        self.close()

    def but_save(self):
        self.qdatein = self.bx_date1.date()
        self.qdateout = self.bx_date2.date()
        self.firstname = str(self.bx_firstname.toPlainText())
        self.lastname = str(self.bx_lastname.toPlainText())
        self.checkinday = int(self.qdatein.day())
        self.checkinmonth = int(self.qdatein.month())
        self.checkinyear = int(self.qdatein.year())
        self.checkoutday = int(self.qdateout.day())
        self.checkoutmonth = int(self.qdateout.month())
        self.checkoutyear = int(self.qdateout.year())
        self.room = str(self.bx_room.currentText())

        error = 0

        if self.firstname == "" or self.lastname == "":
            error = 1
            self.lab2.setText("Hint: There's no input in first name or last name!")
            self.lab2.setFont(QtGui.QFont('Calibri', 15))
            self.lab2.setStyleSheet("QLabel {color : darkgreen}")
            self.lab2.adjustSize()

        for ind in self.firstname:
            if ind == " ":
                error = 1
                self.lab2.setText("Hint: There's spacebar in first name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()
            elif ind == "\t":
                error = 1
                self.lab2.setText("Hint: There's tab in first name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()
            elif ind == "\n":
                error = 1
                self.lab2.setText("Hint: There's enter in first name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()
        for i in self.lastname:
            if i == " ":
                error = 1
                self.lab2.setText("Hint: There's spacebar in last name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()
            elif i == "\t":
                error = 1
                self.lab2.setText("Hint: There's tab in last name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()
            elif i == "\n":
                error = 1
                self.lab2.setText("Hint: There's enter in last name!")
                self.lab2.setFont(QtGui.QFont('Calibri', 15))
                self.lab2.setStyleSheet("QLabel {color : darkgreen}")
                self.lab2.adjustSize()

        if error != 0:
            self.error_label()
        else:
            data = {
                'firstname': [self.firstname],
                'lastname': [self.lastname],
                'checkinday': [self.checkinday],
                'checkinmonth': [self.checkinmonth],
                'checkinyear': [self.checkinyear],
                'checkoutday': [self.checkoutday],
                'checkoutmonth': [self.checkoutmonth],
                'checkoutyear': [self.checkoutyear],
                'room': [self.room]
            }
            rawdata = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
            filename = "guestsdata/guests_{0}_{1}.csv".format(self.checkinmonth, self.checkinyear)
            data2 = pd.DataFrame(data, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                                'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
            filename2 = "guestsdata/guests_{0}_{1}.csv".format(self.checkinmonth, self.checkinyear)

            if (self.checkinmonth < self.checkoutmonth) and (self.checkinyear == self.checkoutyear):
                filename2 = "guestsdata/guests_{0}_{1}.csv".format(self.checkoutmonth, self.checkoutyear)
            elif (self.checkinmonth > self.checkoutmonth) and (self.checkinyear < self.checkoutyear):
                filename2 = "guestsdata/guests_{0}_{1}.csv".format(self.checkoutmonth, self.checkoutyear)

            try:
                inf = pd.read_csv(filename)
            except:
                rawdata.to_csv(filename, index=False)
                inf = pd.read_csv(filename)
            info = pd.DataFrame(inf, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                              'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

            index = 0

            try:
                inf2 = pd.read_csv(filename2)
            except:
                rawdata.to_csv(filename2,index=False)
                inf2 = pd.read_csv(filename2)
            info2 = pd.DataFrame(inf2, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                              'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

            lastnamelistsource = info['lastname']
            firstnamelistsource = info['firstname']
            cinds = info['checkinday']
            cinms = info['checkinmonth']
            cinys = info['checkinyear']
            cods = info['checkoutday']
            coms = info['checkoutmonth']
            coys = info['checkoutyear']
            roomsource = info['room']

            lastnamelistnew = data2['lastname']
            firstnamelistnew = data2['firstname']
            cindn = data2['checkinday']
            cinmn = data2['checkinmonth']
            cinyn = data2['checkinyear']
            codn = data2['checkoutday']
            comn = data2['checkoutmonth']
            coyn = data2['checkoutyear']
            roomnew = data2['room']

            guest_error = 0
            while index < len(info):
                if str(lastnamelistsource[index]) == str(lastnamelistnew[0]) \
                        and str(firstnamelistsource[index]) == str(firstnamelistnew[0]) \
                        and str(cinys[index]) == str(cinyn[0]) \
                        and str(cinms[index]) == str(cinmn[0]) \
                        and str(cinds[index]) == str(cindn[0]) \
                        and str(cods[index]) == str(codn[0]) \
                        and str(coms[index]) == str(comn[0]) \
                        and str(coys[index]) == str(coyn[0]) \
                        and str(roomsource[index]) == str(roomnew[0]):
                    guest_error = 1
                else:
                    pass
                index += 1
            if guest_error == 1:
                self.guest_already_assigned()
            elif guest_error == 0:
                df = pd.concat([info, data2])
                df.to_csv(filename, index=False)
                self.label_succes()
            if guest_error == 0 and filename != filename2:
                df = pd.concat([info2, data2])
                df.to_csv(filename2, index=False)
                self.label_succes()
    def get_date(self):
        self.qdatein = self.bx_date1.date()
        self.dateinstr = str('{0}.{1}.{2}'.format(self.qdatein.day(), self.qdatein.month(), self.qdatein.year()))

    def error_label(self):
        self.lab1.setText("Please enter correct name!")
        self.lab1.setFont(QtGui.QFont('Calibri', 15))
        self.lab1.setStyleSheet("QLabel {color : #c40202}")
        self.lab1.adjustSize()

    def guest_already_assigned(self):
        self.lab1.setText("Guest already assigned!")
        self.lab1.setFont(QtGui.QFont('Calibri', 15))
        self.lab1.setStyleSheet("QLabel {color : #c40202}")
        self.lab1.adjustSize()

    def label_succes(self):
        self.lab1.setText("Guest successfully booked in!")
        self.lab1.setFont(QtGui.QFont('Calibri', 15))
        self.lab1.setStyleSheet("QLabel {color : green}")
        self.lab1.adjustSize()
        self.lab2.close()
        self.bx_firstname.setPlainText("")
        self.bx_lastname.setPlainText("")

class MyWindow(QtWidgets.QMainWindow, QtWidgets.QLabel, QtGui.QFont):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 150, 700, 500)
        self.setWindowTitle("Hotel app")
        self.grid_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.grid_layout)
        self.win_gcal = guestscalendar.GuestsCalendar()
        self.win_gadd = GuestAdding()

    def main_menu(self):
        self.l_w = QtWidgets.QLabel(self)
        self.l_w.move(170,80)
        self.l_w.setFont(QtGui.QFont('Calibri', 30))
        self.l_w.setText("Welcome to the hotel")
        self.l_w.adjustSize()

        self.l_w_desc = QtWidgets.QLabel(self)
        self.l_w_desc.setFont(QtGui.QFont('Calibri', 15))
        self.l_w_desc.move(240,160)
        self.l_w_desc.setStyleSheet("QLabel {color : #a3a3a3}")
        self.l_w_desc.setText("What do you want to do?")
        self.l_w_desc.adjustSize()

    def show_calendar(self, checked):
        if self.win_gcal.isVisible():
            self.win_gcal.hide()
        else:
            self.win_gcal.show()

    def add_guest(self):
        if self.win_gadd.isVisible():
            self.win_gadd.hide()

        else:
            self.win_gadd.show()

    def make_buttons(self):
        self.b_addg = QtWidgets.QPushButton(self)
        self.b_addg.move(100, 400)
        self.b_addg.setText("Add new guest")
        self.b_addg.adjustSize()
        self.b_addg.clicked.connect(self.add_guest)

        self.b_cal = QtWidgets.QPushButton(self)
        self.b_cal.move(300, 400)
        self.b_cal.setText("Show calendar")
        self.b_cal.adjustSize()
        self.b_cal.clicked.connect(self.show_calendar)

        try:
            filename = "guestsdata/guests_{0}_{1}.csv".format(date.today().month, date.today().year)
            db = pd.read_csv(filename)
            info = pd.DataFrame(db, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                              'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

        except:
            filename = ""
            info = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                             'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

        checkoutsnum = 0
        sameday = False
        roomslist = []
        index = 0
        if filename == "":
            checkoutsnum = 0
        elif filename == "guestsdata/guests_{0}_{1}.csv".format(date.today().month, date.today().year):
            cods = info['checkoutday']
            coms = info['checkoutmonth']
            room = info['room']
            for i in cods:
                if int(i) == int(date.today().day):
                    sameday = True
                for i in coms:
                    if int(i) == int(date.today().month) and sameday == True:
                        checkoutsnum += 1
                        sameday = False
                        roomslist.append(room[index])
                index += 1

        todaysdate = [date.today().day,date.today().month,date.today().year]
        if todaysdate[0] == calendar.monthrange(date.today().year,date.today().month)[1] and not (date.today().month == 12 and date.today().day == 31):
            tomorrowsdate = [1,date.today().month+1,date.today().year]
        elif date.today().month == 12 and date.today().day == 31:
            tomorrowsdate = [1,1,date.today().year+1]
        else:
            tomorrowsdate = [date.today().day+1,date.today().month,date.today().year]

        self.b_checkouts = QtWidgets.QPushButton(self)
        self.b_checkouts.move(500, 400)
        self.b_checkouts.setText("Checkouts today: {0}".format(checkoutsnum))
        self.b_checkouts.adjustSize()
        but_text = self.b_checkouts.text()
        self.b_checkouts.clicked.connect(partial(self.but_show_todays_checkouts,but_text, roomslist))

        checkoutsnum2 = 0

        try:
            filename2 = "guestsdata/guests_{0}_{1}.csv".format(tomorrowsdate[1], tomorrowsdate[2])
            db2 = pd.read_csv(filename2)
            info2 = pd.DataFrame(db2, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                              'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

        except:
            filename2 = ""
            info2 = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                             'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])


        sameday2 = False
        roomslist2 = []
        index = 0
        if filename2 == "":
            checkoutsnum2 = 0
        elif filename2 == "guestsdata/guests_{0}_{1}.csv".format(tomorrowsdate[1], tomorrowsdate[2]):
            cods2 = info2['checkoutday']
            coms2 = info2['checkoutmonth']
            room2 = info2['room']
            for i in cods2:
                if int(i) == int(tomorrowsdate[0]):
                    sameday2 = True
                for i in coms2:
                    if int(i) == int(tomorrowsdate[1]) and sameday2 == True:
                        checkoutsnum2 += 1
                        sameday2 = False
                        roomslist2.append(room2[index])
                index += 1

        self.b_checkoutstomorrow = QtWidgets.QPushButton(self)
        self.b_checkoutstomorrow.move(500, 350)
        self.b_checkoutstomorrow.setText("Checkouts tomorrow: {0}".format(checkoutsnum2))
        self.b_checkoutstomorrow.adjustSize()
        but_text2 = self.b_checkoutstomorrow.text()
        self.b_checkoutstomorrow.clicked.connect(partial(self.but_show_todays_checkouts,but_text2, roomslist2))

        self.grid_layout.addWidget(self.b_checkoutstomorrow)
        self.grid_layout.addWidget(self.b_cal)
        self.grid_layout.addWidget(self.b_addg)
        self.grid_layout.addWidget(self.b_checkouts)

    def but_show_todays_checkouts(self, but_text, roomslist):
        self.showcheckouts = ShowCheckouts(but_text, roomslist)
        if self.showcheckouts.isVisible():
            self.showcheckouts.hide()
        else:
            self.showcheckouts.show()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.main_menu()
    win.make_buttons()
    win.show()
    sys.exit(app.exec())
