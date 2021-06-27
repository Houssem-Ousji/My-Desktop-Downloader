# import pyqt5 libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

#import os and sys
import sys


import urllib.request
import pafy
from pytube import Playlist
import humanize

ui,_ = loadUiType('Downloader.ui')

class Mainapp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(Mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Ui()
        self.Handle_Buttons()

        #initialize my Progress bars
        self.progressBar_2.setValue(0)
        self.progressBar.setValue(0)
        self.progressBar_5.setValue(0)

        #set the choices in the combobox of the third section (Youtube Playlist)
        self.comboBox_3.addItem("Media type : Audio")
        self.comboBox_3.addItem("Media type : Video")
        self.comboBox_3.addItem("Media type : Normal")

    # Handle ui
    def Handle_Ui(self):
        self.setWindowTitle("My Desktop Downloader")
        self.setFixedSize(771, 361)

    # Handle Buttons
    def Handle_Buttons(self):
        #buttons of the section 1
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
        location = QFileDialog.getSaveFileName(self, caption="Save as", directory="C:/Users/HOUSSEM/Desktop", filter="All files ()")
        self.lineEdit_4.setText(location[0])

    # Making the Progress bar
    def Handle_Progress_Bar_Section_1(self ,  block_number, block_size, total_size):
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
            QMessageBox.warning(self, "Error", "Choose Folder Please")
            self.Browse_section_1()
            path = self.lineEdit_4.text()

        # Make the Download
        try:
            urllib.request.urlretrieve(url, path, self.Handle_Progress_Bar_Section_1)
            QMessageBox.information(self, "Download Done", "successful download")
        except:
            QMessageBox.warning(self, "Download error", "download failed")

        # initializing the inputs and the Progress bar
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.progressBar_2.setValue(0)
############################# END first section ################################

############################# Start Second section ################################
    # Saving and Showing the path of the second section
    def Browse_section_2(self):
        location = QFileDialog.getExistingDirectory(self, caption= "Choose Folder", directory="C:/Users/HOUSSEM/Desktop")
        self.lineEdit_2.setText(location)

    # Our video Quality and the Media type
    def Quality_section_2(self):
        url = self.lineEdit.text()
        test = True
        try:
           video = pafy.new(url)
        except:
            QMessageBox.warning(self, "Error 404", "Url Doesn't exist !")
            self.lineEdit.setText('')
            test = False
        if test == True:
            for Stream in video.allstreams:
               file_size = humanize.naturalsize(Stream.get_filesize())
               video_data = "{} : {} : {} : {}".format(Stream.mediatype, Stream.extension, Stream.quality, file_size)
               self.comboBox.addItem(video_data)

    # Making the Progress bar
    def Handle_Progress_Bar_Section_2(self, *Data_recieved):
        percentage = (Data_recieved[1] / Data_recieved[0]) *100
        self.progressBar.setValue(int(percentage))
        QApplication.processEvents()

    # Download the Youtube Video
    def Handle_Download_Youtube_Video(self):
        url = self.lineEdit.text()
        test = True
        try:
            video = pafy.new(url)
        except:
            QMessageBox.warning(self, "Error 404", "Url Doesn't exist !")
            self.lineEdit.setText('')
            test = False
        if test == True:
            path = self.lineEdit_2.text()
            while path == '':
                QMessageBox.warning(self, "Error", "Choose Folder Please")
                self.Browse_section_2()
                path = self.lineEdit_2.text()
            video_index = self.comboBox.currentIndex()
            try:
                Download = video.allstreams[video_index].download(filepath=path, callback=self.Handle_Progress_Bar_Section_2)
                QMessageBox.information(self, "Download Done", "successful download")
            except:
                QMessageBox.warning(self, "Download error", "download failed")

            # Reset Our Inputs
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.comboBox.clear()
############################# END second section ################################

############################# Start Third section ################################
    # Saving and Showing the path of the Third section
    def Browse_section_3(self):
        location = QFileDialog.getExistingDirectory(self, caption="Choose Folder", directory="C:/Users/HOUSSEM/Desktop")
        self.lineEdit_9.setText(location)

    # Making the Progress bar
    def Handle_Progress_Bar_section_3(self, *Data_recieved):
        percentage = (Data_recieved[1] / Data_recieved[0])*100
        self.progressBar_5.setValue(int(percentage))
        QApplication.processEvents()

    # Download the Youtube Video
    def Handle_Download_Youtube_Playlist(self):
        url = self.lineEdit_10.text()
        path = self.lineEdit_9.text()
        while path == '':
            QMessageBox.warning(self, "Error", "Choose Folder Please")
            self.Browse_section_3()
            path = self.lineEdit_9.text()

        test = True
        test_2 = True
        try:
            My_Playlist = Playlist(url)
        except:
            QMessageBox.warning(self, "Error 404", "Url Doesn't exist !")
            self.lineEdit_10.setText('')
            test = False
        if test:
            for url_video in My_Playlist:
                  try:
                        video = pafy.new(url_video)
                  except:
                        QMessageBox.warning(self,"Error 404", "Download of '{}' Failed".format(video.title))
                        test_2 = False
                  if test_2 and self.comboBox_3.currentIndex() == 0:
                      try:
                          self.lineEdit_11.setText("Downloading {}".format(video.title))
                          Download = video.getbestaudio().download(filepath=path, callback=self.Handle_Progress_Bar_section_3)
                      except:
                          QMessageBox.warning(self, "Error 404", "Download of '{}' Failed".format(video.title))
                  elif test_2 and self.comboBox_3.currentIndex() == 1:
                      try:
                          self.lineEdit_11.setText("Downloading {}".format(video.title))
                          Download = video.getbestvideo().download(filepath=path, callback=self.Handle_Progress_Bar_section_3)
                      except:
                          QMessageBox.warning(self, "Error 404", "Download of '{}' Failed".format(video.title))
                  elif test_2 and self.comboBox_3.currentIndex() == 2:
                      try:
                          self.lineEdit_11.setText("Downloading {}".format(video.title))
                          Download = video._getbest().download(filepath=path, callback=self.Handle_Progress_Bar_section_3)
                      except:
                          QMessageBox.warning(self, "Error 404", "Download of '{}' Failed".format(video.title))
            QMessageBox.information(self, "Download Done", "successful download")
            # Reset The Inputs
            self.lineEdit_10.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_11.setText('')
            self.progressBar_5.setValue(0)
############################# END Third section ################################
def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()

if __name__ == '__main__' :
    main()
