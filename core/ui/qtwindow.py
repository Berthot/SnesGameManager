# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/allan/PycharmProjects/pyqt/qtwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 417)
        MainWindow.setMaximumSize(QtCore.QSize(750, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listGamesbox = QtWidgets.QListView(self.centralwidget)
        self.listGamesbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listGamesbox.setAutoFillBackground(False)
        self.listGamesbox.setIconSize(QtCore.QSize(120, 100))
        self.listGamesbox.setResizeMode(QtWidgets.QListView.Fixed)
        self.listGamesbox.setViewMode(QtWidgets.QListView.ListMode)
        self.listGamesbox.setUniformItemSizes(True)
        self.listGamesbox.setObjectName("listGamesbox")
        self.verticalLayout.addWidget(self.listGamesbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btPlay = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btPlay.sizePolicy().hasHeightForWidth())
        self.btPlay.setSizePolicy(sizePolicy)
        self.btPlay.setObjectName("btPlay")
        self.horizontalLayout.addWidget(self.btPlay)
        self.btReload = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btReload.sizePolicy().hasHeightForWidth())
        self.btReload.setSizePolicy(sizePolicy)
        self.btReload.setObjectName("btReload")
        self.horizontalLayout.addWidget(self.btReload)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 22))
        self.menubar.setObjectName("menubar")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_roms_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_roms_folder.setObjectName("actionOpen_roms_folder")
        self.actionDownload_Game_Covers = QtWidgets.QAction(MainWindow)
        self.actionDownload_Game_Covers.setObjectName("actionDownload_Game_Covers")
        self.menuOp_es.addSeparator()
        self.menuOp_es.addAction(self.actionOpen_roms_folder)
        self.menuFunctions.addAction(self.actionDownload_Game_Covers)
        self.menubar.addAction(self.menuOp_es.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snes games manager"))
        self.btPlay.setText(_translate("MainWindow", "Play"))
        self.btReload.setText(_translate("MainWindow", "Reload List"))
        self.menuOp_es.setTitle(_translate("MainWindow", "File"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.actionOpen_roms_folder.setText(_translate("MainWindow", "Open roms folder"))
        self.actionOpen_roms_folder.setToolTip(_translate("MainWindow", "Abre o diretorio das roms"))
        self.actionDownload_Game_Covers.setText(_translate("MainWindow", "Download Game Covers"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())