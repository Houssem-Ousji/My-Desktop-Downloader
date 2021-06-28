# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import urllib.request
import pafy
import humanize
from pytube import Playlist

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 381))
        self.tabWidget.setStyleSheet("QPushButton{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color:#6a6b6e;\n"
"font: 10pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-bottom-color: rgb(115, 115, 115);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #6a6b6e;\n"
"}\n"
"QLabel {\n"
"    color:rgb(255,255,255);\n"
"    font: 12pt \"MS Reference Sans Serif\";\n"
"\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#6a6b6e;\n"
"}\n"
"QProgressBar::chunk {\n"
"    \n"
"    background-color: rgb(199, 139, 54);\n"
"    border-radius: 5px;\n"
"}\n"
"QTabWidget {\n"
"font: 11pt \"MS Reference Sans Serif\";\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:black;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding:5px;\n"
"    color:rgb(250,250,250);\n"
"      background-color:#6a6b6e;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"      border-top-right-radius:4px;\n"
"   border-top-left-radius:4px;\n"
"    border-color: #6a6b6e;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:  rgb(199, 139, 54);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"        margin-top: 1px;\n"
"        margin-right: 1px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 200, 201, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 90, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 30, 511, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 90, 371, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(190, 150, 511, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(540, 190, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"E:\developpement\projects\My_Desktop_Downloader\My-Desktop-Downloader\images\file.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 260, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 40, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(560, 90, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 511, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 371, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(190, 210, 511, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(190, 150, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 150, 261, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(550, 260, 51, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(r"E:\developpement\projects\My_Desktop_Downloader\My-Desktop-Downloader\images\youtube.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 90, 141, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 90, 371, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(190, 30, 511, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(50, 40, 47, 13))
        self.label_10.setObjectName("label_10")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(310, 260, 201, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar_5.setGeometry(QtCore.QRect(190, 210, 511, 23))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 150, 171, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(360, 150, 341, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(550, 260, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(r"E:\developpement\projects\My_Desktop_Downloader\My-Desktop-Downloader\images\playlist.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Handle_Ui()
        self.Handle_Buttons()
        # initialize my Progress bars
        self.progressBar_2.setValue(0)
        self.progressBar.setValue(0)
        self.progressBar_5.setValue(0)

        # set the choices in the combobox of the third section (Youtube Playlist)
        self.comboBox_3.addItem("Media type : Audio")
        self.comboBox_3.addItem("Media type : Video")
        self.comboBox_3.addItem("Media type : Normal")

    # Handle ui
    def Handle_Ui(self):
        MainWindow.setWindowTitle("My Desktop Downloader")
        MainWindow.setFixedSize(771, 361)

    # Handle Buttons
    def Handle_Buttons(self):
        # buttons of the section 1
        self.pushButton_3.clicked.connect(self.Handle_Download_section_1)
        self.pushButton_4.clicked.connect(self.Browse_section_1)

        # Buttons of the section 2
        self.pushButton_2.clicked.connect(self.Handle_Download_Youtube_Video)
        self.pushButton.clicked.connect(self.Browse_section_2)
        self.pushButton_5.clicked.connect(self.Quality_section_2)

        # Butttons of the section 3
        self.pushButton_13.clicked.connect(self.Handle_Download_Youtube_Playlist)
        self.pushButton_11.clicked.connect(self.Browse_section_3)

############################# Start first section ################################
    # Saving and Showing the path of the first section
    def Browse_section_1(self):
        location = QFileDialog.getSaveFileName(MainWindow, caption="Save as", directory="C:/Users/HOUSSEM/Desktop",
                                                   filter="All files ()")
        self.lineEdit_4.setText(location[0])

    # Making the Progress bar
    def Handle_Progress_Bar_Section_1(self, block_number, block_size, total_size):
        recieved_data = block_number * block_size
        percentage = (recieved_data / total_size) * 100
        self.progressBar_2.setValue(int(percentage))
        QApplication.processEvents()

    # Downloading the file
    def Handle_Download_section_1(self):
        # Taking the data
        url = self.lineEdit_3.text()
        path = self.lineEdit_4.text()
        while path == '':
            QMessageBox.warning(MainWindow, "Error", "Choose Folder Please")
            self.Browse_section_1()
            path = self.lineEdit_4.text()

        # Make the Download
        try:
            urllib.request.urlretrieve(url, path, self.Handle_Progress_Bar_Section_1)
            QMessageBox.information(MainWindow, "Download Done", "successful download")
        except:
            QMessageBox.warning(MainWindow, "Download error", "download failed")

        # initializing the inputs and the Progress bar
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.progressBar_2.setValue(0)
############################# END first section ################################

############################# Start Second section ################################
    # Saving and Showing the path of the second section
    def Browse_section_2(self):
        location = QFileDialog.getExistingDirectory(MainWindow, caption="Choose Folder",
                                                        directory="C:/Users/HOUSSEM/Desktop")
        self.lineEdit_2.setText(location)

    # Our video Quality and the Media type
    def Quality_section_2(self):
        url = self.lineEdit.text()
        test = True
        try:
            video = pafy.new(url)
        except:
            QMessageBox.warning(MainWindow, "Error 404", "Url Doesn't exist !")
            self.lineEdit.setText('')
            test = False
        if test == True:
            for Stream in video.allstreams:
                file_size = humanize.naturalsize(Stream.get_filesize())
                video_data = "{} : {} : {} : {}".format(Stream.mediatype, Stream.extension, Stream.quality,
                                                            file_size)
                self.comboBox.addItem(video_data)

    # Making the Progress bar
    def Handle_Progress_Bar_Section_2(self, *Data_recieved):
        percentage = (Data_recieved[1] / Data_recieved[0]) * 100
        self.progressBar.setValue(int(percentage))
        QApplication.processEvents()

    # Download the Youtube Video
    def Handle_Download_Youtube_Video(self):
          url = self.lineEdit.text()
          test = True
          try:
            video = pafy.new(url)
          except:
            QMessageBox.warning(MainWindow, "Error 404", "Url Doesn't exist !")
            self.lineEdit.setText('')
            test = False
          if test == True:
              path = self.lineEdit_2.text()
              while path == '':
                  QMessageBox.warning(MainWindow, "Error", "Choose Folder Please")
                  self.Browse_section_2()
                  path = self.lineEdit_2.text()
              video_index = self.comboBox.currentIndex()
              try:
                  Download = video.allstreams[video_index].download(filepath=path,
                                                                    callback=self.Handle_Progress_Bar_Section_2)
                  QMessageBox.information(MainWindow, "Download Done", "successful download")
              except:
                  QMessageBox.warning(MainWindow, "Download error", "download failed")

              # Reset Our Inputs
              self.lineEdit.setText('')
              self.lineEdit_2.setText('')
              self.comboBox.clear()
############################# END second section ################################

############################# Start Third section ################################
    # Saving and Showing the path of the Third section
    def Browse_section_3(self):
        location = QFileDialog.getExistingDirectory(MainWindow, caption="Choose Folder", directory="C:/Users/HOUSSEM/Desktop")
        self.lineEdit_9.setText(location)

    # Making the Progress bar
    def Handle_Progress_Bar_section_3(self, *Data_recieved):
        percentage = (Data_recieved[1] / Data_recieved[0]) * 100
        self.progressBar_5.setValue(int(percentage))
        QApplication.processEvents()

    # Download the Youtube Video
    def Handle_Download_Youtube_Playlist(self):
        url = self.lineEdit_10.text()
        path = self.lineEdit_9.text()
        while path == '':
            QMessageBox.warning(MainWindow, "Error", "Choose Folder Please")
            self.Browse_section_3()
            path = self.lineEdit_9.text()

        test = True
        test_2 = True
        try:
            My_Playlist = Playlist(url)
        except:
            QMessageBox.warning(MainWindow, "Error 404", "Url Doesn't exist !")
            self.lineEdit_10.setText('')
            test = False
        if test:
            for url_video in My_Playlist:
                try:
                    video = pafy.new(url_video)
                except:
                    test_2 = False
                if test_2 and self.comboBox_3.currentIndex() == 0:
                    try:
                        self.lineEdit_11.setText("Downloading {}".format(video.title))
                        Download = video.getbestaudio().download(filepath=path,
                                                                 callback=self.Handle_Progress_Bar_section_3)
                    except:
                        QMessageBox.warning(MainWindow, "Error 404", "Download of '{}' Failed".format(video.title))
                elif test_2 and self.comboBox_3.currentIndex() == 1:
                    try:
                        self.lineEdit_11.setText("Downloading {}".format(video.title))
                        Download = video.getbestvideo().download(filepath=path,
                                                                 callback=self.Handle_Progress_Bar_section_3)
                    except:
                        QMessageBox.warning(MainWindow, "Error 404", "Download of '{}' Failed".format(video.title))
                elif test_2 and self.comboBox_3.currentIndex() == 2:
                    try:
                        self.lineEdit_11.setText("Downloading {}".format(video.title))
                        Download = video._getbest().download(filepath=path,
                                                             callback=self.Handle_Progress_Bar_section_3)
                    except:
                        QMessageBox.warning(MainWindow, "Error 404", "Download of '{}' Failed".format(video.title))
            QMessageBox.information(MainWindow, "Download Done", "successful download")
            # Reset The Inputs
            self.lineEdit_10.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_11.setText('')
            self.progressBar_5.setValue(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "URL"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Save Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Download Files"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Save Location"))
        self.pushButton_5.setText(_translate("MainWindow", "Quality Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Download Youtube Video"))
        self.pushButton_11.setText(_translate("MainWindow", "Browse"))
        self.label_9.setText(_translate("MainWindow", "Save Location"))
        self.label_10.setText(_translate("MainWindow", "URL"))
        self.pushButton_13.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Download Youtube\'s Playlist"))
############################# END Third section ################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())