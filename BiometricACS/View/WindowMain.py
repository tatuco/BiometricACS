# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\BiometricACS\BiometricACS\View\WindowMain.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\Source\Program.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabPresenter = QtWidgets.QTabWidget(self.centralwidget)
        self.tabPresenter.setAutoFillBackground(True)
        self.tabPresenter.setObjectName("tabPresenter")
        self.tabCheckpoints = QtWidgets.QWidget()
        self.tabCheckpoints.setAutoFillBackground(True)
        self.tabCheckpoints.setObjectName("tabCheckpoints")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabCheckpoints)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gbVideoStream = QtWidgets.QGroupBox(self.tabCheckpoints)
        self.gbVideoStream.setObjectName("gbVideoStream")
        self.gridLayout = QtWidgets.QGridLayout(self.gbVideoStream)
        self.gridLayout.setObjectName("gridLayout")
        self.gvLandmarksDetection = QtWidgets.QGraphicsView(self.gbVideoStream)
        self.gvLandmarksDetection.setObjectName("gvLandmarksDetection")
        self.gridLayout.addWidget(self.gvLandmarksDetection, 0, 1, 1, 1)
        self.gvFaceDetection = QtWidgets.QGraphicsView(self.gbVideoStream)
        self.gvFaceDetection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gvFaceDetection.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gvFaceDetection.setObjectName("gvFaceDetection")
        self.gridLayout.addWidget(self.gvFaceDetection, 0, 0, 2, 1)
        self.gvFaceNormalization = QtWidgets.QGraphicsView(self.gbVideoStream)
        self.gvFaceNormalization.setObjectName("gvFaceNormalization")
        self.gridLayout.addWidget(self.gvFaceNormalization, 1, 1, 1, 1)
        self.lblDetectedName = QtWidgets.QLabel(self.gbVideoStream)
        self.lblDetectedName.setObjectName("lblDetectedName")
        self.gridLayout.addWidget(self.lblDetectedName, 2, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout_3.addWidget(self.gbVideoStream, 0, 1, 1, 1)
        self.gbControlPanel = QtWidgets.QGroupBox(self.tabCheckpoints)
        self.gbControlPanel.setObjectName("gbControlPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbControlPanel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGetAccess = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnGetAccess.setObjectName("btnGetAccess")
        self.horizontalLayout_2.addWidget(self.btnGetAccess)
        self.btnSaveFace = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnSaveFace.setObjectName("btnSaveFace")
        self.horizontalLayout_2.addWidget(self.btnSaveFace)
        self.btnLockCheckpoint = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnLockCheckpoint.setObjectName("btnLockCheckpoint")
        self.horizontalLayout_2.addWidget(self.btnLockCheckpoint)
        self.btnUnlockCheckpoint = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnUnlockCheckpoint.setObjectName("btnUnlockCheckpoint")
        self.horizontalLayout_2.addWidget(self.btnUnlockCheckpoint)
        self.gridLayout_3.addWidget(self.gbControlPanel, 1, 1, 1, 1)
        self.gbCameras = QtWidgets.QGroupBox(self.tabCheckpoints)
        self.gbCameras.setAutoFillBackground(False)
        self.gbCameras.setObjectName("gbCameras")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbCameras)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeCameras = QtWidgets.QTreeWidget(self.gbCameras)
        self.treeCameras.setObjectName("treeCameras")
        self.treeCameras.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.treeCameras)
        self.gridLayout_3.addWidget(self.gbCameras, 0, 0, 2, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.tabPresenter.addTab(self.tabCheckpoints, "")
        self.tabSessionLog = QtWidgets.QWidget()
        self.tabSessionLog.setAutoFillBackground(True)
        self.tabSessionLog.setObjectName("tabSessionLog")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabSessionLog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lvVisitsLog = QtWidgets.QListView(self.tabSessionLog)
        self.lvVisitsLog.setObjectName("lvVisitsLog")
        self.gridLayout_4.addWidget(self.lvVisitsLog, 0, 0, 2, 2)
        self.tabPresenter.addTab(self.tabSessionLog, "")
        self.tabStatistics = QtWidgets.QWidget()
        self.tabStatistics.setObjectName("tabStatistics")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabStatistics)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tbSearchName = QtWidgets.QLineEdit(self.tabStatistics)
        self.tbSearchName.setObjectName("tbSearchName")
        self.gridLayout_5.addWidget(self.tbSearchName, 0, 0, 1, 1)
        self.btnSaveStatistics = QtWidgets.QPushButton(self.tabStatistics)
        self.btnSaveStatistics.setObjectName("btnSaveStatistics")
        self.gridLayout_5.addWidget(self.btnSaveStatistics, 0, 1, 1, 1)
        self.tableStatistics = QtWidgets.QTableWidget(self.tabStatistics)
        self.tableStatistics.setObjectName("tableStatistics")
        self.tableStatistics.setColumnCount(0)
        self.tableStatistics.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableStatistics, 1, 0, 1, 2)
        self.tabPresenter.addTab(self.tabStatistics, "")
        self.gridLayout_2.addWidget(self.tabPresenter, 0, 0, 3, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubarMain = QtWidgets.QMenuBar(MainWindow)
        self.menubarMain.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubarMain.setObjectName("menubarMain")
        self.mFile = QtWidgets.QMenu(self.menubarMain)
        self.mFile.setObjectName("mFile")
        self.menuExport = QtWidgets.QMenu(self.mFile)
        self.menuExport.setObjectName("menuExport")
        self.menuControl = QtWidgets.QMenu(self.menubarMain)
        self.menuControl.setObjectName("menuControl")
        self.menuSettings = QtWidgets.QMenu(self.menuControl)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAccounts = QtWidgets.QMenu(self.menuControl)
        self.menuAccounts.setObjectName("menuAccounts")
        self.menuData = QtWidgets.QMenu(self.menuControl)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubarMain)
        self.statusbarCurrentEvent = QtWidgets.QStatusBar(MainWindow)
        self.statusbarCurrentEvent.setObjectName("statusbarCurrentEvent")
        MainWindow.setStatusBar(self.statusbarCurrentEvent)
        self.actionExportSessionLog = QtWidgets.QAction(MainWindow)
        self.actionExportSessionLog.setObjectName("actionExportSessionLog")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpenSettiongs = QtWidgets.QAction(MainWindow)
        self.actionOpenSettiongs.setObjectName("actionOpenSettiongs")
        self.actionImportSettings = QtWidgets.QAction(MainWindow)
        self.actionImportSettings.setObjectName("actionImportSettings")
        self.actionExportSettings = QtWidgets.QAction(MainWindow)
        self.actionExportSettings.setObjectName("actionExportSettings")
        self.actionRelogin = QtWidgets.QAction(MainWindow)
        self.actionRelogin.setObjectName("actionRelogin")
        self.actionOpenSettings = QtWidgets.QAction(MainWindow)
        self.actionOpenSettings.setObjectName("actionOpenSettings")
        self.actionImportSettings1 = QtWidgets.QAction(MainWindow)
        self.actionImportSettings1.setObjectName("actionImportSettings1")
        self.actionExportSettings1 = QtWidgets.QAction(MainWindow)
        self.actionExportSettings1.setObjectName("actionExportSettings1")
        self.actionRelogin1 = QtWidgets.QAction(MainWindow)
        self.actionRelogin1.setObjectName("actionRelogin1")
        self.actionExport_Accounts = QtWidgets.QAction(MainWindow)
        self.actionExport_Accounts.setObjectName("actionExport_Accounts")
        self.actionCreateAccount = QtWidgets.QAction(MainWindow)
        self.actionCreateAccount.setObjectName("actionCreateAccount")
        self.actionAddBbiometricsData = QtWidgets.QAction(MainWindow)
        self.actionAddBbiometricsData.setObjectName("actionAddBbiometricsData")
        self.actionBackingUpData = QtWidgets.QAction(MainWindow)
        self.actionBackingUpData.setObjectName("actionBackingUpData")
        self.menuExport.addAction(self.actionExportSessionLog)
        self.mFile.addAction(self.menuExport.menuAction())
        self.mFile.addSeparator()
        self.mFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionOpenSettings)
        self.menuSettings.addAction(self.actionImportSettings)
        self.menuSettings.addAction(self.actionExportSettings)
        self.menuAccounts.addAction(self.actionRelogin)
        self.menuAccounts.addAction(self.actionCreateAccount)
        self.menuAccounts.addAction(self.actionExport_Accounts)
        self.menuData.addAction(self.actionAddBbiometricsData)
        self.menuData.addAction(self.actionBackingUpData)
        self.menuControl.addAction(self.menuData.menuAction())
        self.menuControl.addAction(self.menuSettings.menuAction())
        self.menuControl.addAction(self.menuAccounts.menuAction())
        self.menubarMain.addAction(self.mFile.menuAction())
        self.menubarMain.addAction(self.menuControl.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPresenter.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnGetAccess, self.btnSaveFace)
        MainWindow.setTabOrder(self.btnSaveFace, self.btnLockCheckpoint)
        MainWindow.setTabOrder(self.btnLockCheckpoint, self.btnUnlockCheckpoint)
        MainWindow.setTabOrder(self.btnUnlockCheckpoint, self.gvLandmarksDetection)
        MainWindow.setTabOrder(self.gvLandmarksDetection, self.tabPresenter)
        MainWindow.setTabOrder(self.tabPresenter, self.gvFaceDetection)
        MainWindow.setTabOrder(self.gvFaceDetection, self.lvVisitsLog)
        MainWindow.setTabOrder(self.lvVisitsLog, self.gvFaceNormalization)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BACS Control Panel"))
        self.gbVideoStream.setTitle(_translate("MainWindow", "Video Stream"))
        self.lblDetectedName.setText(_translate("MainWindow", "Detected Name:"))
        self.gbControlPanel.setTitle(_translate("MainWindow", "Control Panel"))
        self.btnGetAccess.setText(_translate("MainWindow", "Get Access"))
        self.btnSaveFace.setText(_translate("MainWindow", "Save Face"))
        self.btnLockCheckpoint.setText(_translate("MainWindow", "Lock Checkpoint"))
        self.btnUnlockCheckpoint.setText(_translate("MainWindow", "Unlock Checkpoint"))
        self.gbCameras.setTitle(_translate("MainWindow", "Cameras"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabCheckpoints), _translate("MainWindow", "Сheckpoints"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabSessionLog), _translate("MainWindow", "Session log"))
        self.btnSaveStatistics.setText(_translate("MainWindow", "Save"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabStatistics), _translate("MainWindow", "Statistics"))
        self.mFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAccounts.setTitle(_translate("MainWindow", "Accounts"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.actionExportSessionLog.setText(_translate("MainWindow", "Session log"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpenSettiongs.setText(_translate("MainWindow", "Open"))
        self.actionImportSettings.setText(_translate("MainWindow", "Import"))
        self.actionExportSettings.setText(_translate("MainWindow", "Export"))
        self.actionRelogin.setText(_translate("MainWindow", "Relogin"))
        self.actionOpenSettings.setText(_translate("MainWindow", "Open"))
        self.actionImportSettings1.setText(_translate("MainWindow", "Import"))
        self.actionExportSettings1.setText(_translate("MainWindow", "Export"))
        self.actionRelogin1.setText(_translate("MainWindow", "Relogin"))
        self.actionExport_Accounts.setText(_translate("MainWindow", "Export Accounts"))
        self.actionCreateAccount.setText(_translate("MainWindow", "Create"))
        self.actionAddBbiometricsData.setText(_translate("MainWindow", "Add biometrics data"))
        self.actionBackingUpData.setText(_translate("MainWindow", "Backing up data"))

