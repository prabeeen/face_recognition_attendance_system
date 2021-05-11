# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1360, 760)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 228, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 228, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 228, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 228, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        Form.setFont(font)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 87, 285, 628))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(64, 66, 226)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 70, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 140, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 210, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 280, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 350, 285, 74))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 540, 285, 84))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color:rgb(255, 0, 0);\n"
"}")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(102, 25, 921, 37))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(93, 136, 206);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(310, 90, 993, 620))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(220, 228, 254);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.train_data_page = QtWidgets.QWidget()
        self.train_data_page.setObjectName("train_data_page")
        self.train_pushbutton = QtWidgets.QPushButton(self.train_data_page)
        self.train_pushbutton.setGeometry(QtCore.QRect(410, 350, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.train_pushbutton.setFont(font)
        self.train_pushbutton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color:rgb(0, 170, 0);\n"
"}")
        self.train_pushbutton.setObjectName("train_pushbutton")
        self.stackedWidget.addWidget(self.train_data_page)
        self.photo_page = QtWidgets.QWidget()
        self.photo_page.setObjectName("photo_page")
        self.label_2 = QtWidgets.QLabel(self.photo_page)
        self.label_2.setGeometry(QtCore.QRect(400, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.photo_page)
        self.lineEdit.setGeometry(QtCore.QRect(500, 295, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.photo_page)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 360, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.photo_page)
        self.student_info_page = QtWidgets.QWidget()
        self.student_info_page.setObjectName("student_info_page")
        self.label_4 = QtWidgets.QLabel(self.student_info_page)
        self.label_4.setGeometry(QtCore.QRect(490, 230, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.student_info_page)
        self.notify_guardian_page = QtWidgets.QWidget()
        self.notify_guardian_page.setObjectName("notify_guardian_page")
        self.label_3 = QtWidgets.QLabel(self.notify_guardian_page)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.notify_guardian_page)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 291, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.to_line_edit = QtWidgets.QLineEdit(self.notify_guardian_page)
        self.to_line_edit.setGeometry(QtCore.QRect(610, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.to_line_edit.setFont(font)
        self.to_line_edit.setObjectName("to_line_edit")
        self.subject_line_edit = QtWidgets.QLineEdit(self.notify_guardian_page)
        self.subject_line_edit.setGeometry(QtCore.QRect(610, 110, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.subject_line_edit.setFont(font)
        self.subject_line_edit.setObjectName("subject_line_edit")
        self.mail_content_edit = QtWidgets.QTextEdit(self.notify_guardian_page)
        self.mail_content_edit.setGeometry(QtCore.QRect(610, 160, 281, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mail_content_edit.setFont(font)
        self.mail_content_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mail_content_edit.setObjectName("mail_content_edit")
        self.send_mail_button = QtWidgets.QPushButton(self.notify_guardian_page)
        self.send_mail_button.setGeometry(QtCore.QRect(690, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(14)
        self.send_mail_button.setFont(font)
        self.send_mail_button.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.send_mail_button.setObjectName("send_mail_button")
        self.stackedWidget.addWidget(self.notify_guardian_page)
        self.attendance_report_page = QtWidgets.QWidget()
        self.attendance_report_page.setObjectName("attendance_report_page")
        self.label_7 = QtWidgets.QLabel(self.attendance_report_page)
        self.label_7.setGeometry(QtCore.QRect(380, 260, 291, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.attendance_report_page)
        self.recognize_face_page = QtWidgets.QWidget()
        self.recognize_face_page.setObjectName("recognize_face_page")
        self.recognize_face_button = QtWidgets.QPushButton(self.recognize_face_page)
        self.recognize_face_button.setGeometry(QtCore.QRect(380, 310, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.recognize_face_button.setFont(font)
        self.recognize_face_button.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(64, 66, 226);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color:rgb(0, 170, 0);\n"
"}")
        self.recognize_face_button.setObjectName("recognize_face_button")
        self.stackedWidget.addWidget(self.recognize_face_page)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "STUDENT INFO"))
        self.pushButton_2.setText(_translate("Form", "TRAIN DATA"))
        self.pushButton_3.setText(_translate("Form", "PHOTO"))
        self.pushButton_4.setText(_translate("Form", "RECOGNIZE FACE"))
        self.pushButton_5.setText(_translate("Form", "NOTIFY GUARDIAN"))
        self.pushButton_6.setText(_translate("Form", "ATTENDANCE REPORT"))
        self.pushButton_7.setText(_translate("Form", "LOGOUT"))
        self.label_5.setText(_translate("Form", "FACE RECOGNITION ATTENDANCE SYSTEM"))
        self.label.setText(_translate("Form", "ICON"))
        self.train_pushbutton.setText(_translate("Form", "TRAIN ALGORITHM"))
        self.label_2.setText(_translate("Form", "SEARCH"))
        self.pushButton_8.setText(_translate("Form", "OPEN FOLDER"))
        self.label_4.setText(_translate("Form", "SUDENT PAGE INFO"))
        self.label_3.setText(_translate("Form", "SEARCH"))
        self.to_line_edit.setPlaceholderText(_translate("Form", "To: (Guardian Email)"))
        self.subject_line_edit.setPlaceholderText(_translate("Form", "Subject"))
        self.mail_content_edit.setPlaceholderText(_translate("Form", "Mail Content"))
        self.send_mail_button.setText(_translate("Form", "Send"))
        self.label_7.setText(_translate("Form", "ATTENDANCE REPORT"))
        self.recognize_face_button.setText(_translate("Form", "RECOGNIZE FACES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())