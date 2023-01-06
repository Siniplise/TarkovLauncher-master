import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

import ClientLoggingHandler

import ClientConfiger
import LauncherCore
import MainSources_Rc

ClientLoggingHandler.Log_Client.info("客户端初始化...")
ClientLoggingHandler.Log_Client.info("获取SPT-AKI服务器IP...")
IP = ClientConfiger.ser["ip"]
Port = ClientConfiger.ser["port"]
Url = str(IP) + str(":") + str(Port)
ClientLoggingHandler.Log_Client.info("获取SPT-AKI服务器IP - 成功")
ClientLoggingHandler.Log_Client.info("开始构建启动函数")
MainToken = "None"
UserSides = "None"
UserLevel = "None"


def SetToken(NToken):
    global MainToken
    if NToken == ClientConfiger.CharacterPMCNNamej1:
        MainToken = ClientConfiger.UserIDj1
        ClientLoggingHandler.Log_Client.info(f"启动存档设置为{MainToken}")
        return MainToken
    elif NToken == ClientConfiger.CharacterPMCNNamej2:
        MainToken = ClientConfiger.UserIDj2
        ClientLoggingHandler.Log_Client.info(f"启动存档设置为{MainToken}")
        return MainToken
    else:
        ClientLoggingHandler.Log_Client.critical("找不到用户存档!")
        print(Exception)
        sys.exit()


def launchmain(tokens):
    ClientLoggingHandler.Log_Client.info(f"当前启动存档: {MainToken}")
    MainC = LauncherCore.Command(
        maindir=ClientConfiger.MainDirectory,
        token=tokens,
        url=Url,
        version="live"
    )
    ClientLoggingHandler.Log_Client.info(f"启动参数已设置: {MainC}")
    LCH = LauncherCore.MainLaunch(TarkovLaunchCommand=MainC)
    if LCH:
        ClientLoggingHandler.Log_Client.info("逃离塔克夫 已启动,请等待")
    else:
        ClientLoggingHandler.Log_Client.info("逃离塔克夫 启动失败")
        print(Exception)
        sys.exit()


def SetMainSide(Sides):
    global UserSides
    if Sides == ClientConfiger.CharacterPMCNNamej1:
        UserSides = "SIDE: " + ClientConfiger.CharacterPMCSidej1
        ClientLoggingHandler.Log_Client.info(f"Side:{UserSides}")
    elif Sides == ClientConfiger.CharacterPMCNNamej2:
        UserSides = "SIDE: " + ClientConfiger.CharacterPMCSidej2
        ClientLoggingHandler.Log_Client.info(f"Side:{UserSides}")
    else:
        ClientLoggingHandler.Log_Client.critical("阵营读取错误!")
        print(Exception)
        sys.exit()


def SetMainLev(User):
    global UserLevel
    if User == ClientConfiger.CharacterPMCNNamej1:
        UserLevel = "LEVEL: " + str(ClientConfiger.CharacterPMCLvlj1)
    elif User == ClientConfiger.CharacterPMCNNamej2:
        UserLevel = "LEVEL: " + str(ClientConfiger.CharacterPMCLvlj2)
    else:
        ClientLoggingHandler.Log_Client.critical("等级读取错误!")
        print(Exception)
        sys.exit()


ClientLoggingHandler.Log_Client.info("开始构建GUI")
try:
    class Ui_EscTkvLchGui(object):
        ClientLoggingHandler.Log_Client.info("setupui...")
        def setupUi(self, EscTkvLchGui):
            global UserSides
            EscTkvLchGui.setObjectName("EscTkvLchGui")
            EscTkvLchGui.setWindowModality(QtCore.Qt.ApplicationModal)
            EscTkvLchGui.resize(1024, 768)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(EscTkvLchGui.sizePolicy().hasHeightForWidth())
            EscTkvLchGui.setSizePolicy(sizePolicy)
            EscTkvLchGui.setMinimumSize(QtCore.QSize(1024, 768))
            EscTkvLchGui.setMaximumSize(QtCore.QSize(1024, 768))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            EscTkvLchGui.setPalette(palette)
            font = QtGui.QFont()
            font.setFamily("Cascadia Code")
            font.setPointSize(16)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            EscTkvLchGui.setFont(font)
            EscTkvLchGui.setMouseTracking(False)
            EscTkvLchGui.setTabletTracking(False)
            EscTkvLchGui.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/assets/unknown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            EscTkvLchGui.setWindowIcon(icon)
            EscTkvLchGui.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                       "selection-background-color: rgb(129, 129, 129);\n"
                                       "selection-color: rgb(163, 163, 163);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(24, 26, 24);\n"
                                       "font: 16pt \"Cascadia Code\";image: url(:/assets/tempSplash.png);")
            EscTkvLchGui.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
            self.EscapeFromTarkovLauncher = QtWidgets.QWidget(EscTkvLchGui)
            self.EscapeFromTarkovLauncher.setObjectName("EscapeFromTarkovLauncher")
            self.label_INFO = QtWidgets.QLabel(self.EscapeFromTarkovLauncher)
            self.label_INFO.setGeometry(QtCore.QRect(300, 530, 51, 41))
            self.label_INFO.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgba(255, 255, 255, 0);\n"
                                          "font: 75 16pt \"Cascadia Code\";\n"
                                          "")
            self.label_INFO.setObjectName("label_INFO")
            self.label_IP = QtWidgets.QLabel(self.EscapeFromTarkovLauncher)
            self.label_IP.setGeometry(QtCore.QRect(310, 580, 41, 41))
            self.label_IP.setStyleSheet("font: 75 16pt \"Bahnschrift Condensed\";\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "image: url(:/assets/simpleback.png);\n"
                                        "font: 75 16pt \"Cascadia Code\";")
            self.label_IP.setObjectName("label_IP")
            self.Launch = QtWidgets.QPushButton(self.EscapeFromTarkovLauncher)
            self.Launch.setGeometry(QtCore.QRect(300, 420, 411, 53))
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Condensed")
            font.setPointSize(20)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(9)
            self.Launch.setFont(font)
            self.Launch.setMouseTracking(True)
            self.Launch.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "image: url(:/assets/ef2t.png);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "font: 75 20pt \"Bahnschrift Condensed\";\n"
                                      "\n"
                                      "")
            self.Launch.setCheckable(True)
            self.Launch.setAutoDefault(True)
            self.Launch.setDefault(True)
            self.Launch.setFlat(True)
            self.Launch.setObjectName("Launch")
            self.Side = QtWidgets.QTextBrowser(self.EscapeFromTarkovLauncher)
            self.Side.setGeometry(QtCore.QRect(360, 530, 151, 41))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.Side.setPalette(palette)
            self.Side.setMouseTracking(False)
            self.Side.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                    "\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(24, 26, 24);\n"
                                    "\n"
                                    "font: 16pt \"Cascadia Code\";\n"
                                    "")
            self.Side.setObjectName("Side")
            self.Level = QtWidgets.QTextBrowser(self.EscapeFromTarkovLauncher)
            self.Level.setGeometry(QtCore.QRect(520, 530, 141, 41))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(24, 26, 24))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
            brush.setStyle(QtCore.Qt.NoBrush)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            self.Level.setPalette(palette)
            self.Level.setMouseTracking(False)
            self.Level.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                     "selection-background-color: rgb(129, 129, 129);\n"
                                     "selection-color: rgb(163, 163, 163);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(24, 26, 24);\n"
                                     "font: 16pt \"Cascadia Code\";")
            self.Level.setObjectName("Level")
            self.NickName = QtWidgets.QComboBox(self.EscapeFromTarkovLauncher)
            self.NickName.setGeometry(QtCore.QRect(300, 480, 411, 41))
            font = QtGui.QFont()
            font.setFamily("Trebuchet MS")
            font.setPointSize(16)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.NickName.setFont(font)
            self.NickName.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                        "font: 16pt \"Trebuchet MS\";\n"
                                        "selection-background-color: rgb(129, 129, 129);\n"
                                        "selection-color: rgb(163, 163, 163);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(24, 26, 24);\n"
                                        "")
            self.NickName.setObjectName("NickName")
            self.Side_BEAR = QtWidgets.QFrame(self.EscapeFromTarkovLauncher)
            self.Side_BEAR.setGeometry(QtCore.QRect(670, 530, 41, 41))
            self.Side_BEAR.setStyleSheet("image: url(:/assets/side_bear.png);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
            self.Side_BEAR.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Side_BEAR.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Side_BEAR.setObjectName("Side_BEAR")
            self.label_Copyright = QtWidgets.QLabel(self.EscapeFromTarkovLauncher)
            self.label_Copyright.setGeometry(QtCore.QRect(10, 730, 611, 31))
            self.label_Copyright.setStyleSheet("image: url(:/assets/simpleback.png);\n"
                                               "background-color: rgba(255, 255, 255, 0);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 12pt \"Cascadia Code\";\n"
                                               ";")
            self.label_Copyright.setObjectName("label_Copyright")
            self.Side_USEC = QtWidgets.QFrame(self.EscapeFromTarkovLauncher)
            self.Side_USEC.setEnabled(True)
            self.Side_USEC.setGeometry(QtCore.QRect(670, 530, 41, 41))
            self.Side_USEC.setStyleSheet("image: url(:/assets/side_usec.png);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
            self.Side_USEC.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Side_USEC.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Side_USEC.setObjectName("Side_USEC")
            self.IP_Display = QtWidgets.QTextBrowser(self.EscapeFromTarkovLauncher)
            self.IP_Display.setGeometry(QtCore.QRect(360, 580, 351, 41))
            self.IP_Display.setObjectName("IP_Display")
            self.label_INFO.raise_()
            self.label_IP.raise_()
            self.Launch.raise_()
            self.Side.raise_()
            self.Level.raise_()
            self.NickName.raise_()
            self.label_Copyright.raise_()
            self.Side_USEC.raise_()
            self.IP_Display.raise_()
            self.Side_BEAR.raise_()
            EscTkvLchGui.setCentralWidget(self.EscapeFromTarkovLauncher)
            self.label_INFO.setBuddy(self.Side)

            self.retranslateUi(EscTkvLchGui)
            ClientLoggingHandler.Log_Client.info("UI槽")
            self.Launch.clicked.connect(lambda: launchmain(tokens=MainToken))
            QtCore.QMetaObject.connectSlotsByName(EscTkvLchGui)
            EscTkvLchGui.setTabOrder(self.Launch, self.NickName)
            EscTkvLchGui.setTabOrder(self.NickName, self.Side)
            EscTkvLchGui.setTabOrder(self.Side, self.Level)
            self.NickName.addItem(ClientConfiger.CharacterPMCNNamej1)
            self.NickName.addItem(ClientConfiger.CharacterPMCNNamej2)
            self.NickName.currentIndexChanged.connect(lambda: SetToken(NToken=self.NickName.currentText()))
            self.NickName.currentIndexChanged.connect(lambda: SetInfoSide())
            self.NickName.currentIndexChanged.connect(lambda: SetInfoLevel())
            self.NickName.currentIndexChanged.connect(lambda: SetUserSide())

            ClientLoggingHandler.Log_Client.info("UI槽函数")

            def SetUserToken():
                SetToken(NToken=self.NickName.currentText())

            def SetInfoSide():
                SetMainSide(Sides=self.NickName.currentText())
                self.Side.setText(UserSides.upper())

            def SetInfoLevel():
                SetMainLev(User=self.NickName.currentText())
                self.Level.setText(UserLevel)

            def SetUserSide():
                if self.NickName.currentText() == ClientConfiger.CharacterPMCNNamej1:
                    self.Side_BEAR.show()
                    self.Side_USEC.hide()
                elif self.NickName.currentText() == ClientConfiger.CharacterPMCNNamej2:
                    self.Side_BEAR.hide()
                    self.Side_USEC.show()
                else:
                    ClientLoggingHandler.Log_Client.info("阵营图标错误")
                    sys.exit()

            ClientLoggingHandler.Log_Client.info("初始化UI")

            self.IP_Display.setText("http://" + Url)
            SetUserToken()
            SetInfoSide()
            SetInfoLevel()
            SetUserSide()

        def retranslateUi(self, EscTkvLchGui):
            ClientLoggingHandler.Log_Client.info("配置UI标签")
            _translate = QtCore.QCoreApplication.translate
            EscTkvLchGui.setWindowTitle(_translate("EscTkvLchGui", "EscapeFromTarkovLauncher"))
            self.label_INFO.setText(_translate("EscTkvLchGui", "INFO"))
            self.label_IP.setText(_translate("EscTkvLchGui", "IP"))
            self.Launch.setText(_translate("EscTkvLchGui", "E S C A P E   F R O M   T A R K O V "))
            self.Side.setHtml(_translate("EscTkvLchGui",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Cascadia Code\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
            self.Level.setHtml(_translate("EscTkvLchGui",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Cascadia Code\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
            self.label_Copyright.setText(
                _translate("EscTkvLchGui", "0.12.98.1 BETA --Escape From Tarkov Launcher - Creade By Siniplis1e"))
            self.IP_Display.setHtml(_translate("EscTkvLchGui",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Cascadia Code\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    ClientLoggingHandler.Log_Client.info("GUI构建成功!")
except Exception:
    ClientLoggingHandler.Log_Client.critical("主线程错误: GUI构建失败!")
    print(Exception)
    sys.exit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ClientLoggingHandler.Log_Client.info("GUI实例构建成功!")
    ui = Ui_EscTkvLchGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ClientLoggingHandler.Log_Client.info("弹出GUI窗体")
    sys.exit(app.exec_())
