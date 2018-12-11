# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\BiometricACS\BiometricACS\APP\UI\WindowMain.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabPresenter = QtWidgets.QTabWidget(self.centralwidget)
        self.tabPresenter.setAutoFillBackground(False)
        self.tabPresenter.setObjectName("tabPresenter")
        self.tabCheckpoints = QtWidgets.QWidget()
        self.tabCheckpoints.setAutoFillBackground(False)
        self.tabCheckpoints.setObjectName("tabCheckpoints")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabCheckpoints)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_4 = QtWidgets.QSplitter(self.tabCheckpoints)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.gbCameras = QtWidgets.QGroupBox(self.splitter_4)
        self.gbCameras.setAutoFillBackground(False)
        self.gbCameras.setObjectName("gbCameras")
        self.gridLayout = QtWidgets.QGridLayout(self.gbCameras)
        self.gridLayout.setObjectName("gridLayout")
        self.treeCameras = QtWidgets.QTreeWidget(self.gbCameras)
        self.treeCameras.setObjectName("treeCameras")
        self.treeCameras.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeCameras, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.gbVideoStream = QtWidgets.QGroupBox(self.splitter)
        self.gbVideoStream.setObjectName("gbVideoStream")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbVideoStream)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_3 = QtWidgets.QSplitter(self.gbVideoStream)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.gvFaceDetection = QtWidgets.QLabel(self.splitter_3)
        self.gvFaceDetection.setText("")
        self.gvFaceDetection.setObjectName("gvFaceDetection")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.gvLandmarksDetection = QtWidgets.QLabel(self.splitter_2)
        self.gvLandmarksDetection.setText("")
        self.gvLandmarksDetection.setObjectName("gvLandmarksDetection")
        self.gvFaceNormalization = QtWidgets.QLabel(self.splitter_2)
        self.gvFaceNormalization.setText("")
        self.gvFaceNormalization.setObjectName("gvFaceNormalization")
        self.gridLayout_3.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.lblDetectedName = QtWidgets.QLabel(self.gbVideoStream)
        self.lblDetectedName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblDetectedName.setObjectName("lblDetectedName")
        self.gridLayout_3.addWidget(self.lblDetectedName, 1, 0, 1, 1)
        self.gbControlPanel = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbControlPanel.sizePolicy().hasHeightForWidth())
        self.gbControlPanel.setSizePolicy(sizePolicy)
        self.gbControlPanel.setMaximumSize(QtCore.QSize(16777215, 56))
        self.gbControlPanel.setObjectName("gbControlPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbControlPanel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGetAccess = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnGetAccess.setObjectName("btnGetAccess")
        self.horizontalLayout_2.addWidget(self.btnGetAccess)
        self.btnLockCheckpoint = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnLockCheckpoint.setObjectName("btnLockCheckpoint")
        self.horizontalLayout_2.addWidget(self.btnLockCheckpoint)
        self.btnUnlockCheckpoint = QtWidgets.QPushButton(self.gbControlPanel)
        self.btnUnlockCheckpoint.setObjectName("btnUnlockCheckpoint")
        self.horizontalLayout_2.addWidget(self.btnUnlockCheckpoint)
        self.gridLayout_6.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.tabPresenter.addTab(self.tabCheckpoints, "")
        self.tabSessionLog = QtWidgets.QWidget()
        self.tabSessionLog.setAutoFillBackground(True)
        self.tabSessionLog.setObjectName("tabSessionLog")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabSessionLog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lvVisitsLog = QtWidgets.QListWidget(self.tabSessionLog)
        self.lvVisitsLog.setObjectName("lvVisitsLog")
        self.gridLayout_4.addWidget(self.lvVisitsLog, 0, 0, 2, 2)
        self.tabPresenter.addTab(self.tabSessionLog, "")
        self.tabStatistics = QtWidgets.QWidget()
        self.tabStatistics.setAutoFillBackground(False)
        self.tabStatistics.setObjectName("tabStatistics")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabStatistics)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_5 = QtWidgets.QSplitter(self.tabStatistics)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblDepartment = QtWidgets.QLabel(self.layoutWidget)
        self.lblDepartment.setObjectName("lblDepartment")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblDepartment)
        self.cmb_department = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_department.setObjectName("cmb_department")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_department)
        self.lblCheif = QtWidgets.QLabel(self.layoutWidget)
        self.lblCheif.setObjectName("lblCheif")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCheif)
        self.lbl_chief = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_chief.setAutoFillBackground(True)
        self.lbl_chief.setText("")
        self.lbl_chief.setObjectName("lbl_chief")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_chief)
        self.lblFirstName = QtWidgets.QLabel(self.layoutWidget)
        self.lblFirstName.setObjectName("lblFirstName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblFirstName)
        self.tb_first_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.tb_first_name.setObjectName("tb_first_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tb_first_name)
        self.lblLastName = QtWidgets.QLabel(self.layoutWidget)
        self.lblLastName.setObjectName("lblLastName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblLastName)
        self.tb_last_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.tb_last_name.setObjectName("tb_last_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tb_last_name)
        self.lblCheckpoint = QtWidgets.QLabel(self.layoutWidget)
        self.lblCheckpoint.setObjectName("lblCheckpoint")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblCheckpoint)
        self.cmb_checkpoint = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_checkpoint.setObjectName("cmb_checkpoint")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmb_checkpoint)
        self.lblEvent = QtWidgets.QLabel(self.layoutWidget)
        self.lblEvent.setObjectName("lblEvent")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblEvent)
        self.cmb_event = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_event.setObjectName("cmb_event")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cmb_event)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.rbtn_considering_time = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtn_considering_time.setObjectName("rbtn_considering_time")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.rbtn_considering_time)
        self.lblStartDate = QtWidgets.QLabel(self.layoutWidget)
        self.lblStartDate.setObjectName("lblStartDate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblStartDate)
        self.lbl_start_date = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_start_date.setAutoFillBackground(True)
        self.lbl_start_date.setText("")
        self.lbl_start_date.setObjectName("lbl_start_date")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_start_date)
        self.lblStopDate = QtWidgets.QLabel(self.layoutWidget)
        self.lblStopDate.setObjectName("lblStopDate")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblStopDate)
        self.lbl_stop_date = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_stop_date.setAutoFillBackground(True)
        self.lbl_stop_date.setText("")
        self.lbl_stop_date.setObjectName("lbl_stop_date")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_stop_date)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.wgt_calendar = QtWidgets.QCalendarWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt_calendar.sizePolicy().hasHeightForWidth())
        self.wgt_calendar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.wgt_calendar.setFont(font)
        self.wgt_calendar.setGridVisible(True)
        self.wgt_calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.wgt_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.wgt_calendar.setNavigationBarVisible(True)
        self.wgt_calendar.setDateEditEnabled(False)
        self.wgt_calendar.setObjectName("wgt_calendar")
        self.horizontalLayout_3.addWidget(self.wgt_calendar)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblFountRecors = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFountRecors.sizePolicy().hasHeightForWidth())
        self.lblFountRecors.setSizePolicy(sizePolicy)
        self.lblFountRecors.setObjectName("lblFountRecors")
        self.horizontalLayout.addWidget(self.lblFountRecors)
        self.lbl_found_records = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_found_records.setAutoFillBackground(False)
        self.lbl_found_records.setText("")
        self.lbl_found_records.setObjectName("lbl_found_records")
        self.horizontalLayout.addWidget(self.lbl_found_records)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.btn_search_statistics = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_search_statistics.setObjectName("btn_search_statistics")
        self.horizontalLayout_4.addWidget(self.btn_search_statistics)
        self.btn_clear = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.btn_save_statistict = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_statistict.sizePolicy().hasHeightForWidth())
        self.btn_save_statistict.setSizePolicy(sizePolicy)
        self.btn_save_statistict.setObjectName("btn_save_statistict")
        self.horizontalLayout_4.addWidget(self.btn_save_statistict)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableStatistics = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableStatistics.setObjectName("tableStatistics")
        self.tableStatistics.setColumnCount(0)
        self.tableStatistics.setRowCount(0)
        self.verticalLayout.addWidget(self.tableStatistics)
        self.gridLayout_5.addWidget(self.splitter_5, 0, 0, 1, 1)
        self.tabPresenter.addTab(self.tabStatistics, "")
        self.gridLayout_2.addWidget(self.tabPresenter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubarMain = QtWidgets.QMenuBar(MainWindow)
        self.menubarMain.setGeometry(QtCore.QRect(0, 0, 996, 21))
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
        self.menuCheckpoints = QtWidgets.QMenu(self.menuControl)
        self.menuCheckpoints.setObjectName("menuCheckpoints")
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
        self.actionExport_Accounts = QtWidgets.QAction(MainWindow)
        self.actionExport_Accounts.setObjectName("actionExport_Accounts")
        self.actionCreateAccount = QtWidgets.QAction(MainWindow)
        self.actionCreateAccount.setObjectName("actionCreateAccount")
        self.actionAddBbiometricsData = QtWidgets.QAction(MainWindow)
        self.actionAddBbiometricsData.setObjectName("actionAddBbiometricsData")
        self.actionBackingUpData = QtWidgets.QAction(MainWindow)
        self.actionBackingUpData.setObjectName("actionBackingUpData")
        self.actionAddCheckpoint = QtWidgets.QAction(MainWindow)
        self.actionAddCheckpoint.setObjectName("actionAddCheckpoint")
        self.actionAddCamera = QtWidgets.QAction(MainWindow)
        self.actionAddCamera.setObjectName("actionAddCamera")
        self.actionDeleteCamera = QtWidgets.QAction(MainWindow)
        self.actionDeleteCamera.setObjectName("actionDeleteCamera")
        self.menuExport.addAction(self.actionExportSessionLog)
        self.mFile.addAction(self.menuExport.menuAction())
        self.mFile.addSeparator()
        self.mFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionOpenSettings)
        self.menuSettings.addAction(self.actionExportSettings)
        self.menuAccounts.addAction(self.actionRelogin)
        self.menuAccounts.addAction(self.actionCreateAccount)
        self.menuAccounts.addAction(self.actionExport_Accounts)
        self.menuData.addAction(self.actionAddBbiometricsData)
        self.menuData.addAction(self.actionBackingUpData)
        self.menuCheckpoints.addAction(self.actionAddCheckpoint)
        self.menuCheckpoints.addAction(self.actionAddCamera)
        self.menuControl.addAction(self.menuData.menuAction())
        self.menuControl.addAction(self.menuCheckpoints.menuAction())
        self.menuControl.addAction(self.menuSettings.menuAction())
        self.menuControl.addAction(self.menuAccounts.menuAction())
        self.menubarMain.addAction(self.mFile.menuAction())
        self.menubarMain.addAction(self.menuControl.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPresenter.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnGetAccess, self.btnLockCheckpoint)
        MainWindow.setTabOrder(self.btnLockCheckpoint, self.btnUnlockCheckpoint)
        MainWindow.setTabOrder(self.btnUnlockCheckpoint, self.lvVisitsLog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BACS Control Panel"))
        self.gbCameras.setTitle(_translate("MainWindow", "Cameras"))
        self.gbVideoStream.setTitle(_translate("MainWindow", "Video Stream"))
        self.lblDetectedName.setText(_translate("MainWindow", "Detected Name:"))
        self.gbControlPanel.setTitle(_translate("MainWindow", "Control Panel"))
        self.btnGetAccess.setText(_translate("MainWindow", "Get Access"))
        self.btnLockCheckpoint.setText(_translate("MainWindow", "Lock Checkpoint"))
        self.btnUnlockCheckpoint.setText(_translate("MainWindow", "Unlock Checkpoint"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabCheckpoints), _translate("MainWindow", "Сheckpoints"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabSessionLog), _translate("MainWindow", "Session log"))
        self.lblDepartment.setText(_translate("MainWindow", "Department:"))
        self.lblCheif.setText(_translate("MainWindow", "Chief:"))
        self.lblFirstName.setText(_translate("MainWindow", "First name:"))
        self.lblLastName.setText(_translate("MainWindow", "Last name:"))
        self.lblCheckpoint.setText(_translate("MainWindow", "Checkpoint:"))
        self.lblEvent.setText(_translate("MainWindow", "Event:"))
        self.rbtn_considering_time.setText(_translate("MainWindow", "Considering time"))
        self.lblStartDate.setText(_translate("MainWindow", "Start date:"))
        self.lblStopDate.setText(_translate("MainWindow", "Stop date:"))
        self.lblFountRecors.setText(_translate("MainWindow", "Found records:"))
        self.btn_search_statistics.setText(_translate("MainWindow", "Search"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_save_statistict.setText(_translate("MainWindow", "Save"))
        self.tabPresenter.setTabText(self.tabPresenter.indexOf(self.tabStatistics), _translate("MainWindow", "Statistics"))
        self.mFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAccounts.setTitle(_translate("MainWindow", "Accounts"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuCheckpoints.setTitle(_translate("MainWindow", "Checkpoints"))
        self.actionExportSessionLog.setText(_translate("MainWindow", "Session log"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpenSettiongs.setText(_translate("MainWindow", "Open"))
        self.actionImportSettings.setText(_translate("MainWindow", "Import"))
        self.actionExportSettings.setText(_translate("MainWindow", "Export"))
        self.actionRelogin.setText(_translate("MainWindow", "Relogin"))
        self.actionOpenSettings.setText(_translate("MainWindow", "Open"))
        self.actionExport_Accounts.setText(_translate("MainWindow", "Export Accounts"))
        self.actionCreateAccount.setText(_translate("MainWindow", "Create"))
        self.actionAddBbiometricsData.setText(_translate("MainWindow", "Add biometrics data"))
        self.actionBackingUpData.setText(_translate("MainWindow", "Backing up data"))
        self.actionAddCheckpoint.setText(_translate("MainWindow", "Add checkpoint"))
        self.actionAddCamera.setText(_translate("MainWindow", "Add camera"))
        self.actionDeleteCamera.setText(_translate("MainWindow", "Delete camera"))

