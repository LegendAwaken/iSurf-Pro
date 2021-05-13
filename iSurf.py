from random import randint
from threading import Thread
import pygetwindow
from PIL import Image  # pip install pillow
from PIL.ImageFilter import *
from PyQt5.QtCore import *  # pip install PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *  # search for it
from PyQt5.QtWidgets import *
from pyautogui import *
from win32api import *

# constants
WIDTH_ = GetSystemMetrics(0)
HEIGHT_ = GetSystemMetrics(1)
USER = GetUserName()
PATH_ = ""


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.blur = QGraphicsBlurEffect()
        self.setGeometry(WIDTH_ / 12, HEIGHT_ / 15, WIDTH_ / 1.14, HEIGHT_ / 1.14)
        self.setMinimumSize(WIDTH_ / 1.2, HEIGHT_ / 1.2)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)
        self.setupUi(self)
        self.functionalities()
        self.showMaximized()

        get_image = screenshot()
        r = str(randint(10, 100000))
        with open("assets/resources/holder.tru", 'w') as hold:
            hold.write(r)
        get_image.save(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
        frame_one_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
        skinned_ = Image.eval(frame_one_image, lambda x: x / 2)
        frame_one_blurred_image = skinned_.filter(GaussianBlur(radius=15))
        frame_one_blurred_image.save(f"C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg")
        frame_two_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
        skinned_image = Image.eval(frame_two_image, lambda x: x / 3)
        frame_two_blurred_image = skinned_image.filter(GaussianBlur(radius=30))
        frame_two_blurred_image.save(f"C:/Users/{USER}/AppData/Local/Temp/vis_reb2{r}.jpeg")
        frame_three_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
        skinned_image_frame_three = Image.eval(frame_three_image, lambda x: x / 4)
        frame_three_blurred_image = skinned_image_frame_three.filter(GaussianBlur(radius=70))
        frame_three_blurred_image.save(f'C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg')

        if self.isMaximized():
            self.setWindowOpacity(1.0)

            # FRAMES UI

            # FRAME 1
            try:
                self.graphics.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                                      background-repeat: repeat;
                                      background-position: left;
                                      border: 0;""")

                # FRAME 2
                self.settings_3.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: left center;
                                      border: 0;
                                  """)

                # FRAME 3
                self.top_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                                      background-repeat: repeat;
                                      background-position: top;
                                      border: 0;
                                  """)
                self.profile_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: repeat;
                                      background-position: top;
                                      border: 0;
                                  """)
                self.appearance_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
                self.downloads_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
                self.startup_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
                self.new_tab_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
                self.history_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
                self.feedback_frame.setStyleSheet(f"""
                                      background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      border: 0;
                                  """)
            except FileNotFoundError:
                pass

    def setupUi(self, iSurf):
        if not iSurf.objectName():
            iSurf.setObjectName(u"iSurf.exe")
        iSurf.resize(1171, 647)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(iSurf.sizePolicy().hasHeightForWidth())
        iSurf.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        iSurf.setFont(font)
        iSurf.setStyleSheet(u"")
        self.gridLayout = QGridLayout(iSurf)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphics = QFrame(iSurf)
        self.graphics.setObjectName(u"graphics")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphics.sizePolicy().hasHeightForWidth())
        self.graphics.setSizePolicy(sizePolicy1)
        self.graphics.setMinimumSize(QSize(300, 0))
        self.graphics.setStyleSheet(u"background: black;")
        self.graphics.setFrameShape(QFrame.StyledPanel)
        self.graphics.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.graphics)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.new_tab = QPushButton(self.graphics)
        self.new_tab.setObjectName(u"new_tab")
        self.new_tab.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.new_tab.setFont(font1)
        self.new_tab.setStyleSheet(u"QPushButton{\n"
                                   "color: white;\n"
                                   "background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "  color: white;\n"
                                   "  background-color : rgba(255, 255  ,255 ,100);\n"
                                   "  border-radius: 2px;\n"
                                   "  border-style: inset;\n"
                                   "  border-width: 1px;\n"
                                   "  border-color: white;\n"
                                   "  border-color: rgba(255, 255  ,255 ,150);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed{\n"
                                   "  background-color: rgba(255, 255, 255, 30)\n"
                                   "}\n"
                                   "")
        icon = QIcon()
        icon.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/fluent-tab.png", QSize(),
                     QIcon.Normal, QIcon.Off)
        self.new_tab.setIcon(icon)
        self.new_tab.setIconSize(QSize(34, 48))

        self.verticalLayout_3.addWidget(self.new_tab)

        self.private_tab = QPushButton(self.graphics)
        self.private_tab.setObjectName(u"private_tab")
        self.private_tab.setMinimumSize(QSize(0, 45))
        self.private_tab.setFont(font1)
        self.private_tab.setStyleSheet(u"QPushButton{\n"
                                       "color: white;\n"
                                       "background: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover{\n"
                                       "  color: white;\n"
                                       "  background-color : rgba(255, 255  ,255 ,100);\n"
                                       "  border-radius: 2px;\n"
                                       "  border-style: inset;\n"
                                       "  border-width: 1px;\n"
                                       "  border-color: white;\n"
                                       "  border-color: rgba(255, 255  ,255 ,150);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::pressed{\n"
                                       "  background-color: rgba(255, 255, 255, 30)\n"
                                       "}\n"
                                       "")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/private-tab.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.private_tab.setIcon(icon1)
        self.private_tab.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.private_tab)

        self.history = QPushButton(self.graphics)
        self.history.setObjectName(u"history")
        self.history.setMinimumSize(QSize(0, 45))
        self.history.setFont(font1)
        self.history.setStyleSheet(u"QPushButton{\n"
                                   "color: white;\n"
                                   "background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "  color: white;\n"
                                   "  background-color : rgba(255, 255  ,255 ,100);\n"
                                   "  border-radius: 2px;\n"
                                   "  border-style: inset;\n"
                                   "  border-width: 1px;\n"
                                   "  border-color: white;\n"
                                   "  border-color: rgba(255, 255  ,255 ,150);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed{\n"
                                   "  background-color: rgba(255, 255, 255, 30)\n"
                                   "}\n"
                                   "")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/history.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.history.setIcon(icon2)
        self.history.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.history)

        self.profile = QPushButton(self.graphics)
        self.profile.setObjectName(u"profile")
        self.profile.setMinimumSize(QSize(0, 45))
        self.profile.setFont(font1)
        self.profile.setStyleSheet(u"QPushButton{\n"
                                   "color: white;\n"
                                   "background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "  color: white;\n"
                                   "  background-color : rgba(255, 255  ,255 ,100);\n"
                                   "  border-radius: 2px;\n"
                                   "  border-style: inset;\n"
                                   "  border-width: 1px;\n"
                                   "  border-color: white;\n"
                                   "  border-color: rgba(255, 255  ,255 ,150);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed{\n"
                                   "  background-color: rgba(255, 255, 255, 30)\n"
                                   "}\n"
                                   "")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/profile.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon3)
        self.profile.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.profile)

        self.extension = QPushButton(self.graphics)
        self.extension.setObjectName(u"extension")
        self.extension.setMinimumSize(QSize(0, 45))
        self.extension.setFont(font1)
        self.extension.setStyleSheet(u"QPushButton{\n"
                                     "color: white;\n"
                                     "background: transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::hover{\n"
                                     "  color: white;\n"
                                     "  background-color : rgba(255, 255  ,255 ,100);\n"
                                     "  border-radius: 2px;\n"
                                     "  border-style: inset;\n"
                                     "  border-width: 1px;\n"
                                     "  border-color: white;\n"
                                     "  border-color: rgba(255, 255  ,255 ,150);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::pressed{\n"
                                     "  background-color: rgba(255, 255, 255, 30)\n"
                                     "}\n"
                                     "")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/extension.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.extension.setIcon(icon4)
        self.extension.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.extension)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.settings = QPushButton(self.graphics)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 45))
        self.settings.setFont(font1)
        self.settings.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover{\n"
                                    " color: white;\n"
                                    " background-color : rgba(255, 255  ,255 ,100);\n"
                                    " border-radius: 2px;\n"
                                    " border-style: inset;\n"
                                    " border-width: 1px;\n"
                                    " border-color: white;\n"
                                    " border-color: rgba(255, 255  ,255 ,150);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed{\n"
                                    " background-color: rgba(255, 255, 255, 30)\n"
                                    "}\n"
                                    "")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/settings.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon5)
        self.settings.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.settings)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addWidget(self.graphics)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.frame_2 = QFrame(iSurf)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"background-color: white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: black")
        self.stackedWidget.setLineWidth(0)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_27 = QVBoxLayout(self.profile_page)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, -1, -1)
        self.profile_frame = QFrame(self.profile_page)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setMinimumSize(QSize(691, 521))
        self.profile_frame.setFrameShape(QFrame.NoFrame)
        self.profile_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_28 = QVBoxLayout(self.profile_frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 10, 0, 0)
        self.pushButton_3 = QPushButton(self.profile_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"color: white; background: transparent;")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(45, 45))

        self.verticalLayout_28.addWidget(self.pushButton_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setContentsMargins(50, 50, 50, 50)
        self.label_7 = QLabel(self.profile_frame)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: white; background: transparent;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.profile_name_edit = QLineEdit(self.profile_frame)
        self.profile_name_edit.setObjectName(u"profile_name_edit")
        sizePolicy.setHeightForWidth(self.profile_name_edit.sizePolicy().hasHeightForWidth())
        self.profile_name_edit.setSizePolicy(sizePolicy)
        self.profile_name_edit.setMinimumSize(QSize(200, 30))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.profile_name_edit.setFont(font4)
        self.profile_name_edit.setStyleSheet(u"color: white;\n"
                                             "background: transparent;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.profile_name_edit)

        self.label_10 = QLabel(self.profile_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: white; \n"
                                    "background: transparent;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.profile_username_edit = QLineEdit(self.profile_frame)
        self.profile_username_edit.setObjectName(u"profile_username_edit")
        sizePolicy.setHeightForWidth(self.profile_username_edit.sizePolicy().hasHeightForWidth())
        self.profile_username_edit.setSizePolicy(sizePolicy)
        self.profile_username_edit.setMinimumSize(QSize(200, 30))
        self.profile_username_edit.setFont(font4)
        self.profile_username_edit.setStyleSheet(u"color: white; \n"
                                                 "background: transparent;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.profile_username_edit)

        self.label_8 = QLabel(self.profile_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: white;\n"
                                   "background: transparent;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.profile_password_edit = QLineEdit(self.profile_frame)
        self.profile_password_edit.setObjectName(u"profile_password_edit")
        sizePolicy.setHeightForWidth(self.profile_password_edit.sizePolicy().hasHeightForWidth())
        self.profile_password_edit.setSizePolicy(sizePolicy)
        self.profile_password_edit.setMinimumSize(QSize(200, 30))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setBold(True)
        font5.setWeight(75)
        self.profile_password_edit.setFont(font5)
        self.profile_password_edit.setStyleSheet(u"color: white; background: transparent;")
        self.profile_password_edit.setInputMask(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.profile_password_edit)

        self.profile_save_button = QPushButton(self.profile_frame)
        self.profile_save_button.setObjectName(u"profile_save_button")
        self.profile_save_button.setMinimumSize(QSize(150, 0))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.profile_save_button.setFont(font6)
        self.profile_save_button.setStyleSheet(u"QPushButton{\n"
                                               "color: white;\n"
                                               "background: transparent;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::hover{\n"
                                               "  color: white;\n"
                                               "  background-color : rgba(255, 255  ,255 ,100);\n"
                                               "  border-radius: 12px;\n"
                                               "  border-style: inset;\n"
                                               "  border-width: 1px;\n"
                                               "  border-color: white;\n"
                                               "  border-color: rgba(255, 255  ,255 ,150);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::pressed{\n"
                                               "  background-color: rgba(255, 255, 255, 30)\n"
                                               "}\n"
                                               "")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.profile_save_button)

        self.verticalLayout_28.addLayout(self.formLayout)

        self.verticalLayout_26.addWidget(self.profile_frame)

        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.stackedWidget.addWidget(self.profile_page)
        self.history_page = QWidget()
        self.history_page.setObjectName(u"history_page")
        self.verticalLayout_21 = QVBoxLayout(self.history_page)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.history_frame = QFrame(self.history_page)
        self.history_frame.setObjectName(u"history_frame")
        self.history_frame.setFrameShape(QFrame.StyledPanel)
        self.history_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.history_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.history_label = QPushButton(self.history_frame)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.history_label.setFont(font7)
        self.history_label.setStyleSheet(u"color: white; background: transparent;")
        self.history_label.setIcon(icon2)
        self.history_label.setIconSize(QSize(35, 35))

        self.verticalLayout_22.addWidget(self.history_label)

        self.history_grid = QGridLayout()
        self.history_grid.setObjectName(u"history_grid")
        self.history_indicator = QLabel(self.history_frame)
        self.history_indicator.setObjectName(u"history_indicator")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(11)
        self.history_indicator.setFont(font8)
        self.history_indicator.setStyleSheet(u"color: white; background: transparent;")
        self.history_indicator.setAlignment(Qt.AlignCenter)

        self.history_grid.addWidget(self.history_indicator, 0, 0, 1, 1)

        self.verticalLayout_22.addLayout(self.history_grid)

        self.verticalLayout_23.addLayout(self.verticalLayout_22)

        self.verticalLayout_20.addWidget(self.history_frame)

        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.stackedWidget.addWidget(self.history_page)
        self.new_tab_page = QWidget()
        self.new_tab_page.setObjectName(u"new_tab_page")
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(10)
        self.new_tab_page.setFont(font9)
        self.new_tab_page.setStyleSheet(u"QTabBar::tab {\n"
                                        " color: white;\n"
                                        " font: Arial 9px;\n"
                                        " background: rgba(255,  255, 255, 50);\n"
                                        " border: 0px;\n"
                                        " border-top-left-radius: 4px;\n"
                                        " border-top-right-radius: 4px;\n"
                                        " min-width: 30ex;\n"
                                        " padding: 5px;\n"
                                        " spacing: 10px;\n"
                                        "}")
        self.verticalLayout_4 = QVBoxLayout(self.new_tab_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.new_tab_frame = QFrame(self.new_tab_page)
        self.new_tab_frame.setObjectName(u"new_tab_frame")
        self.new_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.new_tab_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.new_tab_frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.tabWidget = QTabWidget(self.new_tab_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background: rgba(0, 0, 0, 2);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_30 = QVBoxLayout(self.tab)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacer_23 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_29.addItem(self.verticalSpacer_23)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamily(u"Segoe Print")
        font10.setPointSize(36)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_5.setFont(font10)
        self.label_5.setStyleSheet(u"color: white; background: transparent;")

        self.verticalLayout_29.addWidget(self.label_5, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        font11 = QFont()
        font11.setFamily(u"Arial")
        font11.setPointSize(7)
        font11.setItalic(True)
        self.label_6.setFont(font11)
        self.label_6.setStyleSheet(u"color: white; background: transparent;")

        self.verticalLayout_29.addWidget(self.label_6, 0, Qt.AlignLeft | Qt.AlignBottom)

        self.verticalLayout_30.addLayout(self.verticalLayout_29)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_24.addWidget(self.tabWidget)

        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalLayout_4.addWidget(self.new_tab_frame)

        self.stackedWidget.addWidget(self.new_tab_page)
        self.goto_settings = QWidget()
        self.goto_settings.setObjectName(u"goto_settings")
        self.horizontalLayout_4 = QHBoxLayout(self.goto_settings)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings_3 = QFrame(self.goto_settings)
        self.settings_3.setObjectName(u"settings_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settings_3.sizePolicy().hasHeightForWidth())
        self.settings_3.setSizePolicy(sizePolicy3)
        self.settings_3.setMinimumSize(QSize(240, 0))
        self.settings_3.setStyleSheet(u"")
        self.settings_3.setFrameShape(QFrame.NoFrame)
        self.settings_3.setFrameShadow(QFrame.Plain)
        self.settings_3.setLineWidth(1)
        self.settings_3.setMidLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.settings_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_20 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_20)

        self.settings_button = QPushButton(self.settings_3)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setFamily(u"Arial")
        font12.setPointSize(26)
        font12.setBold(True)
        font12.setWeight(75)
        self.settings_button.setFont(font12)
        self.settings_button.setStyleSheet(u"color: white; background: transparent;")
        self.settings_button.setIcon(icon5)
        self.settings_button.setIconSize(QSize(45, 45))
        self.settings_button.setCheckable(False)

        self.verticalLayout_5.addWidget(self.settings_button, 0, Qt.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.appearance = QPushButton(self.settings_3)
        self.appearance.setObjectName(u"appearance")
        self.appearance.setMinimumSize(QSize(0, 45))
        self.appearance.setFont(font8)
        self.appearance.setStyleSheet(u"QPushButton{\n"
                                      "color: white;\n"
                                      "background: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      " color: white;\n"
                                      " background-color : rgba(255, 255  ,255 ,100);\n"
                                      " border-radius: 5px;\n"
                                      " border-style: inset;\n"
                                      " border-width: 1px;\n"
                                      " border-color: white;\n"
                                      " border-color: rgba(255, 255  ,255 ,150);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      " background-color: rgba(255, 255, 255, 30)\n"
                                      "}\n"
                                      "")
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/appearance.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.appearance.setIcon(icon6)
        self.appearance.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.appearance)

        self.passwords = QPushButton(self.settings_3)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setMinimumSize(QSize(0, 45))
        self.passwords.setFont(font8)
        self.passwords.setStyleSheet(u"QPushButton{\n"
                                     "color: white;\n"
                                     "background: transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::hover{\n"
                                     "  color: white;\n"
                                     "  background-color : rgba(255, 255  ,255 ,100);\n"
                                     "  border-radius: 5px;\n"
                                     "  border-style: inset;\n"
                                     "  border-width: 1px;\n"
                                     "  border-color: white;\n"
                                     "  border-color: rgba(255, 255  ,255 ,150);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::pressed{\n"
                                     "  background-color: rgba(255, 255, 255, 30)\n"
                                     "}\n"
                                     "")
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/passwords.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.passwords.setIcon(icon7)
        self.passwords.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.passwords)

        self.startup = QPushButton(self.settings_3)
        self.startup.setObjectName(u"startup")
        self.startup.setMinimumSize(QSize(0, 45))
        self.startup.setFont(font8)
        self.startup.setStyleSheet(u"QPushButton{\n"
                                   "color: white;\n"
                                   "background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "  color: white;\n"
                                   "  background-color : rgba(255, 255  ,255 ,100);\n"
                                   "  border-radius: 5px;\n"
                                   "  border-style: inset;\n"
                                   "  border-width: 1px;\n"
                                   "  border-color: white;\n"
                                   "  border-color: rgba(255, 255  ,255 ,150);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed{\n"
                                   "  background-color: rgba(255, 255, 255, 30)\n"
                                   "}\n"
                                   "")
        icon8 = QIcon()
        icon8.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/startup.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.startup.setIcon(icon8)
        self.startup.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.startup)

        self.downloads = QPushButton(self.settings_3)
        self.downloads.setObjectName(u"downloads")
        self.downloads.setMinimumSize(QSize(0, 45))
        self.downloads.setFont(font8)
        self.downloads.setStyleSheet(u"QPushButton{\n"
                                     "color: white;\n"
                                     "background: transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::hover{\n"
                                     "  color: white;\n"
                                     "  background-color : rgba(255, 255  ,255 ,100);\n"
                                     "  border-radius: 5px;\n"
                                     "  border-style: inset;\n"
                                     "  border-width: 1px;\n"
                                     "  border-color: white;\n"
                                     "  border-color: rgba(255, 255  ,255 ,150);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::pressed{\n"
                                     "  background-color: rgba(255, 255, 255, 30)\n"
                                     "}\n"
                                     "")
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/downloads.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.downloads.setIcon(icon9)
        self.downloads.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.downloads)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.feedback = QPushButton(self.settings_3)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setMinimumSize(QSize(0, 45))
        self.feedback.setFont(font8)
        self.feedback.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover{\n"
                                    " color: white;\n"
                                    " background-color : rgba(255, 255  ,255 ,100);\n"
                                    " border-radius: 5px;\n"
                                    " border-style: inset;\n"
                                    " border-width: 1px;\n"
                                    " border-color: white;\n"
                                    " border-color: rgba(255, 255  ,255 ,150);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed{\n"
                                    " background-color: rgba(255, 255, 255, 30)\n"
                                    "}\n"
                                    "")
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/feedback.png", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.feedback.setIcon(icon10)
        self.feedback.setIconSize(QSize(35, 35))

        self.verticalLayout_5.addWidget(self.feedback)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout.addWidget(self.settings_3, 0, Qt.AlignLeft)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.settings_pages_frame = QFrame(self.goto_settings)
        self.settings_pages_frame.setObjectName(u"settings_pages_frame")
        self.settings_pages_frame.setFrameShape(QFrame.NoFrame)
        self.settings_pages_frame.setFrameShadow(QFrame.Plain)
        self.settings_pages_frame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.settings_pages_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settings_pages = QStackedWidget(self.settings_pages_frame)
        self.settings_pages.setObjectName(u"settings_pages")
        self.settings_pages.setStyleSheet(u"background-color:  black;\n"
                                          "color: black;")
        self.settings_pages.setFrameShape(QFrame.StyledPanel)
        self.settings_pages.setFrameShadow(QFrame.Plain)
        self.settings_pages.setLineWidth(0)
        self.startup_page = QWidget()
        self.startup_page.setObjectName(u"startup_page")
        self.startup_page.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.startup_page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.startup_frame = QFrame(self.startup_page)
        self.startup_frame.setObjectName(u"startup_frame")
        self.startup_frame.setFrameShape(QFrame.StyledPanel)
        self.startup_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.startup_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.verticalSpacer_10 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_10)

        self.start_up_label = QPushButton(self.startup_frame)
        self.start_up_label.setObjectName(u"start_up_label")
        self.start_up_label.setMinimumSize(QSize(0, 45))
        font13 = QFont()
        font13.setFamily(u"Arial")
        font13.setPointSize(24)
        font13.setBold(True)
        font13.setWeight(75)
        self.start_up_label.setFont(font13)
        self.start_up_label.setStyleSheet(u"color: white; background: transparent;")
        self.start_up_label.setIcon(icon8)
        self.start_up_label.setIconSize(QSize(35, 35))

        self.verticalLayout_12.addWidget(self.start_up_label, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.verticalSpacer_12 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.radioButton_2 = QRadioButton(self.startup_frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy4)
        self.radioButton_2.setMinimumSize(QSize(0, 30))
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setStyleSheet(u"color: white;\n"
                                         "background: transparent;")

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton_4 = QRadioButton(self.startup_frame)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(0, 30))
        self.radioButton_4.setFont(font1)
        self.radioButton_4.setStyleSheet(u"color: white;\n"
                                         "background: transparent;")

        self.verticalLayout_12.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.startup_frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(0, 30))
        self.radioButton_3.setFont(font1)
        self.radioButton_3.setStyleSheet(u"color: white;\n"
                                         "background: transparent;")

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.verticalSpacer_3 = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.specific_page_url = QLineEdit(self.startup_frame)
        self.specific_page_url.setObjectName(u"specific_page_url")
        self.specific_page_url.setEnabled(False)
        self.specific_page_url.setFont(font1)
        self.specific_page_url.setStyleSheet(u"color: white; border-radius: 10px white;;\n"
                                             "background: transparent;")

        self.gridLayout_3.addWidget(self.specific_page_url, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalLayout_12.addLayout(self.gridLayout_3)

        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.horizontalLayout_6.addWidget(self.startup_frame)

        self.settings_pages.addWidget(self.startup_page)
        self.downloads_page = QWidget()
        self.downloads_page.setObjectName(u"downloads_page")
        self.verticalLayout_19 = QVBoxLayout(self.downloads_page)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.downloads_frame = QFrame(self.downloads_page)
        self.downloads_frame.setObjectName(u"downloads_frame")
        self.downloads_frame.setFrameShape(QFrame.StyledPanel)
        self.downloads_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.downloads_frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(20, -1, -1, -1)
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_16, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_21, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.downloads_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 42))
        font14 = QFont()
        font14.setFamily(u"Arial")
        font14.setPointSize(22)
        font14.setBold(True)
        font14.setWeight(75)
        self.pushButton.setFont(font14)
        self.pushButton.setStyleSheet(u"color: white; background: transparent;")
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.pushButton, 1, 2, 1, 1, Qt.AlignHCenter | Qt.AlignTop)

        self.label = QLabel(self.downloads_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;\n"
                                 "background: transparent;")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label, 3, 0, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_13 = QSpacerItem(25, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.downloads_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
        self.lineEdit.setMinimumSize(QSize(300, 10))
        font15 = QFont()
        font15.setFamily(u"Arial")
        font15.setPointSize(12)
        self.lineEdit.setFont(font15)
        self.lineEdit.setStyleSheet(u"background: transparent;\n"
                                    "color: white;")

        self.gridLayout_5.addWidget(self.lineEdit, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 3, 1, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalLayout_18.addWidget(self.downloads_frame)

        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.settings_pages.addWidget(self.downloads_page)
        self.feeedback_page = QWidget()
        self.feeedback_page.setObjectName(u"feeedback_page")
        self.gridLayout_4 = QGridLayout(self.feeedback_page)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.feedback_frame = QFrame(self.feeedback_page)
        self.feedback_frame.setObjectName(u"feedback_frame")
        self.feedback_frame.setStyleSheet(u"background-color: rgba(0,0,0,0.56)")
        self.feedback_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.feedback_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.label_3 = QLabel(self.feedback_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white; background: transparent;")
        self.label_3.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignTop)

        self.feedback_graphics_frame = QFrame(self.feedback_frame)
        self.feedback_graphics_frame.setObjectName(u"feedback_graphics_frame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.feedback_graphics_frame.sizePolicy().hasHeightForWidth())
        self.feedback_graphics_frame.setSizePolicy(sizePolicy7)
        self.feedback_graphics_frame.setMinimumSize(QSize(0, 200))
        self.feedback_graphics_frame.setStyleSheet(u"background: transparent;")
        self.feedback_graphics_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_graphics_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.feedback_graphics_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_2 = QLabel(self.feedback_graphics_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        font16 = QFont()
        font16.setFamily(u"Arial")
        font16.setPointSize(20)
        font16.setBold(True)
        font16.setWeight(75)
        self.label_2.setFont(font16)
        self.label_2.setStyleSheet(u"color: white; background: transparent;")

        self.verticalLayout_15.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.verticalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.verticalSpacer_19)

        self.label_4 = QLabel(self.feedback_graphics_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: white; background: transparent;")
        self.label_4.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_4)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_11)

        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.verticalLayout_11.addWidget(self.feedback_graphics_frame, 0, Qt.AlignTop)

        self.write_to_us_box = QPlainTextEdit(self.feedback_frame)
        self.write_to_us_box.setObjectName(u"write_to_us_box")
        self.write_to_us_box.setFont(font)
        self.write_to_us_box.setStyleSheet(u"color: white; background: transparent; border: 0;")

        self.verticalLayout_11.addWidget(self.write_to_us_box)

        self.close_writ_to_us = QPushButton(self.feedback_frame)
        self.close_writ_to_us.setObjectName(u"close_writ_to_us")
        sizePolicy.setHeightForWidth(self.close_writ_to_us.sizePolicy().hasHeightForWidth())
        self.close_writ_to_us.setSizePolicy(sizePolicy)
        self.close_writ_to_us.setMinimumSize(QSize(0, 0))
        self.close_writ_to_us.setStyleSheet(u"QPushButton{\n"
                                            "color: white;\n"
                                            "background: transparent;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::hover{\n"
                                            " color: white;\n"
                                            " background-color : rgba(255, 255  ,255 ,100);\n"
                                            " border-radius: 5px;\n"
                                            " border-style: inset;\n"
                                            " border-width: 1px;\n"
                                            " border-color: white;\n"
                                            " border-color: rgba(255, 255  ,255 ,150);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::pressed{\n"
                                            " background-color: rgba(255, 255, 255, 30)\n"
                                            "}\n"
                                            "")
        icon11 = QIcon()
        icon11.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/close.png", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.close_writ_to_us.setIcon(icon11)
        self.close_writ_to_us.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.close_writ_to_us, 0, Qt.AlignRight)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_9)

        self.write_to_us = QPushButton(self.feedback_frame)
        self.write_to_us.setObjectName(u"write_to_us")
        self.write_to_us.setMinimumSize(QSize(0, 0))
        self.write_to_us.setFont(font)
        self.write_to_us.setStyleSheet(u"QPushButton{\n"
                                       "color: white;\n"
                                       "background: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover{\n"
                                       "  color: white;\n"
                                       "  background-color : rgba(255, 255  ,255 ,100);\n"
                                       "  border-radius: 5px;\n"
                                       "  border-style: inset;\n"
                                       "  border-width: 1px;\n"
                                       "  border-color: white;\n"
                                       "  border-color: rgba(255, 255  ,255 ,150);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::pressed{\n"
                                       "  background-color: rgba(255, 255, 255, 30)\n"
                                       "}\n"
                                       "")
        icon12 = QIcon()
        icon12.addFile(
            u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/icons8-contact-us-48.png",
            QSize(), QIcon.Normal, QIcon.Off)
        self.write_to_us.setIcon(icon12)
        self.write_to_us.setIconSize(QSize(35, 35))

        self.verticalLayout_11.addWidget(self.write_to_us, 0, Qt.AlignBottom)

        self.verticalLayout_14.addLayout(self.verticalLayout_11)

        self.gridLayout_2.addWidget(self.feedback_frame, 0, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.settings_pages.addWidget(self.feeedback_page)
        self.Appearance_page = QWidget()
        self.Appearance_page.setObjectName(u"Appearance_page")
        self.verticalLayout_8 = QVBoxLayout(self.Appearance_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.appearance_frame = QFrame(self.Appearance_page)
        self.appearance_frame.setObjectName(u"appearance_frame")
        self.appearance_frame.setStyleSheet(u"background-color: black; color: white;")
        self.appearance_frame.setFrameShape(QFrame.NoFrame)
        self.appearance_frame.setFrameShadow(QFrame.Plain)
        self.appearance_frame.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.appearance_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, -1, 0)
        self.verticalSpacer_22 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_22)

        self.pushButton_2 = QPushButton(self.appearance_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font16)
        self.pushButton_2.setStyleSheet(u"color: white; background: transparent;")
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.verticalSpacer_7 = QSpacerItem(3, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.radioButton = QRadioButton(self.appearance_frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 35))
        font17 = QFont()
        font17.setFamily(u"Arial")
        font17.setPointSize(11)
        font17.setItalic(False)
        self.radioButton.setFont(font17)
        self.radioButton.setStyleSheet(u"color: white; text-align: center; background: transparent;")

        self.verticalLayout_9.addWidget(self.radioButton)

        self.comboBox = QComboBox(self.appearance_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setFont(font15)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
                                    " color: white;\n"
                                    " background: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::hover{\n"
                                    " color: white;\n"
                                    " background-color : rgba(255, 255  ,255 ,100);\n"
                                    " border-color: white;\n"
                                    " border-color: rgba(255, 255  ,255 ,150);\n"
                                    "}\n"
                                    "\n"
                                    "QcomboBox::pressed{\n"
                                    " color: white;\n"
                                    "}")

        self.verticalLayout_9.addWidget(self.comboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_7.addWidget(self.appearance_frame)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.settings_pages.addWidget(self.Appearance_page)
        self.NoPage = QWidget()
        self.NoPage.setObjectName(u"NoPage")
        self.horizontalLayout_9 = QHBoxLayout(self.NoPage)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.blank_page = QFrame(self.NoPage)
        self.blank_page.setObjectName(u"blank_page")
        self.blank_page.setFrameShape(QFrame.StyledPanel)
        self.blank_page.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.blank_page)

        self.horizontalLayout_9.addLayout(self.verticalLayout_17)

        self.settings_pages.addWidget(self.NoPage)

        self.horizontalLayout_5.addWidget(self.settings_pages)

        self.horizontalLayout_4.addWidget(self.settings_pages_frame)

        self.stackedWidget.addWidget(self.goto_settings)
        self.private_tab_page = QWidget()
        self.private_tab_page.setObjectName(u"private_tab_page")
        self.stackedWidget.addWidget(self.private_tab_page)
        self.extension_page = QWidget()
        self.extension_page.setObjectName(u"extension_page")
        self.stackedWidget.addWidget(self.extension_page)
        self.blank = QWidget()
        self.blank.setObjectName(u"blank")
        self.stackedWidget.addWidget(self.blank)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.top_frame = QFrame(iSurf)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy8)
        self.top_frame.setMinimumSize(QSize(0, 20))
        self.top_frame.setStyleSheet(u"background-color: black;")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.collapse = QPushButton(self.top_frame)
        self.collapse.setObjectName(u"collapse")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.collapse.sizePolicy().hasHeightForWidth())
        self.collapse.setSizePolicy(sizePolicy9)
        self.collapse.setMinimumSize(QSize(20, 0))
        self.collapse.setFont(font1)
        self.collapse.setStyleSheet(u"color: white; background: transparent;")
        icon13 = QIcon()
        icon13.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/menu.png", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.collapse.setIcon(icon13)

        self.horizontalLayout_8.addWidget(self.collapse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.top_frame)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover{\n"
                                    " color: white;\n"
                                    " background-color : rgba(255, 255  ,255 ,70);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed{\n"
                                    " background-color: rgba(255, 255, 255, 30)\n"
                                    "}\n"
                                    "")
        icon14 = QIcon()
        icon14.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/minimize.png", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon14)

        self.horizontalLayout_8.addWidget(self.minimize)

        self.maximize = QPushButton(self.top_frame)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setStyleSheet(u"QPushButton{\n"
                                    "color: white;\n"
                                    "background: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover{\n"
                                    " color: white;\n"
                                    " background-color : rgba(255, 255  ,255 ,70);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed{\n"
                                    " background-color: rgba(255, 255, 255, 30)\n"
                                    "}\n"
                                    "")
        icon15 = QIcon()
        icon15.addFile(u"C:/Users/Windows Ultra/PycharmProjects/untitled/assets/resources/images/maximize.png", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.maximize.setIcon(icon15)

        self.horizontalLayout_8.addWidget(self.maximize)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.close = QPushButton(self.top_frame)
        self.close.setObjectName(u"close")
        self.close.setStyleSheet(u"QPushButton{\n"
                                 "color: white;\n"
                                 "background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton::hover{\n"
                                 "  color: white;\n"
                                 "  background-color : rgba(255, 255  ,255 ,70);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton::pressed{\n"
                                 "  background-color: rgba(255, 255, 255, 30)\n"
                                 "}\n"
                                 "")
        self.close.setIcon(icon11)

        self.horizontalLayout_7.addWidget(self.close)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.gridLayout.addWidget(self.top_frame, 0, 0, 1, 1)

        self.retranslateUi(iSurf)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.settings_pages.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(iSurf)
        # setupUi

    def retranslateUi(self, iSurf):
        iSurf.setWindowTitle(QCoreApplication.translate("iSurf.exe", u"iSurf.exe", None))
        self.new_tab.setText(QCoreApplication.translate("iSurf.exe", u" New Tab       ", None))
        self.private_tab.setText(QCoreApplication.translate("iSurf.exe", u"  Private Tab", None))
        self.history.setText(QCoreApplication.translate("iSurf.exe", u"  History        ", None))
        self.profile.setText(QCoreApplication.translate("iSurf.exe", u" My  Profile  ", None))
        self.extension.setText(QCoreApplication.translate("iSurf.exe", u" Extensions ", None))
        self.settings.setText(QCoreApplication.translate("iSurf.exe", u"Settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("iSurf.exe", u" Profile", None))
        self.label_7.setText(QCoreApplication.translate("iSurf.exe", u"Your Name ", None))
        self.profile_name_edit.setText(QCoreApplication.translate("iSurf.exe", u"Mr. Whoever", None))
        self.label_10.setText(QCoreApplication.translate("iSurf.exe", u"Gmail Username  ", None))
        self.profile_username_edit.setText(QCoreApplication.translate("iSurf.exe", u"LegendAwkaken4@gmail.com", None))
        self.label_8.setText(QCoreApplication.translate("iSurf.exe", u"Gmail Password ", None))
        self.profile_save_button.setText(QCoreApplication.translate("iSurf.exe", u"Save Profile", None))
        self.history_label.setText(QCoreApplication.translate("iSurf.exe", u" History", None))
        self.history_indicator.setText(QCoreApplication.translate("iSurf.exe", u"Nothing is here.", None))
        self.label_5.setText(QCoreApplication.translate("iSurf.exe", u"Welcome Mr. whoever!", None))
        self.label_6.setText(QCoreApplication.translate("iSurf.exe",
                                                        u"Thank you for choosing this beautiful browser, please send your feedback as contribution in development.",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("iSurf.exe", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("iSurf.exe", u"Tab 2", None))
        self.settings_button.setText(QCoreApplication.translate("iSurf.exe", u" Settings ", None))
        # if QT_CONFIG(shortcut)
        self.settings_button.setShortcut(QCoreApplication.translate("iSurf.exe", u"Ctrl+R", None))
        # endif // QT_CONFIG(shortcut)
        self.appearance.setText(QCoreApplication.translate("iSurf.exe", u"  Appearance  ", None))
        self.passwords.setText(QCoreApplication.translate("iSurf.exe", u"  Passwords  ", None))
        self.startup.setText(QCoreApplication.translate("iSurf.exe", u"  On Startup   ", None))
        self.downloads.setText(QCoreApplication.translate("iSurf.exe", u"  Downloads   ", None))
        self.feedback.setText(QCoreApplication.translate("iSurf.exe", u"  Feedback  ", None))
        self.start_up_label.setText(QCoreApplication.translate("iSurf.exe", u" StartUp", None))
        self.radioButton_2.setText(QCoreApplication.translate("iSurf.exe", u"Open a net tab.", None))
        self.radioButton_4.setText(QCoreApplication.translate("iSurf.exe", u"Continue where you left.", None))
        self.radioButton_3.setText(QCoreApplication.translate("iSurf.exe", u"Open a specific page.", None))
        self.specific_page_url.setText(QCoreApplication.translate("iSurf.exe", u"www.gooogle.co.in", None))
        self.pushButton.setText(QCoreApplication.translate("iSurf.exe", u"  Downloads", None))
        self.label.setText(QCoreApplication.translate("iSurf.exe", u"Download Path : ", None))
        self.lineEdit.setText(QCoreApplication.translate("iSurf.exe", u"C:\\Users\\--User\\Downloads", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("iSurf.exe", u"Help & Feedback", None))
        self.label_4.setText(QCoreApplication.translate("iSurf.exe",
                                                        u"You can make contribution in the development of this software  by telling us what you do not like about this application at Legendawaken4@gmail.com. This app is under development please contact us and report your issue it may get fixed in the next release.",
                                                        None))
        self.close_writ_to_us.setText("")
        self.write_to_us.setText(QCoreApplication.translate("iSurf.exe", u"  Write to Us ", None))
        self.pushButton_2.setText(QCoreApplication.translate("iSurf.exe", u" Appearance", None))
        self.radioButton.setText(QCoreApplication.translate("iSurf.exe", u"Elegant Effect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("iSurf.exe", u"Theme : Default", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("iSurf.exe", u"Acrylic", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("iSurf.exe", u"Transparent", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("iSurf.exe", u"Blur", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("iSurf.exe", u"Light", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("iSurf.exe", u"Dark", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("iSurf.exe", u"Amoled", None))

        self.collapse.setText(QCoreApplication.translate("iSurf.exe", u"  iSurf Pro", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.close.setText("")

    def slideMenu(self, value=True | False):
        width = self.graphics.width()

        if width == 300 or value == True:
            # decrease the slide menu size
            self.graphics.setMinimumSize(QSize(10, 0))

            # set name
            self.new_tab.setText("")
            self.history.setText("")
            self.extension.setText("")
            self.profile.setText("")
            self.settings.setText("")
            self.private_tab.setText("")

            with open("assets/resources/holder.tru", 'r') as place:
                value = str(place.read())

            self.settings_3.setStyleSheet(f"""
                background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{value}.jpeg);
                background-repeat: no-repeat;
                background-position: left;
                border: 0;
            """)

            return -1

        else:
            # increae the size
            self.graphics.setMinimumSize(QSize(300, 0))

            # set name
            self.new_tab.setText(" New Tab       ")
            self.history.setText("  History        ")
            self.extension.setText(" Extensions ")
            self.profile.setText(" My  Profile  ")
            self.settings.setText("Settings")
            self.private_tab.setText("  Private Tab")

            with open("assets/resources/holder.tru", 'r') as place:
                value = str(place.read())

            self.settings_3.setStyleSheet(f"""
                          background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{value}.jpeg);
                          background-repeat: no-repeat;
                          background-position: left center;
                          border: 0;
                      """)

        if self.graphics.width() == 38:
            return "closed"

        else:
            return "opened"

    def slideSettingsMenu(self, value=True | False):

        width = self.settings_3.width()

        if width == 240 or value == True:
            self.settings_3.setMinimumSize(QSize(5, 0))
            self.settings_button.setText("")
            self.appearance.setText("")
            self.startup.setText("")
            self.passwords.setText("")
            self.downloads.setText("")
            self.feedback.setText("")

        else:
            self.settings_3.setMinimumSize((QSize(240, 0)))
            self.settings_button.setText("  Settings ")
            self.appearance.setText("  Appearance  ")
            self.startup.setText("  On Startup   ")
            self.passwords.setText("  Passwords  ")
            self.downloads.setText("  Downloads   ")
            self.feedback.setText("  Feedback  ")

    def fluentHandler(self):
        # FRAME 1
        with open("assets/resources/holder.tru", "r") as reader_:
            r = str(reader_.read())

        self.graphics.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                                   background-repeat: repeat;
                                   background-position: left;
                                   border: 0;""")

        # FRAME 2
        self.settings_3.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: left center;
                                   border: 0;
                               """)

        # FRAME 3
        self.top_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                                   background-repeat: repeat;
                                   background-position: top;
                                   border: 0;
                               """)
        self.profile_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: repeat;
                                   background-position: top;
                                   border: 0;
                               """)
        self.appearance_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)
        self.downloads_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)
        self.startup_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)
        self.new_tab_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)
        self.history_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)
        self.feedback_frame.setStyleSheet(f"""
                                   background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                                   background-repeat: no-repeat;
                                   background-position: center;
                                   border: 0;
                               """)

    def stop(self):
        sys.exit()

    def min(self):
        self.showMinimized()

    def max_reduce(self):
        if self.isMaximized():
            self.showNormal()
            icon = QIcon()
            icon.addFile("assets/resources/images/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
            self.maximize.setIcon(icon)
        else:
            self.showMaximized()
            icon = QIcon()
            icon.addFile("assets/resources/images/estore.png", QSize(), QIcon.Normal, QIcon.Off)
            self.maximize.setIcon(icon)

    def settingsUI(self):
        self.stackedWidget.setCurrentIndex(3)
        with open("assets/resources/holder.tru", 'r') as place:
            value = str(place.read())

        val = self.slideMenu(False)

        if val == -1:
            self.settings_3.setStyleSheet(f"""
                background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{value}.jpeg);
                background-repeat: no-repeat;
                background-position: left;
                border: 0;
            """)

        else:
            self.settings_3.setStyleSheet(f"""
                background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{value}.jpeg);
                background-repeat: no-repeat;
                background-position: left center;
                border: 0;
            """)

    def appearance_UI(self):
        self.slideMenu(True)
        self.settings_pages.setCurrentIndex(3)

    def startup_UI(self):
        self.slideMenu(True)
        self.settings_pages.setCurrentIndex(0)

    def downloads_UI(self):
        self.slideMenu(True)
        self.settings_pages.setCurrentIndex(1)

    def feedback_UI(self):
        self.slideMenu(True)
        self.settings_pages.setCurrentIndex(2)

    def remove_feedback_graphics(self):
        feedback_blur_remove = QGraphicsBlurEffect()
        feedback_blur_remove.setBlurRadius(0.0)
        settings_blur_remove = QGraphicsBlurEffect()
        settings_blur_remove.setBlurRadius(0.0)
        self.feedback_graphics_frame.setGraphicsEffect(feedback_blur_remove)
        self.settings_3.setGraphicsEffect(settings_blur_remove)
        self.write_to_us.setText(" Write to us.")
        self.close_writ_to_us.setIcon(QIcon(""))
        self.write_to_us_box.setPlainText("")
        self.settings_3.setEnabled(True)

    def feedback_graphics_effect_UI(self):
        feedback_frame_blur = QGraphicsBlurEffect()
        feedback_frame_blur.setBlurRadius(15.0)
        settings_frame_blur = QGraphicsBlurEffect()
        settings_frame_blur.setBlurRadius(15.0)
        self.write_to_us_box.setPlainText("         Write Here")

        if self.write_to_us_box.isEnabled():
            self.write_to_us.setText("Send Feedback.")
            self.close_writ_to_us.setIcon(QIcon("assets/resources/images/close.png"))
            self.close_writ_to_us.clicked.connect(self.remove_feedback_graphics)

        # self.setBlurRadius(15.0)
        self.feedback_graphics_frame.setGraphicsEffect(feedback_frame_blur)
        self.settings_3.setGraphicsEffect(settings_frame_blur)
        self.settings_3.setDisabled(True)

    def new_tab_UI(self):
        self.stackedWidget.setCurrentIndex(2)
        if self.isMaximized():
            self.fluentHandler()
        self.add_new_tab()

    def functionalities(self):

        # Title bar buttons
        self.close.clicked.connect(self.stop)
        self.minimize.clicked.connect(self.min)
        self.maximize.clicked.connect(self.max_reduce)

        # Main UI
        self.collapse.clicked.connect(self.slideMenu)
        self.settings.clicked.connect(self.settingsUI)
        self.feedback.clicked.connect(self.feedback_UI)
        self.appearance.clicked.connect(self.appearance_UI)
        self.settings_button.clicked.connect(lambda: self.slideSettingsMenu(False))
        self.startup.clicked.connect(self.startup_UI)
        self.downloads.clicked.connect(self.downloads_UI)
        self.write_to_us.clicked.connect(self.feedback_graphics_effect_UI)

        # graphics widgets
        self.profile.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.new_tab.clicked.connect(self.new_tab_UI)
        self.history.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # set slide menu collapsed
        self.slideMenu(False)

        # making document mode true
        self.tabWidget.setDocumentMode(True)

        # adding action when double clicked
        self.tabWidget.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # adding action when tab is changed
        # self.tabWidget.currentChanged.connect(self.current_tab_changed)

        # making tabs closeable
        self.tabWidget.setTabsClosable(True)

        self.tabWidget.setMovable(True)

        # adding action when tab close is requested
        self.tabWidget.tabCloseRequested.connect(self.close_current_tab)

        self.tabWidget.removeTab(1)

        self.tabWidget.setTabText(0, "Welcome")

        # creating first tab
        self.add_new_tab(QUrl('http://www.google.com'), 'Google')

    def add_new_tab(self, qurl=None, label="Blank"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)

        browser.page().setBackgroundColor(Qt.transparent)

        browser.setStyleSheet("""background: transparent;""")

        # setting tab index
        i = self.tabWidget.addTab(browser, label)
        self.tabWidget.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        # browser.urlChanged.connect(lambda qurl, browser = browser:
        #             self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabWidget.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self):

        self.add_new_tab()

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):

        qurl = self.tabWidget.currentWidget().url()

        # update the url
        self.update_urlbar(qurl, self.tabWidget.currentWidget())

        # update the title
        self.update_title(self.tabWidget.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabWidget.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabWidget.removeTab(i)

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabWidget.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabWidget.currentWidget().page().title()

        MainWindow.setWindowTitle(title)

    # action to go to home
    def navigate_home(self):

        # go to google
        self.tabWidget.currentWidget().setUrl(QUrl("http://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabWidget.currentWidget().setUrl(q)


class UI:
    def __init__(self):
        Thread(target=self.cleaner).start()

    # @ staticmethod
    def check_window(self):
        try:
            # get the current active window
            a = pygetwindow.getActiveWindowTitle()

            if str(a) != "iSurf.exe":
                try:
                    # minimize
                    MainWindow.showMinimized()

                    # grab screen
                    get_image = screenshot()

                    # random value grabber
                    r = str(randint(10, 100000))

                    # save value into a file for furure use
                    with open("assets/resources/holder.tru", 'w') as hold:
                        hold.write(r)

                    # save at this location
                    get_image.save(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')

                    # Frame One UI
                    frame_one_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
                    skinned_ = Image.eval(frame_one_image, lambda x: x / 2)
                    # blur the image
                    frame_one_blurred_image = skinned_.filter(GaussianBlur(radius=15))
                    frame_one_blurred_image.save(f"C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg")

                    # Frame TwoUI
                    frame_two_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
                    # # dim the image
                    skinned_image = Image.eval(frame_two_image, lambda x: x / 3)
                    frame_two_blurred_image = skinned_image.filter(GaussianBlur(radius=30))
                    frame_two_blurred_image.save(f"C:/Users/{USER}/AppData/Local/Temp/vis_reb2{r}.jpeg")

                    # frame 3 UI
                    frame_three_image = Image.open(f'C:/Users/{USER}/AppData/Local/Temp/vis_ref{r}.jpeg')
                    skinned_image_frame_three = Image.eval(frame_three_image, lambda x: x / 4)
                    frame_three_blurred_image = skinned_image_frame_three.filter(GaussianBlur(radius=70))
                    frame_three_blurred_image.save(f'C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg')

                # will raise OS error if image is subjected to modifications
                except OSError:
                    pass

            elif MainWindow.isMaximized():
                MainWindow.setWindowOpacity(1.0)

                # FRAMES UI

                # FRAME 1
                with open("assets/resources/qr.tru", "r") as reader:
                    read = str(reader.read())

                if read == "True":
                    with open("assets/resources/holder.tru", "r") as reader:
                        r = str(reader.read())

                    MainWindow.graphics.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                        background-repeat: repeat;
                        background-position: left;
                        border: 0;""")

                    # FRAME 2
                    MainWindow.settings_3.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb2{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: left center;
                        border: 0;
                    """)

                    # FRAME 3
                    MainWindow.top_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb1{r}.jpeg);
                        background-repeat: repeat;
                        background-position: top;
                        border: 0;
                    """)
                    MainWindow.profile_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: repeat;
                        background-position: top;
                        border: 0;
                    """)
                    MainWindow.appearance_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)
                    MainWindow.downloads_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)
                    MainWindow.startup_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)
                    MainWindow.new_tab_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)
                    MainWindow.history_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)
                    MainWindow.feedback_frame.setStyleSheet(f"""
                        background: url(C:/Users/{USER}/AppData/Local/Temp/vis_reb3{r}.jpeg);
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 0;
                    """)

                    with open("assets/resources/qr.tru", "w") as writer:
                        writer.write("False")

            else:
                pass
        except NameError:
            pass

    def no_screen(self):
        current = pygetwindow.getActiveWindowTitle()
        if MainWindow.isMinimized() or current != "iSurf.exe" or not MainWindow.isMaximized():
            with open("assets/resources/block.tru", "w") as writer:
                writer.write("True")
            with open("assets/resources/qr.tru", "w") as writer:
                writer.write("True")
        if MainWindow.isMaximized():
            MainWindow.setWindowOpacity(1.0)
            with open("assets/resources/block.tru", 'r') as reader:
                read = str(reader.read())
            if read == "True":
                MainWindow.fluentHandler()
                with open("assets/resources/block.tru", "w") as writer:
                    writer.write("False")

        else:
            if not MainWindow.isMaximized():
                MainWindow.setStyleSheet("""background-color: black;""")
                MainWindow.graphics.setStyleSheet("""background-color: black;""")
                MainWindow.top_frame.setStyleSheet("""background-color: black;""")
                MainWindow.settings_3.setStyleSheet("""background-color: black;""")
                MainWindow.appearance_frame.setStyleSheet("""background-color: black;""")
                MainWindow.feedback_frame.setStyleSheet("""background-color: black;""")
                MainWindow.downloads_frame.setStyleSheet("""background-color: black;""")
                MainWindow.startup_frame.setStyleSheet("""background-color: black;""")
                MainWindow.profile_frame.setStyleSheet("""background-color: black;""")
                MainWindow.history_frame.setStyleSheet("""background-color: black;""")
                MainWindow.startup_frame.setStyleSheet("""background-color: black;""")
                MainWindow.new_tab_frame.setStyleSheet("""background-color: black;""")
                MainWindow.setWindowOpacity(0.97)

    def cleaner(self):
        walker = os.walk(f'C:/Users/{USER}/AppData/Local/Temp')

        for i in walker:
            r = i[2]
            for g in r:
                if g.endswith('.jpeg'):
                    with open(f'assets/resources/holder.tru', "r") as t:
                        ri = str(t.read())
                    if ri in str(g):
                        pass
                    else:
                        z = g
                        try:
                            os.remove(f"C:/Users/{USER}/AppData/Local/Temp/{z}")
                        except (PermissionError, FileNotFoundError):
                            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = QTimer()
    main = UI()
    timer.timeout.connect(main.no_screen)
    timer.timeout.connect(main.cleaner)
    timer.timeout.connect(main.check_window)
    timer.setInterval(100 / 150)
    timer.start()
    MainWindow = Main()
    MainWindow.show()
    app.exec()
