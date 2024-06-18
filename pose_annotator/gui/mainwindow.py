# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pose_annotator.gui.custom_widgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1397, 896)
        self.actionOpen_image = QAction(MainWindow)
        self.actionOpen_image.setObjectName(u"actionOpen_image")
        self.actionOpen_image_directory = QAction(MainWindow)
        self.actionOpen_image_directory.setObjectName(u"actionOpen_image_directory")
        self.actionOpen_video = QAction(MainWindow)
        self.actionOpen_video.setObjectName(u"actionOpen_video")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Add the new UI elements for labeling frames
        self.individualLabelLayout = QHBoxLayout()
        self.individualLabelLayout.setObjectName(u"individualLabelLayout")
        self.labelLabel = QLabel(self.centralwidget)
        self.labelLabel.setText("Assign Label to Current Frame:")
        self.individualLabelLayout.addWidget(self.labelLabel)
        self.labelComboBox = QComboBox(self.centralwidget)
        self.individualLabelLayout.addWidget(self.labelComboBox)
        self.verticalLayout.addLayout(self.individualLabelLayout)

        self.bulkLabelLayout = QHBoxLayout()
        self.bulkLabelLayout.setObjectName(u"bulkLabelLayout")
        self.bulkLabel = QLabel(self.centralwidget)
        self.bulkLabel.setText("Assign Label to Frames:")
        self.bulkLabelLayout.addWidget(self.bulkLabel)
        self.bulkLabelComboBox = QComboBox(self.centralwidget)
        self.bulkLabelLayout.addWidget(self.bulkLabelComboBox)
        self.startFrameEdit = QLineEdit(self.centralwidget)
        self.startFrameEdit.setPlaceholderText("Start Frame")
        self.bulkLabelLayout.addWidget(self.startFrameEdit)
        self.endFrameEdit = QLineEdit(self.centralwidget)
        self.endFrameEdit.setPlaceholderText("End Frame")
        self.bulkLabelLayout.addWidget(self.endFrameEdit)
        self.bulkAssignButton = QPushButton(self.centralwidget)
        self.bulkAssignButton.setText("Assign")
        self.bulkLabelLayout.addWidget(self.bulkAssignButton)
        self.bulkLabelCheckBox = QCheckBox(self.centralwidget)
        self.bulkLabelCheckBox.setText("Enable Bulk Labeling")
        self.bulkLabelLayout.addWidget(self.bulkLabelCheckBox)
        self.verticalLayout.addLayout(self.bulkLabelLayout)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = VideoPlayer(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout.setStretch(1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1397, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen_image_or_video = QMenu(self.menubar)
        self.menuOpen_image_or_video.setObjectName(u"menuOpen_image_or_video")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOpen_image_or_video.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuOpen_image_or_video.addAction(self.actionOpen_image)
        self.menuOpen_image_or_video.addAction(self.actionOpen_image_directory)
        self.menuOpen_image_or_video.addAction(self.actionOpen_video)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_image.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.actionOpen_image_directory.setText(QCoreApplication.translate("MainWindow", u"Open image directory", None))
        self.actionOpen_video.setText(QCoreApplication.translate("MainWindow", u"Open video", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpen_image_or_video.setTitle(QCoreApplication.translate("MainWindow", u"Open image or video", None))