
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'es.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import numpy as np
global a
import glob, os, os.path
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900,600)
        MainWindow.setStyleSheet("background-color: #005bea;")
        MainWindow.setWindowIcon(QIcon("C:\\Users\HASSAN\Desktop\doc.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        
        # Get screen geometry
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        screen_center = screen_geometry.center()

        frame_width = screen_geometry.width() * 8 // 10  # Integer division
        frame_height = screen_geometry.height() * 6 // 10  # Integer division

        # Get the frame position to center it
        frame_x = screen_center.x() - frame_width // 2
        frame_y = screen_center.y() - frame_height // 2
        
        self.frame.setGeometry(QtCore.QRect(frame_x, frame_y, frame_width, frame_height))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.630318, y1:0.392, x2:0.068, y2:0, stop:0.551136 #4facfe, stop:1 #00f2fe);\n"
                                 "border-radius: 25px;\n"
                                 "border: 2px solid #00c6fb;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.image_dir = "C://Users/HASSAN/OneDrive/Python/test"  # Define image directory
        