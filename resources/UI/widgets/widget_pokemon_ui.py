# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_pokemon.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 174)
        Form.setMaximumSize(QSize(16777215, 174))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bg = QFrame(Form)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"#bg {\n"
"	background-color: qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.506, y2:0, stop:0 rgba(168, 0, 168, 255), stop:1 rgba(255, 170, 255, 255));\n"
"border-radius: 18px;\n"
"}\n"
"")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.bg)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 62))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_name = QLabel(self.frame_3)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"#label_name {\n"
"color: white;\n"
"font-size: 20px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_name)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_id = QLabel(self.frame_4)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setStyleSheet(u"#label_id {\n"
"color: #536fca;\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_id)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.bg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.type_1 = QPushButton(self.frame_5)
        self.type_1.setObjectName(u"type_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_1.sizePolicy().hasHeightForWidth())
        self.type_1.setSizePolicy(sizePolicy)
        self.type_1.setMaximumSize(QSize(16777215, 25))
        self.type_1.setStyleSheet(u"#type_1 {\n"
"background-color: rgb(71, 141, 212);\n"
"color: white;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.type_1)

        self.type_2 = QPushButton(self.frame_5)
        self.type_2.setObjectName(u"type_2")
        sizePolicy.setHeightForWidth(self.type_2.sizePolicy().hasHeightForWidth())
        self.type_2.setSizePolicy(sizePolicy)
        self.type_2.setMaximumSize(QSize(16777215, 25))
        self.type_2.setStyleSheet(u"#type_2 {\n"
"background-color: rgb(94, 62, 113);\n"
"color: white;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.type_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.artwork = QLabel(self.frame_6)
        self.artwork.setObjectName(u"artwork")
        self.artwork.setMaximumSize(QSize(90, 90))
        self.artwork.setPixmap(QPixmap(u"../../icons/img pokemon/007.png"))
        self.artwork.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.artwork)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.bg)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"Bulbasaur", None))
        self.label_id.setText(QCoreApplication.translate("Form", u"#0001", None))
        self.type_1.setText(QCoreApplication.translate("Form", u"Planta", None))
        self.type_2.setText(QCoreApplication.translate("Form", u"Veneno", None))
        self.artwork.setText("")
    # retranslateUi

