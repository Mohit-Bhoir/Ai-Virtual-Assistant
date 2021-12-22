from JarvisUi import Ui_JarvisUi
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTime , QDate
from PyQt5.uic  import loadUiType
import Main
import sys

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        Main.starter()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        
        super().__init__()

        self.gui = Ui_JarvisUi()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("..//..//..//Downloads/gui//ExtraGui//Jarvis_Gui (1).gif")
        self.gui.gif1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("..//..//..//Downloads//gui//ExtraGui//Code_Template.gif")
        self.gui.gif2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//..//..//Downloads//gui//system.gif")
        self.gui.gif3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("../../../Downloads/gui/VoiceReg/Aqua.gif")
        self.gui.gif4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("..//..//..//Downloads//LIVE WALLPAPER _ AI JARVIS - IRON-MAN _ STATUS REALM _ PC_DESKTOP _ (Download link in description).gif")
        self.gui.gif5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("..//..//..//Downloads//gui//ExtraGui//Hero_Template.gif")
        self.gui.gif6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("..//..//..//Downloads//gui//ExtraGui//Earth.gif")
        self.gui.gif7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie("..//..//..//Downloads//gui//ExtraGui//Health_Template.gif")
        self.gui.gif8.setMovie(self.gui.label8)
        self.gui.label8.start()


        self.gui.label10 = QtGui.QMovie("..//..//..//Downloads//gui//gui3.gif")
        self.gui.gif_1.setMovie(self.gui.label10)
        self.gui.label10.start()

        

    #     timer = QTimer(self)
    #     timer.timeout.connect(self.showTimeLive)
    #     timer.start(999)
        startExe.start()

    # def showTimeLive(self):
    #     t_i_m_e = QTime.currentTime()
    #     time = t_i_m_e.toString()
    #     d_a_t_e = QDate.currentDate()
    #     date = d_a_t_e.toString()
    #     label_time = "Time : " + time
    #     label_date = "Date : " + date

    #     self.gui.gif11.setText(label_time)
    #     self.gui.gif11_2.setText(label_date)




GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())

        
    