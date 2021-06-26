# import pyqt5 libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

#import os and sys
import sys
from os import path

import urllib.request
import pafy
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
    # Saving and Showing the path of the seconb section
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
############################# END first section ################################








def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()

if __name__ == '__main__' :
    main()
