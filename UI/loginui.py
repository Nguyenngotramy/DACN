# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:#F5F7FA;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 100, 551, 111))
        self.label.setStyleSheet("\n"
"color: 2C3E50 ;\n"
"border: none;")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(260, 220, 551, 461))
        self.widget.setStyleSheet("border:none;")
        self.widget.setObjectName("widget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 10, 341, 71))
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
"    color: #2C3E50;\n"
"    border: 1.5px solid #2C3E50;\n"
"    border-radius: 15px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 30px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.passw = QtWidgets.QLineEdit(self.widget)
        self.passw.setGeometry(QtCore.QRect(200, 117, 341, 71))
        self.passw.setStyleSheet("background-color: white;\n"
"    color: #2C3E50;\n"
"    border: 1.5px solid #2C3E50;\n"
"    border-radius: 15px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 50px;")
        self.passw.setText("")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw.setObjectName("passw")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(11, 11, 126, 50))
        self.label_2.setStyleSheet("color: rgb(44, 62, 80);                          \n"
"padding: 8px 16px;   \n"
"font-size: 28px; \n"
"font-weight: bold; ")
        self.label_2.setObjectName("label_2")
        self.lb = QtWidgets.QLabel(self.widget)
        self.lb.setGeometry(QtCore.QRect(0, 130, 184, 50))
        self.lb.setStyleSheet("color: rgb(44, 62, 80);                \n"
"padding: 8px 16px;   \n"
"font-size: 28px; \n"
"font-weight: bold; ")
        self.lb.setObjectName("lb")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 280, 521, 71))
        self.pushButton_2.setStyleSheet("background-color: white;\n"
"    color: #2C3E50;\n"
"    border: 1.5px solid #2C3E50;\n"
"    border-radius: 15px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(120, 230, 253, 42))
        self.pushButton.setStyleSheet("color: #2C3E50;\n"
"border: none;\n"
"border-radius: 15px;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"padding: 10px 50px;\n"
"font-style: italic;   \n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 370, 521, 71))
        self.pushButton_3.setStyleSheet("background-color:#2C3E50;\n"
"    color: white;\n"
"    border: 1.5px solid white;\n"
"    border-radius: 15px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px 20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#2c3e50;\">LOGIN</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.lb.setText(_translate("MainWindow", "Password"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Foget password?"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
