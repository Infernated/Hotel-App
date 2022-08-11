import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from datetime import date
import calendar
import pandas as pd
import random
from functools import partial

PyQt5.QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

class GuestInfo(QtWidgets.QWidget, QtCore.QDate):
    def __init__(self, firstname, lastname, cind, cinm, ciny, cod, com, coy, room):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.cind = cind
        self.cinm = cinm
        self.ciny = ciny
        self.cod = cod
        self.com = com
        self.coy = coy
        self.room = room
        self.setGeometry(530, 180, 300, 200)
        self.setWindowTitle("Guest Info")
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
        self.but_delete = QtWidgets.QPushButton(self)
        self.but_q = QtWidgets.QPushButton(self)
        self.initscreen()

    def initscreen(self):
        self.lab1.setText("First name:")
        self.lab1.move(60, 20)
        self.lab1.setFont(QtGui.QFont('Times', 15))
        self.lab1.adjustSize()

        self.lab2.setText("Last name:")
        self.lab2.move(61, 40)
        self.lab2.setFont(QtGui.QFont('Times', 15))
        self.lab2.adjustSize()

        self.lab3.setText("Check in date:")
        self.lab3.move(33, 60)
        self.lab3.setFont(QtGui.QFont('Times', 15))
        self.lab3.adjustSize()

        self.lab4.setText("Check out date:")
        self.lab4.move(20, 80)
        self.lab4.setFont(QtGui.QFont('Times', 15))
        self.lab4.adjustSize()

        self.lab5.setText("Room:")
        self.lab5.move(103, 100)
        self.lab5.setFont(QtGui.QFont('Times', 15))
        self.lab5.adjustSize()

        self.lab6.setText(self.firstname)
        self.lab6.move(170, 20)
        self.lab6.setFont(QtGui.QFont('Times', 15))
        self.lab6.adjustSize()

        self.lab7.setText(self.lastname)
        self.lab7.move(170, 40)
        self.lab7.setFont(QtGui.QFont('Times', 15))
        self.lab7.adjustSize()


        self.lab8.setText(str(self.cind)+"-"+str(self.cinm)+"-"+str(self.ciny))
        self.lab8.move(170, 60)
        self.lab8.setFont(QtGui.QFont('Times', 15))
        self.lab8.adjustSize()

        self.lab9.setText(str(self.cod)+"-"+str(self.com)+"-"+str(self.coy))
        self.lab9.move(170, 80)
        self.lab9.setFont(QtGui.QFont('Times', 15))
        self.lab9.adjustSize()

        self.lab10.setText(self.room)
        self.lab10.move(170, 100)
        self.lab10.setFont(QtGui.QFont('Times', 15))
        self.lab10.adjustSize()

        self.but_delete.move(160,140)
        self.but_delete.resize(50,40)
        self.but_delete.setText("Delete")
        self.but_delete.clicked.connect(self.but_del)

        self.but_q.move(230,140)
        self.but_q.resize(50,40)
        self.but_q.setText("Quit")
        self.but_q.clicked.connect(self.but_quit)


    def but_del(self):
        filename = "guestsdata/guests_{0}_{1}.csv".format(self.cinm, self.ciny)
        filename2 = ""
        try:
            gd = pd.read_csv(filename)
            guestdb = pd.DataFrame(gd, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
            filename2 = "guestsdata/guests_{0}_{1}.csv".format(self.com, self.coy)
            gd2 = pd.read_csv(filename2)
            guestdb2 = pd.DataFrame(gd2, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
        except:
            guestdb = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
            guestdb2 = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                                  'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

        lastname = guestdb['lastname']
        firstname = guestdb['firstname']
        cind = guestdb['checkinday']
        cinm = guestdb['checkinmonth']
        ciny = guestdb['checkinyear']
        cod = guestdb['checkoutday']
        com = guestdb['checkoutmonth']
        coy = guestdb['checkoutyear']
        room = guestdb['room']

        lastname2 = guestdb2['lastname']
        firstname2 = guestdb2['firstname']
        cind2 = guestdb2['checkinday']
        cinm2 = guestdb2['checkinmonth']
        ciny2 = guestdb2['checkinyear']
        cod2 = guestdb2['checkoutday']
        com2 = guestdb2['checkoutmonth']
        coy2 = guestdb2['checkoutyear']
        room2 = guestdb2['room']

        ind = 0
        notsamemonth = 0
        for i in range(len(guestdb)):
            if str(lastname[ind]) == str(self.lastname) and \
                    str(firstname[ind]) == str(self.firstname) and \
                    str(cind[ind]) == str(self.cind) and \
                    str(cinm[ind]) == str(self.cinm) and \
                    str(ciny[ind]) == str(self.ciny) and\
                    str(cod[ind]) == str(self.cod) and \
                    str(com[ind]) == str(self.com) and\
                    str(coy[ind]) == str(self.coy) and \
                    str(room[ind]) == str(self.room) and \
                    len(guestdb) != 0:
                if self.cinm != self.com:
                    guestdb = guestdb.drop(ind)
                    rawdb = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                                  'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
                    df = pd.concat([rawdb, guestdb])
                    df.to_csv(filename, index=False)
                    notsamemonth = 1
                else:
                    guestdb = guestdb.drop(ind)
                    rawdb = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                                  'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
                    df = pd.concat([rawdb, guestdb])
                    df.to_csv(filename, index=False)
            ind += 1
        ind = 0
        if notsamemonth == 1:
            for i in range(len(guestdb2)):
                if str(lastname2[ind]) == str(self.lastname) and \
                        str(firstname2[ind]) == str(self.firstname) and \
                        str(cind2[ind]) == str(self.cind) and \
                        str(cinm2[ind]) == str(self.cinm) and \
                        str(ciny2[ind]) == str(self.ciny) and \
                        str(cod2[ind]) == str(self.cod) and \
                        str(com2[ind]) == str(self.com) and \
                        str(coy2[ind]) == str(self.coy) and \
                        str(room2[ind]) == str(self.room) and \
                        len(guestdb2) != 0:
                    if self.cinm != self.com:
                        guestdb2 = guestdb2.drop(ind)
                        rawdb = pd.DataFrame(
                            columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                     'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
                        df = pd.concat([rawdb, guestdb2])
                        df.to_csv(filename2, index=False)
                    else:
                        guestdb2 = guestdb2.drop(ind)
                        rawdb = pd.DataFrame(
                            columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                     'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
                        df = pd.concat([rawdb, guestdb2])
                        df.to_csv(filename2, index=False)
                ind += 1

        self.close()
    def but_quit(self):
        self.close()

class GuestsCalendar(QtWidgets.QWidget, QtCore.QDate):
    def __init__(self):
        super().__init__()
        self.setGeometry(120, 100, 1130, 550)
        self.setWindowTitle("Guests calendar")
        self.setFixedSize(1130,550)
        self.but_next = QtWidgets.QPushButton(self)
        self.but_next.move(1050,10)
        self.but_next.resize(50,40)
        self.but_next.setText("Next")
        self.but_next.clicked.connect(self.but_next_mth)

        self.but_prev = QtWidgets.QPushButton(self)
        self.but_prev.move(10,10)
        self.but_prev.resize(50,40)
        self.but_prev.setText("Prev")
        self.but_prev.clicked.connect(self.but_prev_mth)

        self.but_ref = QtWidgets.QPushButton(self)
        self.but_ref.move(100,10)
        self.but_ref.resize(50,40)
        self.but_ref.setText("Refresh")
        self.but_ref.clicked.connect(self.refresh)

        self.rec1 = QtWidgets.QLabel(self)
        self.rec2 = QtWidgets.QLabel(self)
        self.rec3 = QtWidgets.QLabel(self)
        self.rec4 = QtWidgets.QLabel(self)
        self.rec5 = QtWidgets.QLabel(self)
        self.rec6 = QtWidgets.QLabel(self)
        self.rec7 = QtWidgets.QLabel(self)
        self.rec8 = QtWidgets.QLabel(self)
        self.rec9 = QtWidgets.QLabel(self)
        self.rec10 = QtWidgets.QLabel(self)
        self.rec11 = QtWidgets.QLabel(self)
        self.rec12 = QtWidgets.QLabel(self)
        self.rec13 = QtWidgets.QLabel(self)
        self.rec14 = QtWidgets.QLabel(self)
        self.rec15 = QtWidgets.QLabel(self)
        self.rec16 = QtWidgets.QLabel(self)
        self.rec17 = QtWidgets.QLabel(self)
        self.rec18 = QtWidgets.QLabel(self)
        self.rec19 = QtWidgets.QLabel(self)
        self.rec20 = QtWidgets.QLabel(self)
        self.rec21 = QtWidgets.QLabel(self)
        self.rec22 = QtWidgets.QLabel(self)
        self.rec23 = QtWidgets.QLabel(self)
        self.rec24 = QtWidgets.QLabel(self)
        self.rec25 = QtWidgets.QLabel(self)
        self.rec26 = QtWidgets.QLabel(self)
        self.rec27 = QtWidgets.QLabel(self)
        self.rec28 = QtWidgets.QLabel(self)
        self.rec29 = QtWidgets.QLabel(self)
        self.rec30 = QtWidgets.QLabel(self)
        self.rec31 = QtWidgets.QLabel(self)
        self.rech1 = QtWidgets.QLabel(self)
        self.rech2 = QtWidgets.QLabel(self)
        self.rech3 = QtWidgets.QLabel(self)
        self.rech4 = QtWidgets.QLabel(self)
        self.rech5 = QtWidgets.QLabel(self)
        self.rech6 = QtWidgets.QLabel(self)
        self.rech7 = QtWidgets.QLabel(self)
        self.rech8 = QtWidgets.QLabel(self)
        self.rech9 = QtWidgets.QLabel(self)
        self.rech10 = QtWidgets.QLabel(self)
        self.rech11 = QtWidgets.QLabel(self)
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
        self.lab13 = QtWidgets.QLabel(self)
        self.lab14 = QtWidgets.QLabel(self)
        self.lab15 = QtWidgets.QLabel(self)
        self.lab16 = QtWidgets.QLabel(self)
        self.lab17 = QtWidgets.QLabel(self)
        self.lab18 = QtWidgets.QLabel(self)
        self.lab19 = QtWidgets.QLabel(self)
        self.lab20 = QtWidgets.QLabel(self)
        self.lab21 = QtWidgets.QLabel(self)
        self.lab22 = QtWidgets.QLabel(self)
        self.lab23 = QtWidgets.QLabel(self)
        self.lab24 = QtWidgets.QLabel(self)
        self.lab25 = QtWidgets.QLabel(self)
        self.lab26 = QtWidgets.QLabel(self)
        self.lab27 = QtWidgets.QLabel(self)
        self.lab28 = QtWidgets.QLabel(self)
        self.lab29 = QtWidgets.QLabel(self)
        self.lab30 = QtWidgets.QLabel(self)
        self.lab31 = QtWidgets.QLabel(self)
        self.labday1 = QtWidgets.QLabel(self)
        self.labday2 = QtWidgets.QLabel(self)
        self.labday3 = QtWidgets.QLabel(self)
        self.labday4 = QtWidgets.QLabel(self)
        self.labday5 = QtWidgets.QLabel(self)
        self.labday6 = QtWidgets.QLabel(self)
        self.labday7 = QtWidgets.QLabel(self)
        self.labday8 = QtWidgets.QLabel(self)
        self.labday9 = QtWidgets.QLabel(self)
        self.labday10 = QtWidgets.QLabel(self)
        self.labday11 = QtWidgets.QLabel(self)
        self.labday12 = QtWidgets.QLabel(self)
        self.labday13 = QtWidgets.QLabel(self)
        self.labday14 = QtWidgets.QLabel(self)
        self.labday15 = QtWidgets.QLabel(self)
        self.labday16 = QtWidgets.QLabel(self)
        self.labday17 = QtWidgets.QLabel(self)
        self.labday18 = QtWidgets.QLabel(self)
        self.labday19 = QtWidgets.QLabel(self)
        self.labday20 = QtWidgets.QLabel(self)
        self.labday21 = QtWidgets.QLabel(self)
        self.labday22 = QtWidgets.QLabel(self)
        self.labday23 = QtWidgets.QLabel(self)
        self.labday24 = QtWidgets.QLabel(self)
        self.labday25 = QtWidgets.QLabel(self)
        self.labday26 = QtWidgets.QLabel(self)
        self.labday27 = QtWidgets.QLabel(self)
        self.labday28 = QtWidgets.QLabel(self)
        self.labday29 = QtWidgets.QLabel(self)
        self.labday30 = QtWidgets.QLabel(self)
        self.labday31 = QtWidgets.QLabel(self)
        self.labrApp = QtWidgets.QLabel(self)
        self.labr2 = QtWidgets.QLabel(self)
        self.labr3 = QtWidgets.QLabel(self)
        self.labr4 = QtWidgets.QLabel(self)
        self.labr7 = QtWidgets.QLabel(self)
        self.labr8 = QtWidgets.QLabel(self)
        self.labr9 = QtWidgets.QLabel(self)
        self.labr10 = QtWidgets.QLabel(self)
        self.labr11 = QtWidgets.QLabel(self)
        self.labr12 = QtWidgets.QLabel(self)
        self.labr14 = QtWidgets.QLabel(self)
        self.labdate = QtWidgets.QLabel(self)
        self.initdate()
        self.initlabels()
        self.initguests()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_F5:
            self.refresh()

    def initdate(self):
        self.todaysdate = date.today()
        self.tyear = self.todaysdate.year
        self.tmonth = self.todaysdate.month
        self.tday = self.todaysdate.day
    def initlabels(self):
        self.reclist = [
            self.rec1,
            self.rec2,
            self.rec3,
            self.rec4,
            self.rec5,
            self.rec6,
            self.rec7,
            self.rec8,
            self.rec9,
            self.rec10,
            self.rec11,
            self.rec12,
            self.rec13,
            self.rec14,
            self.rec15,
            self.rec16,
            self.rec17,
            self.rec18,
            self.rec19,
            self.rec20,
            self.rec21,
            self.rec22,
            self.rec23,
            self.rec24,
            self.rec25,
            self.rec26,
            self.rec27,
            self.rec28,
            self.rec29,
            self.rec30,
            self.rec31
        ]

        for i in self.reclist:
            i.close()
        self.sizex = 30
        self.colind = 0
        self.daynum = 1
        for i in self.reclist:
            if self.daynum < 29:
                i.setFixedSize(34,430)
                i.move(50+self.sizex,100)
                i.show()
            elif self.daynum == 29 and not (self.tmonth == 2 and calendar.isleap(self.tyear) == False):
                i.move(50 + self.sizex, 100)
                i.setFixedSize(34,430)
                i.show()
            elif self.daynum == 30 and self.tmonth != 2:
                i.move(50 + self.sizex, 100)
                i.setFixedSize(34,430)
                i.show()
            elif self.daynum == 31 and self.tmonth != 2 and self.tmonth != 4 and self.tmonth != 6 \
                    and self.tmonth != 9 and self.tmonth != 11:
                i.move(50 + self.sizex, 100)
                i.setFixedSize(34,430)
                i.show()
            if self.colind == 2:
                self.colind = 0
            if self.colind == 1:
                i.setStyleSheet("background-color: lightgray;border: 1px solid black;")
            else:
                i.setStyleSheet("background-color: gray;border: 1px solid black;")
            self.sizex += 33
            self.colind += 1
            self.daynum += 1
        self.sizex = 30

        self.lablist = [
            self.lab1,
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
            self.lab12,
            self.lab13,
            self.lab14,
            self.lab15,
            self.lab16,
            self.lab17,
            self.lab18,
            self.lab19,
            self.lab20,
            self.lab21,
            self.lab22,
            self.lab23,
            self.lab24,
            self.lab25,
            self.lab26,
            self.lab27,
            self.lab28,
            self.lab29,
            self.lab30,
            self.lab31
        ]
        for i in self.lablist:
            i.close()
        self.sizex = 30
        self.daynum = 1
        for i in self.lablist:
            if self.daynum < 29:
                i.setText(str(self.daynum))
                i.setFixedSize(34,26)
                i.move(50+self.sizex,50)
                i.setFont(QtGui.QFont('Times', 15))
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.daynum == 29 and not (self.tmonth == 2 and calendar.isleap(self.tyear) == False):
                i.setText(str(self.daynum))
                i.move(50 + self.sizex, 50)
                i.setFixedSize(34,26)
                i.setFont(QtGui.QFont('Times', 15))
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.daynum == 30 and self.tmonth != 2:
                i.setText(str(self.daynum))
                i.move(50 + self.sizex, 50)
                i.setFixedSize(34,26)
                i.setFont(QtGui.QFont('Times', 15))
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.daynum == 31 and self.tmonth != 2 and self.tmonth != 4 and self.tmonth != 6 \
                    and self.tmonth != 9 and self.tmonth != 11:
                i.setText(str(self.daynum))
                i.move(50 + self.sizex, 50)
                i.setFixedSize(34,26)
                i.setFont(QtGui.QFont('Times', 15))
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            self.sizex += 33
            self.daynum += 1

        self.sizex = 30



        self.labdlist = [
            self.labday1,
            self.labday2,
            self.labday3,
            self.labday4,
            self.labday5,
            self.labday6,
            self.labday7,
            self.labday8,
            self.labday9,
            self.labday10,
            self.labday11,
            self.labday12,
            self.labday13,
            self.labday14,
            self.labday15,
            self.labday16,
            self.labday17,
            self.labday18,
            self.labday19,
            self.labday20,
            self.labday21,
            self.labday22,
            self.labday23,
            self.labday24,
            self.labday25,
            self.labday26,
            self.labday27,
            self.labday28,
        ]
        if not (self.tmonth == 2 and calendar.isleap(self.tyear) == False):
            self.labdlist.append(self.labday29)
        if self.tmonth != 2:
            self.labdlist.append(self.labday30)
        if self.tmonth != 2 and self.tmonth != 4 and self.tmonth != 6\
                and self.tmonth != 9 and self.tmonth != 11:
            self.labdlist.append(self.labday31)

        self.sizex = 30
        self.dayind = 0
        self.mthweeks = calendar.monthcalendar(self.tyear,self.tmonth)
        self.mthlist = []
        for i in self.mthweeks:
            self.mthlist += i
        self.dayname = 0
        for i in self.mthlist:
            if i == 0:
                self.dayname += 1
            else:
                break
        for i in self.labdlist:
            i.close()
        self.labday29.close()
        self.labday30.close()
        self.labday31.close()
        for i in self.labdlist:
            i.setFixedSize(34, 26)
            if self.dayname == 0:
                i.setText("Mon")
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.dayname == 1:
                i.setText("Tue")
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.dayname == 2:
                i.setText("Wed")
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.dayname == 3:
                i.setText("Thu")
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.dayname == 4:
                i.setText("Fri")
                i.setStyleSheet("border: 1px solid black;")
                i.show()
            elif self.dayname == 5:
                i.setText("Sat")
                i.setStyleSheet("border: 1px solid black;color:red")
                i.show()
            elif self.dayname == 6:
                i.setText("Sun")
                i.setStyleSheet("border: 1px solid black;color:red")
                i.show()

            i.move(50 + self.sizex, 75)
            i.setFont(QtGui.QFont('Times', 10))
            self.sizex += 33
            self.dayname += 1
            if self.dayname == 7:
                self.dayname = 0



        self.labrApp.setText("App")
        self.labrApp.move(11,100)
        self.labrApp.setFont(QtGui.QFont('Times', 20))
        self.labrApp.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labrApp.setFixedSize(70,40)


        self.labr2.setText("2")
        self.labr2.move(11,139)
        self.labr2.setFont(QtGui.QFont('Times', 20))
        self.labr2.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr2.setFixedSize(70,40)


        self.labr3.setText("3")
        self.labr3.move(11,178)
        self.labr3.setFont(QtGui.QFont('Times', 20))
        self.labr3.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr3.setFixedSize(70,40)


        self.labr4.setText("4")
        self.labr4.move(11,217)
        self.labr4.setFont(QtGui.QFont('Times', 20))
        self.labr4.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr4.setFixedSize(70,40)


        self.labr7.setText("7")
        self.labr7.move(11,256)
        self.labr7.setFont(QtGui.QFont('Times', 20))
        self.labr7.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr7.setFixedSize(70,40)


        self.labr8.setText("8")
        self.labr8.move(11,295)
        self.labr8.setFont(QtGui.QFont('Times', 20))
        self.labr8.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr8.setFixedSize(70,40)


        self.labr9.setText("9")
        self.labr9.move(11,334)
        self.labr9.setFont(QtGui.QFont('Times', 20))
        self.labr9.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr9.setFixedSize(70,40)


        self.labr10.setText("10")
        self.labr10.move(11,373)
        self.labr10.setFont(QtGui.QFont('Times', 20))
        self.labr10.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr10.setFixedSize(70,40)


        self.labr11.setText("11")
        self.labr11.move(11,412)
        self.labr11.setFont(QtGui.QFont('Times', 20))
        self.labr11.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr11.setFixedSize(70,40)


        self.labr12.setText("12")
        self.labr12.move(11,451)
        self.labr12.setFont(QtGui.QFont('Times', 20))
        self.labr12.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr12.setFixedSize(70,40)


        self.labr14.setText("14")
        self.labr14.move(11,490)
        self.labr14.setFont(QtGui.QFont('Times', 20))
        self.labr14.setStyleSheet("border: 1px solid black;color:#c7129d")
        self.labr14.setFixedSize(70,40)


        self.labdate.move(550,10)
        self.labdate.setFont(QtGui.QFont('Constantia', 20))
        self.labdate.setStyleSheet("color:#c7129d")
        if self.tmonth == 1:
            self.labdate.setText("January " + str(self.tyear))
        elif self.tmonth == 2:
            self.labdate.setText("February " + str(self.tyear))
        elif self.tmonth == 3:
            self.labdate.setText("March " + str(self.tyear))
        elif self.tmonth == 4:
            self.labdate.setText("April " + str(self.tyear))
        elif self.tmonth == 5:
            self.labdate.setText("May " + str(self.tyear))
        elif self.tmonth == 6:
            self.labdate.setText("June " + str(self.tyear))
        elif self.tmonth == 7:
            self.labdate.setText("July " + str(self.tyear))
        elif self.tmonth == 8:
            self.labdate.setText("August " + str(self.tyear))
        elif self.tmonth == 9:
            self.labdate.setText("September " + str(self.tyear))
        elif self.tmonth == 10:
            self.labdate.setText("October " + str(self.tyear))
        elif self.tmonth == 11:
            self.labdate.setText("November " + str(self.tyear))
        elif self.tmonth == 12:
            self.labdate.setText("December " + str(self.tyear))
        self.labdate.adjustSize()

        self.rechlist = [
            self.rech1,
            self.rech2,
            self.rech3,
            self.rech4,
            self.rech5,
            self.rech6,
            self.rech7,
            self.rech8,
            self.rech9,
            self.rech10,
            self.rech11
        ]

        for i in self.rechlist:
            i.close()
        self.sizey = 100
        for i in self.rechlist:
            if len(self.labdlist) == 30:
                i.move(80, 0 + self.sizey)
                i.setFixedSize(991,40)
                i.show()
            elif len(self.labdlist) == 29:
                i.move(80, 0 + self.sizey)
                i.setFixedSize(958,40)
                i.show()
            elif len(self.labdlist) == 28:
                i.move(80, 0 + self.sizey)
                i.setFixedSize(925,40)
                i.show()
            elif len(self.labdlist) == 31:
                i.move(80, 0 + self.sizey)
                i.setFixedSize(1024,40)
                i.show()
            if self.colind == 2:
                self.colind = 0
            if self.colind == 1:
                i.setStyleSheet("border: 1px solid black;")
            else:
                i.setStyleSheet("border: 1px solid black;")
            self.sizey += 39
            self.colind += 1


    def but_prev_mth(self):
        if self.tmonth > 1:
            for i in self.guestslist:
                i.hide()
                i.destroy()
            self.tmonth -= 1
            self.initlabels()
            self.initguests()
            for i in self.guestslist:
                i.show()
        else:
            for i in self.guestslist:
                i.hide()
                i.destroy()
            self.tyear -= 1
            self.tmonth = 12
            self.initlabels()
            self.initguests()
            for i in self.guestslist:
                i.show()

    def refresh(self):
            for i in self.guestslist:
                i.hide()
                i.destroy()
            self.initlabels()
            self.initguests()
            for i in self.guestslist:
                i.show()


    def but_next_mth(self):
        if self.tmonth < 12:
            for i in self.guestslist:
                i.hide()
                i.destroy()
            self.tmonth += 1
            self.initlabels()
            self.initguests()
            for i in self.guestslist:
                i.show()
        else:
            for i in self.guestslist:
                i.hide()
                i.destroy()
            self.tmonth = 1
            self.tyear += 1
            self.initlabels()
            self.initguests()
            for i in self.guestslist:
                i.show()

    def initguests(self):
        try:
            filename = "guestsdata/guests_{0}_{1}.csv".format(self.tmonth, self.tyear)
            gd = pd.read_csv(filename)
            guestdb = pd.DataFrame(gd, columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])
        except:
            guestdb = pd.DataFrame(columns=['firstname', 'lastname', 'checkinday', 'checkinmonth', 'checkinyear',
                                            'checkoutday', 'checkoutmonth', 'checkoutyear', 'room'])

        lastname = guestdb['lastname']
        firstname = guestdb['firstname']
        cind = guestdb['checkinday']
        cinm = guestdb['checkinmonth']
        ciny = guestdb['checkinyear']
        cod = guestdb['checkoutday']
        com = guestdb['checkoutmonth']
        coy = guestdb['checkoutyear']
        room = guestdb['room']

        ind = 0
        self.guestslist = []
        for i in range(len(guestdb)):
            movex = 0
            if cind[ind] == 1:
                movex = 95
            elif cind[ind] == 2:
                movex = 128
            elif cind[ind] == 3:
                movex = 161
            elif cind[ind] == 4:
                movex = 194
            elif cind[ind] == 5:
                movex = 227
            elif cind[ind] == 6:
                movex = 260
            elif cind[ind] == 7:
                movex = 293
            elif cind[ind] == 8:
                movex = 326
            elif cind[ind] == 9:
                movex = 359
            elif cind[ind] == 10:
                movex = 392
            elif cind[ind] == 11:
                movex = 425
            elif cind[ind] == 12:
                movex = 458
            elif cind[ind] == 13:
                movex = 491
            elif cind[ind] == 14:
                movex = 524
            elif cind[ind] == 15:
                movex = 557
            elif cind[ind] == 16:
                movex = 590
            elif cind[ind] == 17:
                movex = 623
            elif cind[ind] == 18:
                movex = 656
            elif cind[ind] == 19:
                movex = 689
            elif cind[ind] == 20:
                movex = 722
            elif cind[ind] == 21:
                movex = 755
            elif cind[ind] == 22:
                movex = 788
            elif cind[ind] == 23:
                movex = 821
            elif cind[ind] == 24:
                movex = 854
            elif cind[ind] == 25:
                movex = 887
            elif cind[ind] == 26:
                movex = 920
            elif cind[ind] == 27:
                movex = 953
            elif cind[ind] == 28:
                movex = 986
            elif cind[ind] == 29:
                movex = 1019
            elif cind[ind] == 30:
                movex = 1052
            elif cind[ind] == 31:
                movex = 1085

            movey = 0
            if str(room[ind]) == "App":
                movey = 104
            elif str(room[ind]) == "2":
                movey = 143
            elif str(room[ind]) == "3":
                movey = 182
            elif str(room[ind]) == "4":
                movey = 221
            elif str(room[ind]) == "7":
                movey = 260
            elif str(room[ind]) == "8":
                movey = 299
            elif str(room[ind]) == "9":
                movey = 338
            elif str(room[ind]) == "10":
                movey = 377
            elif str(room[ind]) == "11":
                movey = 416
            elif str(room[ind]) == "12":
                movey = 455
            elif str(room[ind]) == "14":
                movey = 494

            resizex = 0

            if cinm[ind] == com[ind]:
                days = cod[ind] - cind[ind]
                resizex = 33*days
            elif (self.tmonth == cinm[ind] and (com[ind] - cinm[ind])) == 1 or \
                    (self.tmonth == cinm[ind] and (com[ind] - cinm[ind]) == -11):
                dcount = calendar.monthrange(ciny[ind],cinm[ind])
                days = dcount[1] - cind[ind]
                resizex = 33*days
                resizex += 16
            else:
                days = cod[ind]
                movex = 82
                resizex = 33*days
                resizex -= 16
            i = QtWidgets.QPushButton(self)
            i.move(movex, movey)
            i.resize(resizex, 30)
            i.setText(str(lastname[ind]))
            i.clicked.connect(partial(self.guestinfo,firstname[ind],lastname[ind],
                cind[ind],cinm[ind],ciny[ind],cod[ind],com[ind],coy[ind],room[ind]))
            i.setStyleSheet("background-color:rgb({0},{1},{2})".format(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            self.guestslist.append(i)
            ind += 1

    def guestinfo(self,firstname,lastname,cind,cinm,ciny,cod,com,coy,room):
        self.ginf = GuestInfo(firstname,lastname,cind,cinm, ciny, cod, com, coy, str(room))
        if self.ginf.isVisible():
            self.ginf.hide()
        else:
            self.ginf.show()
