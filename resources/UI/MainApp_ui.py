# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainApp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 548)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.sideBar = QFrame(self.frame)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMaximumSize(QSize(88, 16777215))
        self.sideBar.setStyleSheet(u"#sideBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.511, y2:1, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"")
        self.sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame_2 = QFrame(self.sideBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 75))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.iconApp = QToolButton(self.frame_5)
        self.iconApp.setObjectName(u"iconApp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconApp.sizePolicy().hasHeightForWidth())
        self.iconApp.setSizePolicy(sizePolicy1)
        self.iconApp.setStyleSheet(u"#iconApp {\n"
"border: none;\n"
"padding: 9px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../icons/menu/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconApp.setIcon(icon)
        self.iconApp.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.iconApp)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"#Line {\n"
"border: none;	\n"
"background-color: rgb(255, 255, 255);\n"
"	\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame_4 = QFrame(self.sideBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QToolButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"padding: 8px;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 0, 7, 0)
        self.btn_pokedex = QToolButton(self.frame_7)
        self.btn_pokedex.setObjectName(u"btn_pokedex")
        sizePolicy1.setHeightForWidth(self.btn_pokedex.sizePolicy().hasHeightForWidth())
        self.btn_pokedex.setSizePolicy(sizePolicy1)
        self.btn_pokedex.setMaximumSize(QSize(50, 50))
        self.btn_pokedex.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../icons/menu/icon_pokedex.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pokedex.setIcon(icon1)
        self.btn_pokedex.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_pokedex)

        self.label_btn_1 = QLabel(self.frame_7)
        self.label_btn_1.setObjectName(u"label_btn_1")
        self.label_btn_1.setStyleSheet(u"")
        self.label_btn_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_btn_1)

        self.verticalSpacer_7 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(7, 0, 7, 0)
        self.btn_items = QToolButton(self.frame_8)
        self.btn_items.setObjectName(u"btn_items")
        sizePolicy1.setHeightForWidth(self.btn_items.sizePolicy().hasHeightForWidth())
        self.btn_items.setSizePolicy(sizePolicy1)
        self.btn_items.setMaximumSize(QSize(50, 50))
        self.btn_items.setStyleSheet(u"#btn_pokedex {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../icons/menu/icon_items.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_items.setIcon(icon2)
        self.btn_items.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.btn_items)

        self.label_btn_2 = QLabel(self.frame_8)
        self.label_btn_2.setObjectName(u"label_btn_2")
        self.label_btn_2.setStyleSheet(u"#label_btn_1 {\n"
"color: white;\n"
"}")
        self.label_btn_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_btn_2)

        self.verticalSpacer_6 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(7, 0, 7, 0)
        self.btn_berries = QToolButton(self.frame_9)
        self.btn_berries.setObjectName(u"btn_berries")
        sizePolicy1.setHeightForWidth(self.btn_berries.sizePolicy().hasHeightForWidth())
        self.btn_berries.setSizePolicy(sizePolicy1)
        self.btn_berries.setMaximumSize(QSize(50, 50))
        self.btn_berries.setStyleSheet(u"#btn_pokedex {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../icons/menu/icon_berries.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_berries.setIcon(icon3)
        self.btn_berries.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_berries)

        self.label_btn_3 = QLabel(self.frame_9)
        self.label_btn_3.setObjectName(u"label_btn_3")
        self.label_btn_3.setStyleSheet(u"#label_btn_1 {\n"
"color: white;\n"
"}")
        self.label_btn_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_btn_3)

        self.verticalSpacer_5 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(7, 0, 7, 0)
        self.btn_user = QToolButton(self.frame_10)
        self.btn_user.setObjectName(u"btn_user")
        sizePolicy1.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy1)
        self.btn_user.setMaximumSize(QSize(50, 50))
        self.btn_user.setStyleSheet(u"#btn_pokedex {\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 12px;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../icons/menu/theme_style/icon_history.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_user.setIcon(icon4)
        self.btn_user.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.btn_user)

        self.label_btn_4 = QLabel(self.frame_10)
        self.label_btn_4.setObjectName(u"label_btn_4")
        self.label_btn_4.setStyleSheet(u"#label_btn_1 {\n"
"color: white;\n"
"}")
        self.label_btn_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_btn_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_11 = QFrame(self.sideBar)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 45))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(7, 0, 7, 0)
        self.btn_settings = QToolButton(self.frame_11)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy1.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setMaximumSize(QSize(50, 50))
        self.btn_settings.setStyleSheet(u"#btn_settings {\n"
"border: none;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../icons/menu/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_settings)


        self.verticalLayout.addWidget(self.frame_11)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages_app = QStackedWidget(self.frame_3)
        self.pages_app.setObjectName(u"pages_app")
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.horizontalLayout_7 = QHBoxLayout(self.welcome)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_12 = QFrame(self.welcome)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(357, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 44))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.title_welcome = QLabel(self.frame_18)
        self.title_welcome.setObjectName(u"title_welcome")
        self.title_welcome.setStyleSheet(u"#title_welcome {\n"
"color: #FE9090;\n"
"font-size: 25px;\n"
"}")
        self.title_welcome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.title_welcome)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 160))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.welcome_text = QTextBrowser(self.frame_19)
        self.welcome_text.setObjectName(u"welcome_text")
        self.welcome_text.setStyleSheet(u"#welcome_text {\n"
"border: none;\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_11.addWidget(self.welcome_text)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(254, 144, 144);\n"
"border-radius: 18px;\n"
"color: rgb(254, 144, 144);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(14, 5, 14, 0)
        self.btn_repository = QPushButton(self.frame_17)
        self.btn_repository.setObjectName(u"btn_repository")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_repository.sizePolicy().hasHeightForWidth())
        self.btn_repository.setSizePolicy(sizePolicy2)
        self.btn_repository.setMinimumSize(QSize(0, 44))
        self.btn_repository.setMaximumSize(QSize(16777215, 44))
        icon6 = QIcon()
        icon6.addFile(u"../icons/github_theme.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_repository.setIcon(icon6)
        self.btn_repository.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.btn_repository)

        self.btn_email = QPushButton(self.frame_17)
        self.btn_email.setObjectName(u"btn_email")
        sizePolicy2.setHeightForWidth(self.btn_email.sizePolicy().hasHeightForWidth())
        self.btn_email.setSizePolicy(sizePolicy2)
        self.btn_email.setMinimumSize(QSize(0, 44))
        self.btn_email.setMaximumSize(QSize(16777215, 44))
        icon7 = QIcon()
        icon7.addFile(u"../icons/email_theme.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_email.setIcon(icon7)
        self.btn_email.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.btn_email)


        self.verticalLayout_9.addWidget(self.frame_17)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 113))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_start = QPushButton(self.frame_15)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy2.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy2)
        self.btn_start.setMaximumSize(QSize(16777215, 47))
        self.btn_start.setLayoutDirection(Qt.RightToLeft)
        self.btn_start.setStyleSheet(u"#btn_start {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.517045, x2:1, y2:0.5, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));;\n"
"\n"
"color: qlineargradient(spread:pad, x1:0, y1:0.517045, x2:1, y2:0.5, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));;\n"
"font-size: 18px;\n"
"border-radius: 14px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../icons/arrow-right_theme.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start.setIcon(icon8)
        self.btn_start.setIconSize(QSize(24, 24))
        self.btn_start.setAutoDefault(False)
        self.btn_start.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btn_start)


        self.verticalLayout_8.addWidget(self.frame_15)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.welcome)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy3)
        self.frame_13.setMaximumSize(QSize(335, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.img_pikachu = QLabel(self.frame_13)
        self.img_pikachu.setObjectName(u"img_pikachu")
        self.img_pikachu.setMaximumSize(QSize(300, 300))
        self.img_pikachu.setPixmap(QPixmap(u"../icons/pikachu_welcome.png"))
        self.img_pikachu.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.img_pikachu)


        self.horizontalLayout_7.addWidget(self.frame_13)

        self.pages_app.addWidget(self.welcome)
        self.pokedex = QWidget()
        self.pokedex.setObjectName(u"pokedex")
        self.verticalLayout_12 = QVBoxLayout(self.pokedex)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_20 = QFrame(self.pokedex)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 61))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy3.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy3)
        self.frame_24.setMaximumSize(QSize(441, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.search_pokemon = QLineEdit(self.frame_24)
        self.search_pokemon.setObjectName(u"search_pokemon")
        sizePolicy1.setHeightForWidth(self.search_pokemon.sizePolicy().hasHeightForWidth())
        self.search_pokemon.setSizePolicy(sizePolicy1)
        self.search_pokemon.setMaximumSize(QSize(16777215, 38))
        self.search_pokemon.setStyleSheet(u"#search_pokemon {\n"
"border: none;\n"
"background-color: rgb(254, 144, 144);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"padding-left: 15px;\n"
"color: white;\n"
"}")
        self.search_pokemon.setCursorPosition(0)

        self.horizontalLayout_13.addWidget(self.search_pokemon)

        self.btn_search = QToolButton(self.frame_24)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy1.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy1)
        self.btn_search.setMaximumSize(QSize(41, 38))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"border: none;\n"
"background-color: rgb(202, 87, 83);\n"
"border-top-right-radius: 9px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../icons/icon button pokemon/pikachu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search.setIcon(icon9)
        self.btn_search.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.btn_search)


        self.horizontalLayout_12.addWidget(self.frame_24)

        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(215, 16777215))
        self.frame_23.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.523, y2:1, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"border-radius: 12px;\n"
"color: white;\n"
"padding: 12px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_23)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(16777215, 38))
        icon10 = QIcon()
        icon10.addFile(u"../icons/buttons options/filter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon10)

        self.horizontalLayout_14.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_23)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMaximumSize(QSize(16777215, 38))
        icon11 = QIcon()
        icon11.addFile(u"../icons/buttons options/order.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon11)

        self.horizontalLayout_14.addWidget(self.pushButton_2)


        self.horizontalLayout_12.addWidget(self.frame_23)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.pokedex)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pages_search = QStackedWidget(self.frame_21)
        self.pages_search.setObjectName(u"pages_search")
        sizePolicy1.setHeightForWidth(self.pages_search.sizePolicy().hasHeightForWidth())
        self.pages_search.setSizePolicy(sizePolicy1)
        self.pokemon = QWidget()
        self.pokemon.setObjectName(u"pokemon")
        sizePolicy1.setHeightForWidth(self.pokemon.sizePolicy().hasHeightForWidth())
        self.pokemon.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.pokemon)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pokemon)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_pokemon = QWidget()
        self.scrollArea_pokemon.setObjectName(u"scrollArea_pokemon")
        self.scrollArea_pokemon.setGeometry(QRect(0, 0, 782, 393))
        self.gridLayout_2 = QGridLayout(self.scrollArea_pokemon)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea.setWidget(self.scrollArea_pokemon)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pages_search.addWidget(self.pokemon)
        self.items = QWidget()
        self.items.setObjectName(u"items")
        self.verticalLayout_13 = QVBoxLayout(self.items)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pages_search.addWidget(self.items)
        self.berries = QWidget()
        self.berries.setObjectName(u"berries")
        self.verticalLayout_14 = QVBoxLayout(self.berries)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pages_search.addWidget(self.berries)
        self.error_search = QWidget()
        self.error_search.setObjectName(u"error_search")
        self.verticalLayout_15 = QVBoxLayout(self.error_search)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_25 = QFrame(self.error_search)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setEnabled(True)
        self.frame_25.setMinimumSize(QSize(0, 0))
        self.frame_25.setMaximumSize(QSize(16777215, 113))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.icon_wifi_off = QLabel(self.frame_25)
        self.icon_wifi_off.setObjectName(u"icon_wifi_off")
        self.icon_wifi_off.setPixmap(QPixmap(u"../icons/wifi_off.png"))
        self.icon_wifi_off.setScaledContents(False)
        self.icon_wifi_off.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.icon_wifi_off)


        self.verticalLayout_15.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.error_search)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label = QLabel(self.frame_27)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label)


        self.verticalLayout_16.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy3.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy3)
        self.frame_28.setMaximumSize(QSize(110, 16777215))
        self.frame_28.setLayoutDirection(Qt.LeftToRight)
        self.frame_28.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.505682, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"color: white;\n"
"border-radius: 9px;\n"
"font-size: 15px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_28)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.btn_back = QPushButton(self.frame_28)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy1.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy1)
        self.btn_back.setMaximumSize(QSize(190, 35))
        icon12 = QIcon()
        icon12.addFile(u"../icons/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_back.setIcon(icon12)

        self.verticalLayout_17.addWidget(self.btn_back)

        self.btn_reload = QPushButton(self.frame_28)
        self.btn_reload.setObjectName(u"btn_reload")
        sizePolicy1.setHeightForWidth(self.btn_reload.sizePolicy().hasHeightForWidth())
        self.btn_reload.setSizePolicy(sizePolicy1)
        self.btn_reload.setMaximumSize(QSize(190, 35))
        icon13 = QIcon()
        icon13.addFile(u"../icons/arrow-clockwise.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reload.setIcon(icon13)

        self.verticalLayout_17.addWidget(self.btn_reload)


        self.verticalLayout_16.addWidget(self.frame_28, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_26)

        self.pages_search.addWidget(self.error_search)

        self.horizontalLayout_16.addWidget(self.pages_search)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.pokedex)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_more = QPushButton(self.frame_22)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy2.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy2)
        self.btn_more.setMaximumSize(QSize(225, 16777215))
        self.btn_more.setStyleSheet(u"#btn_more {\n"
"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.505682, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"\n"
"color: white;\n"
"border-radius: 12px;\n"
"font-size: 15px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"../icons/buttons options/plus pokemon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_more.setIcon(icon14)
        self.btn_more.setIconSize(QSize(25, 25))

        self.horizontalLayout_15.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.pages_app.addWidget(self.pokedex)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_18 = QVBoxLayout(self.history)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_29 = QFrame(self.history)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 80))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.btn_history = QToolButton(self.frame_31)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy1.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy1)
        self.btn_history.setMaximumSize(QSize(16777215, 40))
        self.btn_history.setStyleSheet(u"#btn_history {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.505682, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"border: none;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"../icons/buttons options/icons_fill/history_fill.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_history.setIcon(icon15)
        self.btn_history.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.btn_history)

        self.btn_favorites = QToolButton(self.frame_31)
        self.btn_favorites.setObjectName(u"btn_favorites")
        sizePolicy1.setHeightForWidth(self.btn_favorites.sizePolicy().hasHeightForWidth())
        self.btn_favorites.setSizePolicy(sizePolicy1)
        self.btn_favorites.setMaximumSize(QSize(16777215, 40))
        self.btn_favorites.setStyleSheet(u"#btn_favorites {\n"
"border: 2px solid rgb(242, 102, 116);\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"../icons/buttons options/favorite.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_favorites.setIcon(icon16)
        self.btn_favorites.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.btn_favorites)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.line_2 = QFrame(self.frame_31)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"#line_2 {\n"
"border: none;\n"
"background-color: rgb(242, 102, 116);\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_2)


        self.horizontalLayout_19.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(222, 16777215))
        self.frame_32.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.523, y2:1, stop:0 rgba(254, 144, 144, 255), stop:1 rgba(255, 140, 78, 255));\n"
"border-radius: 12px;\n"
"color: white;\n"
"padding: 12px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_3 = QPushButton(self.frame_32)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMaximumSize(QSize(16777215, 38))
        self.pushButton_3.setIcon(icon10)

        self.horizontalLayout_21.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_32)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMaximumSize(QSize(16777215, 38))
        self.pushButton_4.setIcon(icon11)

        self.horizontalLayout_21.addWidget(self.pushButton_4)


        self.horizontalLayout_19.addWidget(self.frame_32)


        self.verticalLayout_18.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.history)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pages_history = QStackedWidget(self.frame_30)
        self.pages_history.setObjectName(u"pages_history")
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.page_history.setStyleSheet(u"#page_history {\n"
"background-color: rgb(238, 238, 238);\n"
"border-radius: 10px;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.page_history)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pages_history.addWidget(self.page_history)
        self.page_favorites = QWidget()
        self.page_favorites.setObjectName(u"page_favorites")
        self.page_favorites.setStyleSheet(u"#page_favorites {\n"
"	background-color: rgb(238, 238, 238);\n"
"border-radius: 10px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.page_favorites)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pages_history.addWidget(self.page_favorites)

        self.horizontalLayout_22.addWidget(self.pages_history)


        self.verticalLayout_18.addWidget(self.frame_30)

        self.pages_app.addWidget(self.history)

        self.horizontalLayout_6.addWidget(self.pages_app)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_app.setCurrentIndex(0)
        self.btn_start.setDefault(False)
        self.pages_search.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.iconApp.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_pokedex.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_btn_1.setText(QCoreApplication.translate("MainWindow", u"Pok\u00e9dex", None))
        self.btn_items.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u00cdtems", None))
        self.btn_berries.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_btn_3.setText(QCoreApplication.translate("MainWindow", u"Bayas", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_btn_4.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.title_welcome.setText(QCoreApplication.translate("MainWindow", u"  \u00a1Bienvenido entrenador!", None))
        self.welcome_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Esta es <span style=\" font-weight:700; color:#fe9090;\">la Pydex</span>, una aplicaci\u00f3n que te permitir\u00e1 obtener informaci\u00f3n en tiempo real sobre el mundo Pok\u00e9mon. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actualmente est\u00e1s utilizando<span style=\" font-weight:700; color:#fe9090;\"> la"
                        " versi\u00f3n Beta-2.0</span><span style=\" color:#000000;\">. S</span>i tienes alguna sugerencia sobre una nueva funci\u00f3n, errores, etc. Te dejar\u00e9 aqu\u00ed un bot\u00f3n al repositorio de GitHub o puedes escribirme con confianza a mi correo.</p></body></html>", None))
        self.btn_repository.setText(QCoreApplication.translate("MainWindow", u"Repositorio del Proyecto", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u"devBluePhoenix77@gmail.com", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Comenzar     ", None))
        self.img_pikachu.setText("")
        self.search_pokemon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Busca el Pok\u00e9mon que m\u00e1s te guste...", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.icon_wifi_off.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ca5753;\">Error:</span><span style=\" font-size:16pt;\"> no hay conexi\u00f3n a internet.</span></p></body></html>", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btn_reload.setText(QCoreApplication.translate("MainWindow", u"Reintentar", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"    Cargar m\u00e1s Pok\u00e9mon", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_favorites.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

