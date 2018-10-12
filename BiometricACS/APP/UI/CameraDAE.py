# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Delpro\Desktop\ui\CameraDAE.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowCameraDAE(object):
    def setupUi(self, WindowCameraDAE):
        WindowCameraDAE.setObjectName("WindowCameraDAE")
        WindowCameraDAE.resize(320, 214)
        WindowCameraDAE.setMaximumSize(QtCore.QSize(350, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\APP\Sources\Icons\Program.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WindowCameraDAE.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(WindowCameraDAE)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(WindowCameraDAE)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(WindowCameraDAE)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(WindowCameraDAE)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(WindowCameraDAE)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(WindowCameraDAE)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(WindowCameraDAE)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(WindowCameraDAE)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(WindowCameraDAE)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(WindowCameraDAE)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(WindowCameraDAE)
        QtCore.QMetaObject.connectSlotsByName(WindowCameraDAE)

    def retranslateUi(self, WindowCameraDAE):
        _translate = QtCore.QCoreApplication.translate
        WindowCameraDAE.setWindowTitle(_translate("WindowCameraDAE", "BACS Camera"))
        self.pushButton.setText(_translate("WindowCameraDAE", "Ok"))
        self.pushButton_2.setText(_translate("WindowCameraDAE", "Cancel"))
        self.label.setText(_translate("WindowCameraDAE", "Checkpoint:"))
        self.label_2.setText(_translate("WindowCameraDAE", "Vector:"))
        self.label_3.setText(_translate("WindowCameraDAE", "Device:"))
        self.label_4.setText(_translate("WindowCameraDAE", "Camera"))

