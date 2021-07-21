
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
        
        self.slctimg = QtWidgets.QPushButton(self.frame)
        self.slctimg.setGeometry(QtCore.QRect(600, 10, 171, 61))
        self.slctimg.setStyleSheet("color:white;\n"
                                   "font: 14pt \"Gadugi\";\n"
                                   "border-radius: 20px;\n"
                                   "border: 2px solid #00c6fb;\n"
                                   "background-color:#005bea;")
      
        self.slctimg.setObjectName("slctimg")
        
        self.rgbtgray = QtWidgets.QPushButton(self.frame)
        self.rgbtgray.setGeometry(QtCore.QRect(600, 80, 171, 61))
        self.rgbtgray.setStyleSheet("color:white;\n"
                                    "font: 14pt \"Gadugi\";\n"
                                    "   border-radius: 20px;\n"
                                    "    border: 2px solid #00c6fb;\n"
                                    "background-color:#005bea;\n"
                                    "width:171px;\n"
                                    "height:61px;")
        self.rgbtgray.setObjectName("rgbtgray")
        self.bilfil = QtWidgets.QPushButton(self.frame)
        self.bilfil.setGeometry(QtCore.QRect(600, 150, 171, 61))
        self.bilfil.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.bilfil.setObjectName("bilfil")
        self.medfil = QtWidgets.QPushButton(self.frame)
        self.medfil.setGeometry(QtCore.QRect(600, 220, 171, 61))
        self.medfil.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.medfil.setObjectName("medfil")
        self.gaufil = QtWidgets.QPushButton(self.frame)
        self.gaufil.setGeometry(QtCore.QRect(390, 150, 111, 41))
        self.gaufil.setStyleSheet("background-color: #008CBA;\n"
                                  "text-align: center;\n"
                                  "\n"
                                  "")
        self.gaufil.setObjectName("gaufil")
        self.thres = QtWidgets.QPushButton(self.frame)
        self.thres.setGeometry(QtCore.QRect(600, 290, 171, 61))
        self.thres.setStyleSheet("color:white;\n"
                                 "font: 14pt \"Gadugi\";\n"
                                 "   border-radius: 20px;\n"
                                 "    border: 2px solid #00c6fb;\n"
                                 "background-color:#005bea;\n"
                                 "width:171px;\n"
                                 "height:61px;")
        self.thres.setObjectName("thres")
        self.dilate = QtWidgets.QPushButton(self.frame)
        self.dilate.setGeometry(QtCore.QRect(600, 360, 171, 61))
        self.dilate.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.dilate.setObjectName("dilate")
        self.morpho = QtWidgets.QPushButton(self.frame)
        self.morpho.setGeometry(QtCore.QRect(600, 430, 171, 61))
        self.morpho.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.morpho.setObjectName("morpho")
        self.addcol = QtWidgets.QPushButton(self.frame)
        self.addcol.setGeometry(QtCore.QRect(600, 500, 171, 61))
        self.addcol.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.addcol.setObjectName("addcol")
        self.savimg = QtWidgets.QPushButton(self.frame)