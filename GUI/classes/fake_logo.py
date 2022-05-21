import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QFileDialog
# from classes.home import HomeScreen
from classes.smart_desk import SmartDesk
from classes.object_motion import ObjectMotionPre
from global_var import widget, fakeLogo_file, PRESSED_STYLE, DEFAULT_STYLE



class FakeLogoDet(QDialog):
    def __init__(self):
        super(FakeLogoDet, self).__init__()
        self.cameraon = False
        self.photouploadon = False
        self.fname = ["", ""]
        loadUi(fakeLogo_file, self)
        self.backButton.clicked.connect(self.backward)
        self.camera.clicked.connect(self.opencamera)
        self.uploadFile.clicked.connect(self.upload)
        self.startButton.clicked.connect(self.start)

    def opencamera(self):
        if self.cameraon:
            self.reset()
        else:
            self.photouploadon = False
            self.cameraon = True
            self.uploadFile.setStyleSheet(DEFAULT_STYLE)
            self.camera.setStyleSheet(PRESSED_STYLE)
            self.error.setText("")
            self.file_name.setText("")

    def upload(self):
        if self.photouploadon:
            self.reset()
        else:
            self.cameraon = False
            self.photouploadon = True
            self.camera.setStyleSheet(DEFAULT_STYLE)
            self.uploadFile.setStyleSheet(PRESSED_STYLE)
            self.error.setText("")
            # Open the image from the file explore and define the file name (stored in "self.fname")
            self.fname[0], __ = QFileDialog.getOpenFileName(self, "Upload Images 1", "C:/Users/Arab0/Documents", 'Images(*.PNG *.JPG *.JPEG *.XMP *.RAW *TIFF *.AI)')
            self.fname[1], __ = QFileDialog.getOpenFileName(self, "Upload Images 2", "C:/Users/Arab0/Documents", 'Images(*.PNG *.JPG *.JPEG *.XMP *.RAW *TIFF *.AI)')
            self.file_name.setText(self.fname[0]) # Change the label below the button to the file name
            self.file_name_2.setText(self.fname[1]) # Change the label below the button to the file name

    # "Start" Button Function
    def start(self):
        # Call the real-time feature matching
        if self.cameraon:
            print("Compare using Camera") # <-- The method should be here
        # Call the feature matching between two images
        elif self.photouploadon and len(self.fname) != 0:
            print("Compare between two images") # <-- The method should be here
        # Error massage 
        else:
            self.error.setText("* No argument have been selected")
        self.reset()


    # "Go Back" Button Function, Return back to the home screen
    def backward(self):
        self.reset()
        self.error.setText("")
        widget.setCurrentIndex(widget.currentIndex() -1)


    def reset(self):
        self.file_name.setText("")
        self.fname = ["", ""]
        self.cameraon = False
        self.photouploadon = False
        self.camera.setStyleSheet(DEFAULT_STYLE)
        self.uploadFile.setStyleSheet(DEFAULT_STYLE)

