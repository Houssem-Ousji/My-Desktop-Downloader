# import pyqt5 libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

#import os and sys
import sys
from os import path

import urllib.request

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

    # Saving and Showing the path
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




def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()

if __name__ == '__main__' :
    main()
