# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\BiometricACS\BiometricACS\APP\UI\WidnowCreateCameraPanel.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wCreateCameraPanel(object):
    def setupUi(self, wCreateCameraPanel):
        wCreateCameraPanel.setObjectName("wCreateCameraPanel")
        wCreateCameraPanel.resize(320, 214)
        wCreateCameraPanel.setMaximumSize(QtCore.QSize(450, 280))
        self.gridLayout = QtWidgets.QGridLayout(wCreateCameraPanel)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(wCreateCameraPanel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblCheckpoint = QtWidgets.QLabel(wCreateCameraPanel)
        self.lblCheckpoint.setObjectName("lblCheckpoint")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCheckpoint)
        self.cmbCheckpoint = QtWidgets.QComboBox(wCreateCameraPanel)
        self.cmbCheckpoint.setObjectName("cmbCheckpoint")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbCheckpoint)
        self.lblVector = QtWidgets.QLabel(wCreateCameraPanel)
        self.lblVector.setObjectName("lblVector")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblVector)
        self.cmbVector = QtWidgets.QComboBox(wCreateCameraPanel)
        self.cmbVector.setObjectName("cmbVector")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbVector)
        self.lblDevice = QtWidgets.QLabel(wCreateCameraPanel)
        self.lblDevice.setObjectName("lblDevice")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblDevice)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbDevice = QtWidgets.QLineEdit(wCreateCameraPanel)
        self.tbDevice.setObjectName("tbDevice")
        self.horizontalLayout_2.addWidget(self.tbDevice)
        self.btnShowDevices = QtWidgets.QPushButton(wCreateCameraPanel)
        self.btnShowDevices.setObjectName("btnShowDevices")
        self.horizontalLayout_2.addWidget(self.btnShowDevices)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnCreate = QtWidgets.QPushButton(wCreateCameraPanel)
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout.addWidget(self.btnCreate)
        self.btnCancel = QtWidgets.QPushButton(wCreateCameraPanel)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.retranslateUi(wCreateCameraPanel)
        QtCore.QMetaObject.connectSlotsByName(wCreateCameraPanel)

    def retranslateUi(self, wCreateCameraPanel):
        _translate = QtCore.QCoreApplication.translate
        wCreateCameraPanel.setWindowTitle(_translate("wCreateCameraPanel", "BACS Camera"))
        self.label_4.setText(_translate("wCreateCameraPanel", "Camera"))
        self.lblCheckpoint.setText(_translate("wCreateCameraPanel", "Checkpoint:"))
        self.lblVector.setText(_translate("wCreateCameraPanel", "Vector:"))
        self.lblDevice.setText(_translate("wCreateCameraPanel", "Device/Ip:"))
        self.btnShowDevices.setText(_translate("wCreateCameraPanel", "Show"))
        self.btnCreate.setText(_translate("wCreateCameraPanel", "Create"))
        self.btnCancel.setText(_translate("wCreateCameraPanel", "Cancel"))

