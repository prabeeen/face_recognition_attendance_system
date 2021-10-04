from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QTextEdit, \
    QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, QLabel, QRadioButton, QMainWindow
# For changing Pydate to Qdate
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui

import send2trash
import shutil

import matplotlib.pyplot as plt


from PyQt5 import uic
import sys
import webbrowser
import os
import train_algo
import recognize_face
import smtp_email
import database_connection_test
import mysql.connector as ms
import generate_image
from datetime import date

from openpyxl import Workbook


class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test_ui.ui", self)

        self.login_username_line_edit = self.findChild(QLineEdit, "login_username_line_edit")
        self.login_password_line_edit = self.findChild(QLineEdit, "login_password_line_edit")
        self.login_password_line_edit.setEchoMode(QLineEdit.Password)
        self.login_push_button = self.findChild(QPushButton, "login_push_button")

        self.login_push_button.clicked.connect(self.authenticate_user)

    def authenticate_user(self):
        username = self.login_username_line_edit.text()
        password = self.login_password_line_edit.text()
        if username == "test" and password == "test":
            dashboard_window = DashboardForm()
            stacked_widget.addWidget(dashboard_window)
            stacked_widget.setCurrentIndex(stacked_widget.currentIndex() + 1)
        else:
            QMessageBox.critical(self, 'Face Recognition Attendance System', 'Login Failed')


class DashboardForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("dashboard.ui", self)

        self.messagebox_title = 'Face Recognition Attendance System'

        # Find the elements in the ui files.
        self.search_text = self.findChild(QLineEdit, "lineEdit")
        self.photo_button = self.findChild(QPushButton, "pushButton_8")
        self.train_pushbutton = self.findChild(QPushButton, "train_pushbutton")
        self.recognize_face_button = self.findChild(QPushButton, 'recognize_face_button')
        self.to_line_edit = self.findChild(QLineEdit, 'to_line_edit')
        self.subject_line_edit = self.findChild(QLineEdit, 'subject_line_edit')
        self.mail_content_edit = self.findChild(QTextEdit, 'mail_content_edit')
        self.send_mail_button = self.findChild(QPushButton, 'send_mail_button')
        # Get the stacked pages of stack Widget.
        self.stack_pages = self.findChild(QStackedWidget, "stackedWidget")
        self.stack_pages_train_data_page = self.findChild(QWidget, "train_data_page")
        self.stack_pages_photo_page = self.findChild(QWidget, "photo_page")
        self.stack_pages_student_info_page = self.findChild(QWidget, "student_info_page")
        self.stack_pages_notify_guardian_page = self.findChild(QWidget, "notify_guardian_page")
        self.stack_pages_attendance_report_page = self.findChild(QWidget, "attendance_report_page")
        self.stack_pages_recognize_face_page = self.findChild(QWidget, "recognize_face_page")
        self.stack_pages_attendance_info_page = self.findChild(QWidget, "attendance_info_page")
        # Get the buttons in stackWidget
        self.dashboard_pushButton = self.findChild(QPushButton, 'pushButton')
        self.dashboard_pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.dashboard_pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.dashboard_pushButton_4 = self.findChild(QPushButton, 'pushButton_4')
        self.dashboard_pushButton_5 = self.findChild(QPushButton, 'pushButton_5')
        self.dashboard_pushButton_6 = self.findChild(QPushButton, 'pushButton_6')
        self.dashboard_pushButton_9 = self.findChild(QPushButton, 'pushButton_9')
        self.logout_button = self.findChild(QPushButton, 'logout_button')
        # Set the first page of Stack Widget.
        self.stack_pages.setCurrentWidget(self.stack_pages_student_info_page)
        # Signals generated in stack widget page.
        self.dashboard_pushButton.clicked.connect(self.open_student_info_page)
        self.dashboard_pushButton_2.clicked.connect(self.open_train_data_page)
        self.dashboard_pushButton_3.clicked.connect(self.open_photo_page)
        self.dashboard_pushButton_4.clicked.connect(self.open_recognize_face_page)
        self.dashboard_pushButton_5.clicked.connect(self.open_notify_guardian_page)
        self.dashboard_pushButton_6.clicked.connect(self.open_attendance_report_page)
        self.dashboard_pushButton_9.clicked.connect(self.open_attendance_info_page)
        self.logout_button.clicked.connect(self.logout)

        self.button_list = [self.dashboard_pushButton,  self.dashboard_pushButton_2, self.dashboard_pushButton_3,
                            self.dashboard_pushButton_4, self.dashboard_pushButton_5, self.dashboard_pushButton_6,
                            self.dashboard_pushButton_9]

        # Signals generated to open photo.
        self.photo_button.clicked.connect(self.open_photo)
        # Signals generated to train algorithm.
        self.train_pushbutton.clicked.connect(self.train_data)
        # Signals generated to recognize face
        self.recognize_face_button.clicked.connect(self.recognize_face)
        # Signals generated to send email
        self.send_mail_button.clicked.connect(self.send_mail)

        # Find the elements in the student info page.
        self.roll_no_line_edit = self.findChild(QLineEdit, 'roll_no_line_edit')
        self.full_name_line_edit = self.findChild(QLineEdit, 'full_name_line_edit')
        self.gender_combo_box = self.findChild(QComboBox, 'gender_combo_box')
        self.date_of_birth_date_edit = self.findChild(QDateEdit, 'date_of_birth_date_edit')
        self.email_line_edit = self.findChild(QLineEdit, 'email_line_edit')
        self.phone_line_edit = self.findChild(QLineEdit, 'phone_line_edit')
        self.address_line_edit = self.findChild(QLineEdit, 'address_line_edit')
        self.parent_email_line_edit = self.findChild(QLineEdit, 'parent_email_line_edit')
        self.department_combo_box = self.findChild(QComboBox, 'department_combo_box')
        self.year_combo_box = self.findChild(QComboBox, 'year_combo_box')
        self.semester_combo_box = self.findChild(QComboBox, 'semester_combo_box')
        self.take_photo_button = self.findChild(QPushButton, 'take_photo_button')
        self.save_button = self.findChild(QPushButton, 'save_button')
        self.update_button = self.findChild(QPushButton, 'update_button')
        self.delete_button = self.findChild(QPushButton, 'delete_button')
        self.reset_button = self.findChild(QPushButton, 'reset_button')
        self.database_table = self.findChild(QTableWidget, 'database_table')
        self.search_line_edit = self.findChild(QLineEdit, 'search_line_edit')
        self.search_by_combo_box = self.findChild(QComboBox, 'search_by_combo_box')
        self.search_button = self.findChild(QPushButton, 'search_button')
        self.refresh_button = self.findChild(QPushButton, 'refresh_button')

        # validation of student_info form
        self.roll_no_line_edit.setValidator(QIntValidator())
        self.phone_line_edit.setValidator(QIntValidator())
        # Find the elements in train algo page:
        self.train_department_combo_box = self.findChild(QComboBox, 'train_department_combo_box')
        self.train_year_combo_box = self.findChild(QComboBox, 'train_year_combo_box')
        self.train_semester_combo_box = self.findChild(QComboBox, 'train_semester_combo_box')

        # Find the elements in open photo page:
        self.photo_department_combo_box = self.findChild(QComboBox, 'photo_department_combo_box')
        self.photo_year_combo_box = self.findChild(QComboBox, 'photo_year_combo_box')
        self.photo_semester_combo_box = self.findChild(QComboBox, 'photo_semester_combo_box')

        # Find the elements in recognize page:
        self.recognize_department_combo_box = self.findChild(QComboBox, 'recognize_department_combo_box')
        self.recognize_year_combo_box = self.findChild(QComboBox, 'recognize_year_combo_box')
        self.recognize_semester_combo_box = self.findChild(QComboBox, 'recognize_semester_combo_box')
        self.recognize_date_value = self.findChild(QLabel, 'recognize_date_value')
        self.recognize_date_edit = self.findChild(QDateEdit, 'recognize_date_edit')
        self.recognize_change_date_button = self.findChild(QPushButton, 'recognize_change_date_button')
        self.recognize_course_combo_box = self.findChild(QComboBox, 'recognize_course_combo_box')
        self.recognize_show_course_button = self.findChild(QPushButton, 'recognize_show_course_button')

        # Find the elements in attendance info:
        self.attendance_table = self.findChild(QTableWidget, 'attendance_table')
        self.attendance_info_save_all_button = self.findChild(QPushButton, 'attendance_info_save_all_button')
        self.attendance_info_search_line_edit = self.findChild(QLineEdit, 'attendance_info_search_line_edit')
        self.attendance_info_roll_number_radio_box = self.findChild(QRadioButton,
                                                                    'attendance_info_roll_number_radio_box')
        self.attendance_info_full_name_radio_box = self.findChild(QRadioButton, 'attendance_info_full_name_radio_box')
        self.attendance_info_status_radio_box = self.findChild(QRadioButton, 'attendance_info_status_radio_box')
        self.attendance_info_course_radio_box = self.findChild(QRadioButton, 'attendance_info_course_radio_box')
        self.attendance_info_search_button = self.findChild(QPushButton, 'attendance_info_search_button')

        self.attendance_info_department_combo_box = self.findChild(QComboBox, 'attendance_info_department_combo_box')
        self.attendance_info_year_combo_box = self.findChild(QComboBox, 'attendance_info_year_combo_box')
        self.attendance_info_semester_combo_box = self.findChild(QComboBox, 'attendance_info_semester_combo_box')
        self.attendance_info_course_combo_box = self.findChild(QComboBox, 'attendance_info_course_combo_box')
        self.attendance_info_export_button = self.findChild(QPushButton, 'attendance_info_export_button')
        self.attendance_info_show_courses_button = self.findChild(QPushButton, 'attendance_info_show_courses_button')

        # Find the elements in notify parent page:
        self.notify_table = self.findChild(QTableWidget, 'notify_table')
        self.notify_guardian_roll_no_radio_button = self.findChild(QRadioButton, 'notify_guardian_roll_no_radio_button')
        self.notify_guardian_full_name_radio_button = self.findChild(QRadioButton,
                                                                     'notify_guardian_full_name_radio_button')
        self.notify_guardian_search_button = self.findChild(QPushButton, 'notify_guardian_search_button')

        # Find the elements in attendance report page:
        self.attendance_report_bar_button = self.findChild(QPushButton, 'attendance_report_bar_button')
        self.attendance_report_pie_button = self.findChild(QPushButton, 'attendance_report_pie_button')
        self.attendance_report_department_combo_box = self.findChild(QComboBox, 'attendance_report_department_combo_box')
        self.attendance_report_year_combo_box = self.findChild(QComboBox, 'attendance_report_year_combo_box')
        self.attendance_report_semester_combo_box = self.findChild(QComboBox, 'attendance_report_semester_combo_box')
        self.attendance_report_course_combo_box = self.findChild(QComboBox, 'attendance_report_course_combo_box')
        self.attendance_report_show_courses_button = self.findChild(QPushButton, 'attendance_report_show_courses_button')

        # Signals generated in student info page
        self.save_button.clicked.connect(self.save_info)
        self.update_button.clicked.connect(self.update_info)
        self.delete_button.clicked.connect(self.delete_info)
        self.reset_button.clicked.connect(self.reset_info)
        self.take_photo_button.clicked.connect(self.take_photo)
        self.database_table.cellClicked.connect(self.cell_was_clicked)
        self.search_button.clicked.connect(self.search_info)
        self.refresh_button.clicked.connect(self.refresh_info)

        # signals generated in recognize page
        self.recognize_change_date_button.clicked.connect(self.attendance_change_date)
        self.recognize_show_course_button.clicked.connect(self.show_courses)

        # signals generated in notify guardian page
        self.notify_table.cellClicked.connect(self.notify_table_cell_clicked)
        self.notify_guardian_search_button.clicked.connect(self.search_notify)

        # signal generated in attendance info page
        self.attendance_info_save_all_button.clicked.connect(self.save_all_info)
        self.attendance_info_search_button.clicked.connect(self.search_attendance)
        self.attendance_info_export_button.clicked.connect(self.export_attendance)
        self.attendance_info_show_courses_button.clicked.connect(self.show_courses_attendance)

        # signal generated in attendance report page
        self.attendance_report_show_courses_button.clicked.connect(self.show_courses_report)
        self.attendance_report_bar_button.clicked.connect(self.display_bar)
        self.attendance_report_pie_button.clicked.connect(self.display_pie)

        # Display table value on start up
        self.refresh_info()

        # Display today date on recognize page
        today_date = date.today().strftime("%Y-%m-%d")
        self.date_value = self.findChild(QLabel, 'recognize_date_value')
        self.date_value.setText(today_date)

        # Disable take photo button
        self.take_photo_button.setVisible(False)
        self.take_photo_button.setEnabled(False)

        # Disable course combo box
        self.recognize_course_combo_box.setEnabled(False)

        # Disable course combo box of attendance info
        self.attendance_info_course_combo_box.setEnabled(False)

        # Disable course combo box of attendance report
        self.attendance_report_course_combo_box.setEnabled(False)

        # Set background of student-info to green on startup
        self.button_not_clicked = """
        QPushButton
        {
            background-color: rgb(64, 66, 226);
            color: rgb(255, 255, 255);
        }
        QPushButton::hover
        {
            background-color: rgb(0, 170, 0);
        }"""
        self.button_clicked = """
        QPushButton
        {
            background-color: rgb(0, 170, 0);
            color: rgb(255, 255, 255);
        }"""
        self.dashboard_pushButton.setStyleSheet(self.button_clicked)

        # Check background color of button
    def check_background(self):
        for i in self.button_list:
            property_value = i.styleSheet()
            if property_value == self.button_clicked:
                i.setStyleSheet(self.button_not_clicked)

    # Student info page functions:

    def open_student_info_page(self):
        self.check_background()
        self.dashboard_pushButton.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_student_info_page)

    def save_info(self):
        roll_no = self.roll_no_line_edit.text()
        full_name = self.full_name_line_edit.text()
        gender = self.gender_combo_box.currentText()
        dob = self.date_of_birth_date_edit.date().toPyDate()
        email = self.email_line_edit.text()
        phone = self.phone_line_edit.text()
        address = self.address_line_edit.text()
        parent_email = self.parent_email_line_edit.text()
        department = self.department_combo_box.currentText()
        year = self.year_combo_box.currentText()
        semester = self.semester_combo_box.currentText()
        if roll_no and full_name and email and phone and address and parent_email and gender and department and year \
                and semester:
            insert_values = [roll_no, full_name.title(), gender, dob, email, phone, address.title(), parent_email,
                             department, year, semester]
            is_complete = database_connection_test.insert_data(insert_values)
            if is_complete == True:
                QMessageBox.information(self, self.messagebox_title,
                                        "Information has been added successfully!")
                self.take_photo_button.setVisible(True)
                self.take_photo_button.setEnabled(True)
                self.refresh_info()
            else:
                QMessageBox.critical(self, self.messagebox_title, str(is_complete))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please fill all the values")
        self.database_table.setEnabled(True)

    def update_info(self):
        roll_no = self.roll_no_line_edit.text()
        full_name = self.full_name_line_edit.text()
        gender = self.gender_combo_box.currentText()
        dob = self.date_of_birth_date_edit.date().toPyDate()
        email = self.email_line_edit.text()
        phone = self.phone_line_edit.text()
        address = self.address_line_edit.text()
        parent_email = self.parent_email_line_edit.text()
        department = self.department_combo_box.currentText()
        year = self.year_combo_box.currentText()
        semester = self.semester_combo_box.currentText()
        if roll_no and full_name and email and phone and address and parent_email and gender and department and year \
                and semester:
            try:
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT department_name, year, semester FROM student_table WHERE roll_no=%s" % roll_no
                cursor.execute(query)
                result = cursor.fetchall()
                prev_department = result[0][0]
                prev_year = str(result[0][1])
                prev_semester = str(result[0][2])
                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))
            update_values = [roll_no, full_name.title(), gender, dob, email, phone, address.title(), parent_email,
                             department, year, semester]
            is_complete = database_connection_test.update_data(update_values)
            if is_complete == True:
                fs_name = full_name.split(' ')
                f_name = '-'.join(fs_name)
                f_name_roll = f_name+"-"+roll_no
                prev_path = "images\\"+prev_department+"\\"+prev_year+"\\"+prev_semester+"\\"+f_name_roll
                new_path = "images\\"+department+"\\"+year+"\\"+semester+"\\"+f_name_roll
                if prev_path != new_path and os.path.exists(prev_path):
                    try:
                        shutil.move(prev_path, new_path)
                    except Exception as err:
                        QMessageBox.critical(self, self.messagebox_title, str(err))
                    QMessageBox.information(self, self.messagebox_title,
                                        "Information has been updated successfully!")
                    self.refresh_info()
                    self.reset_info()
            else:
                QMessageBox.critical(self, self.messagebox_title, str(is_complete))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please fill all the values")
        self.database_table.setEnabled(True)

    def delete_info(self):
        roll_no = self.roll_no_line_edit.text()
        department = self.department_combo_box.currentText()
        year = self.year_combo_box.currentText()
        semester = self.semester_combo_box.currentText()
        f_name = self.full_name_line_edit.text()
        f_split_name = f_name.split(' ')
        full_name = '-'.join(f_split_name)
        path = "images\\"+department+"\\"+year+"\\"+semester+"\\"+full_name+"-"+roll_no+"\\"
        if roll_no:
            ret = QMessageBox.warning(self, self.messagebox_title, "Are you sure you want to delete these data?",
                                      QMessageBox.Ok | QMessageBox.No)
            if ret == QMessageBox.Ok:
                is_complete = database_connection_test.delete_data(roll_no)
                if os.path.exists(path):
                    send2trash.send2trash(path)
                if is_complete == True:
                    QMessageBox.information(self, self.messagebox_title,
                                            "Information has been deleted successfully!")
                    self.refresh_info()
                    self.reset_info()
                else:
                    QMessageBox.critical(self, self.messagebox_title, str(is_complete))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select any one of the data")
        self.database_table.setEnabled(True)

    def reset_info(self):
        self.roll_no_line_edit.setText('')
        self.full_name_line_edit.setText('')
        self.gender_combo_box.setCurrentIndex(0)
        self.email_line_edit.setText('')
        self.phone_line_edit.setText('')
        self.address_line_edit.setText('')
        self.parent_email_line_edit.setText('')
        self.department_combo_box.setCurrentIndex(0)
        self.year_combo_box.setCurrentIndex(0)
        self.semester_combo_box.setCurrentIndex(0)
        self.search_line_edit.setText('')
        self.search_by_combo_box.setCurrentIndex(0)
        self.database_table.setEnabled(True)

    def take_photo(self):
        roll_no = self.roll_no_line_edit.text()
        full_name = self.full_name_line_edit.text()
        department = self.department_combo_box.currentText()
        year = self.year_combo_box.currentText()
        semester = self.semester_combo_box.currentText()
        if roll_no and full_name and department and year and semester:
            is_complete = generate_image.generate_photo(roll_no, full_name.title(), department, year, semester)
            if is_complete:
                QMessageBox.information(self, self.messagebox_title,
                                        "Sample photo taken successfully.")
                self.reset_info()
                self.take_photo_button.setEnabled(False)
                self.take_photo_button.setVisible(False)
            else:
                QMessageBox.critical(self, self.messagebox_title, str(is_complete))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please fill above information first.")

    def refresh_info(self):
        try:
            self.database_table.setRowCount(0)
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            query = "SELECT * FROM student_table"
            cursor.execute(query)
            result = cursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.database_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.database_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as err:
            QMessageBox.critical(self, self.messagebox_title, str(err))

    def cell_was_clicked(self, row):
        values = []
        for i in range(11):
            item = self.database_table.item(row, i)
            values.append(item.text())

        # Setting the values of line edit after cell of table is clicked.
        self.roll_no_line_edit.setText(values[0])
        self.full_name_line_edit.setText(values[1])
        index = self.gender_combo_box.findText(values[2])
        if index >= 0:
            self.gender_combo_box.setCurrentIndex(index)
        date = [int(i) for i in values[3].split('-')]
        self.date_of_birth_date_edit.setDate(QDate(date[0], date[1], date[2]))
        self.email_line_edit.setText(values[4])
        self.phone_line_edit.setText(values[5])
        self.address_line_edit.setText(values[6])
        self.parent_email_line_edit.setText(values[7])
        index = self.department_combo_box.findText(values[8])
        if index >= 0:
            self.department_combo_box.setCurrentIndex(index)
        index = self.year_combo_box.findText(values[9])
        if index >= 0:
            self.year_combo_box.setCurrentIndex(index)
        index = self.semester_combo_box.findText(values[10])
        if index >= 0:
            self.semester_combo_box.setCurrentIndex(index)
        self.database_table.setEnabled(False)

    def search_info(self):
        search = '%'+self.search_line_edit.text()+'%'
        search_by = self.search_by_combo_box.currentText()
        if search_by and search:
            try:
                self.database_table.setRowCount(0);
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT * FROM student_table WHERE %s LIKE '%s'" % (search_by, search)
                cursor.execute(query)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.database_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.database_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please fill all the fields.")

    # Train Data page functions:

    def open_train_data_page(self):
        self.check_background()
        self.dashboard_pushButton_2.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_train_data_page)

    def train_data(self):
        try:
            train_department = self.train_department_combo_box.currentText()
            train_year = self.train_year_combo_box.currentText()
            train_semester = self.train_semester_combo_box.currentText()
            if train_department and train_year and train_semester:
                test_path = 'images\\' + train_department + '\\' + train_year + '\\' + train_semester
                if os.path.exists(test_path):
                    if len(os.listdir(test_path)) != 0:
                        try:
                            train = train_algo.TrainAlgo()
                            train.perform_training(train_department, train_year, train_semester)
                            QMessageBox.information(self, self.messagebox_title,
                                                    "Algorithm Trained. Proceed to Recognize Face!")
                        except Exception as e:
                            QMessageBox.critical(self, self.messagebox_title, str(e))
                    else:
                        QMessageBox.critical(self, self.messagebox_title,
                                             "No images found to train")
                else:
                    QMessageBox.critical(self, self.messagebox_title,
                                            "No images found to train")
            else:
                QMessageBox.critical(self, self.messagebox_title, "Fill all the fields")
        except Exception as err:
            print(err)

    # open image page functions:
    def open_photo_page(self):
        self.check_background()
        self.dashboard_pushButton_3.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_photo_page)

    def open_photo(self):
        photo_department = self.photo_department_combo_box.currentText()
        photo_year = self.photo_year_combo_box.currentText()
        photo_semester = self.photo_semester_combo_box.currentText()
        student_name = self.search_text.text().title()
        if photo_department and photo_year and photo_semester:
            path = 'images\\' + photo_department + '\\' + photo_year + '\\' + photo_semester + '\\' + student_name
            if os.path.exists(path):
                if len(os.listdir(path)) != 0:
                    webbrowser.open(path)
                else:
                    QMessageBox.critical(self, self.messagebox_title, "No Students Found!")
            else:
                QMessageBox.critical(self, self.messagebox_title, "No Students Found!")
        else:
            QMessageBox.critical(self, self.messagebox_title, "Fill all the fields")

    # Recognize page functions:
    def open_recognize_face_page(self):
        self.check_background()
        self.dashboard_pushButton_4.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_recognize_face_page)

    def recognize_face(self):
        date = self.date_value.text()
        course = self.recognize_course_combo_box.currentText()
        recognize_department = self.recognize_department_combo_box.currentText()
        recognize_year = self.recognize_year_combo_box.currentText()
        recognize_semester = self.recognize_semester_combo_box.currentText()
        if recognize_department and recognize_year and recognize_semester and course:
            required_path = 'yml//' + recognize_department + '\\' + recognize_year + '\\' + recognize_semester
            if os.path.exists(required_path):
                try:
                    recognize = recognize_face.RecognizeFace(recognize_department, recognize_year, recognize_semester)
                    recognize.get_name_list()
                    id_no, name = recognize.perform_face_recognition()
                    if id_no == 'NULL' or name == 'Unknown':
                        QMessageBox.critical(self, self.messagebox_title, "Sorry please try again.")
                    else:
                        message_confirm = QMessageBox.question(self, self.messagebox_title, "Name: %s\nRoll: %s" %
                                                               (name, id_no), QMessageBox.Yes | QMessageBox.No)
                        if message_confirm == QMessageBox.Yes:
                            handle_duplicate = database_connection_test.add_attendance(id_no, course, date)
                            if type(handle_duplicate) == ms.errors.IntegrityError:
                                QMessageBox.information(self, self.messagebox_title, "Looks like your attendance is "
                                                                                     "already taken.")
                            else:
                                QMessageBox.information(self, self.messagebox_title, "Your attendance is taken "
                                                                                     "successfully.")
                        else:
                            QMessageBox.critical(self, self.messagebox_title, "Sorry please try again.")
                except Exception as e:
                    QMessageBox.critical(self, self.messagebox_title, str(e))
            else:
                QMessageBox.critical(self, self.messagebox_title, "Sorry, no trained files found")
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select the required fields.")
        self.recognize_course_combo_box.setEnabled(False)

    def attendance_change_date(self):
        change_date = str(self.recognize_date_edit.date().toPyDate())
        try:
            self.date_value.setText(change_date)
        except Exception as err:
            QMessageBox.critical(self, self.messagebox_title, str(err))

    def show_courses(self):
        recognize_department = self.recognize_department_combo_box.currentText()
        recognize_year = self.recognize_year_combo_box.currentText()
        recognize_semester = self.recognize_semester_combo_box.currentText()
        values_list = [recognize_department, recognize_year, recognize_semester]
        if recognize_department and recognize_year and recognize_semester:
            self.recognize_course_combo_box.setEnabled(True)
            values = database_connection_test.get_course(values_list)
            if type(values) != ms.errors.InterfaceError:
                self.recognize_course_combo_box.clear()
                for course in values:
                    self.recognize_course_combo_box.addItem(course[0])
            else:
                QMessageBox.critical(self, self.messagebox_title, str(values))

        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select Department, year and "\
                                                                 "semester field first.")

    # Notify Guardian Page functions:
    def open_notify_guardian_page(self):
        self.check_background()
        self.dashboard_pushButton_5.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_notify_guardian_page)
        try:
            self.notify_table.setRowCount(0);
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            # query = "SELECT roll_no, full_name, course, attendance_date, attendance_status" \
            #         " FROM attendance_view WHERE attendance_date=CURDATE() AND attendance_status='A'"
            query = "SELECT roll_no, full_name, course, attendance_date, attendance_status" \
                    " FROM attendance_final_view WHERE attendance_status='A'"
            cursor.execute(query)
            result = cursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.notify_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.notify_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as err:
            QMessageBox.critical(self, self.messagebox_title, str(err))

    def send_mail(self):
        try:
            receiver_email = self.to_line_edit.text()
            subject = self.subject_line_edit.text()
            main_body = self.mail_content_edit.toPlainText()
            is_empty = False
            if receiver_email == '' and subject == '' and main_body == '':
                QMessageBox.critical(self, self.messagebox_title, "Please enter value for all fields")
                is_empty = True

            if not is_empty:
                send = smtp_email.SendEmail(receiver_email, subject, main_body)
                value = send.send_email()
                if value == True:
                    QMessageBox.information(self, 'Face Recognition Attendance System',
                                            'The mail has been sent successfully!')
                    self.to_line_edit.setText('')
                    self.subject_line_edit.setText('')
                    self.mail_content_edit.setPlainText('')
                else:
                    QMessageBox.critical(self, self.messagebox_title, str(value))
        except Exception as e:
            QMessageBox.critical(self, self.messagebox_title, str(e))

    def notify_table_cell_clicked(self, row):
        # Change number value with number of columns.
        item = self.notify_table.item(row, 0)
        value = item.text()
        try:
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            query = "SELECT parent_email FROM student_table WHERE roll_no = %s" % value
            cursor.execute(query)
            result = cursor.fetchall()
            self.to_line_edit.setText(result[0][0])
        except Exception as err:
            QMessageBox.critical(self, self.messagebox_title, str(err))

    def search_notify(self):
        search_value = '%' + self.notify_guardian_search_line_edit.text() + '%'
        selected_radio = ''
        if self.notify_guardian_roll_no_radio_button.isChecked():
            selected_radio = 'roll_no'
        elif self.notify_guardian_full_name_radio_button.isChecked():
            selected_radio = 'full_name'
        if selected_radio == '':
            QMessageBox.critical(self, self.messagebox_title, "Please select one of the radio boxes.")
        else:
            try:
                self.notify_table.setRowCount(0)
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT roll_no, full_name, course, attendance_date, attendance_status" \
                        " FROM attendance_final_view WHERE attendance_status='A' AND %s LIKE '%s'" % \
                        (selected_radio, search_value)
                cursor.execute(query)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.notify_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.notify_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))

    # Attendance Report page functions:
    def open_attendance_report_page(self):
        self.check_background()
        self.dashboard_pushButton_6.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_attendance_report_page)

    def show_courses_report(self):
        report_department = self.attendance_report_department_combo_box.currentText()
        report_year = self.attendance_report_year_combo_box.currentText()
        report_semester = self.attendance_report_semester_combo_box.currentText()
        values_list = [report_department, report_year, report_semester]
        if report_department and report_year and report_semester:
            self.attendance_report_course_combo_box.setEnabled(True)
            values = database_connection_test.get_course(values_list)
            if type(values) != ms.errors.InterfaceError:
                self.attendance_report_course_combo_box.clear()
                for course in values:
                    self.attendance_report_course_combo_box.addItem(course[0])
            else:
                QMessageBox.critical(self, self.messagebox_title, str(values))

        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select Department, year and " \
                                                              "semester field first.")

    def display_bar(self):
        width = 0.2
        x = ['CE', 'Civil', 'IT', 'Software']
        y = [1, 2, 3, 4]
        # count_d = []
        count_d = [[40, 70, 50, 20], [20, 60, 70, 90], [60, 20, 40, 50], [70, 50, 90, 30]]
        # try:
        #     conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        #     cursor = conn.cursor()
        #     for i in x:
        #         count = []
        #         for j in y:
        #             query = "SELECT COUNT(roll_no) FROM attendance_final_view WHERE department_name='%s' AND YEAR='%s'" \
        #                     "AND attendance_status = 'P'" % (i, j)
        #             cursor.execute(query)
        #             result = cursor.fetchall()
        #             count.append(result[0][0])
        #         count_d.append(count)
        #     print(count_d)
        #     conn.close()
        # except Exception as err:
        #     QMessageBox.critical(self, self.messagebox_title, str(err))
        ce_count, civil_count, it_count, software_count = count_d
        bar1 = [i for i in range(len(x))]
        bar2 = [i+width for i in bar1]
        bar3 = [i+width for i in bar2]
        bar4 = [i+width for i in bar3]
        plt.bar(bar1, ce_count, width, label="year-1")
        plt.bar(bar2, civil_count, width, label="year-2")
        plt.bar(bar3, it_count, width, label="year-3")
        plt.bar(bar4, software_count, width, label="year-4")

        tick_distance = [i+0.3 for i in bar1]
        plt.xticks(tick_distance, x)
        plt.legend(bbox_to_anchor=[1, 1], loc='upper left')
        plt.xlabel("Department")
        plt.ylabel("Present Students")
        plt.title("Present Students vs Department based on year")
        plt.show()

    def display_pie(self):
        report_course = self.attendance_report_course_combo_box.currentText()
        report_department = self.attendance_report_department_combo_box.currentText()
        report_year = self.attendance_report_year_combo_box.currentText()
        report_semester = self.attendance_report_semester_combo_box.currentText()
        if report_department and report_year and report_semester and report_course:
            try:
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT COUNT(roll_no) FROM attendance_final_view WHERE department_name = '%s' AND year = '%s'" \
                        " AND semester = '%s' AND course = '%s' AND attendance_status = 'P'" \
                        % (report_department, report_year, report_semester, report_course)
                cursor.execute(query)
                result = cursor.fetchall()
                present_count = result[0][0]
                query = "SELECT COUNT(roll_no) FROM attendance_final_view WHERE department_name = '%s' AND year = '%s'" \
                        " AND semester = '%s' AND course = '%s' AND attendance_status = 'A'" \
                        % (report_department, report_year, report_semester, report_course)
                cursor.execute(query)
                result = cursor.fetchall()
                absent_count = result[0][0]
                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))
            try:
                label = ['present', 'absent']
                # value = [present_count, absent_count]
                value = [30, 5]
                plt.pie(value, labels=label, explode=[0.2, 0], autopct='%.1f%%', shadow=True)
                plt.show()
            except Exception as err:
                print(err)
                QMessageBox.critical(self, self.messagebox_title, str(err))
        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select the required fields.")
        self.attendance_report_course_combo_box.setEnabled(False)

    # Attendance Info page functions:
    def open_attendance_info_page(self):
        self.check_background()
        self.dashboard_pushButton_9.setStyleSheet(self.button_clicked)
        self.stack_pages.setCurrentWidget(self.stack_pages_attendance_info_page)
        try:
            date_value = self.recognize_date_value.text()
            self.attendance_table.setRowCount(0)
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            query = "CREATE OR REPLACE VIEW attendance_final_view AS "\
                    "SELECT st.roll_no, st.full_name, st.department_name, st.year, st.semester, dt.course, "\
                    "IFNULL(at.attendance_date,'%s') AS attendance_date, IFNULL(at.attendance_status,'A') "\
                    "AS attendance_status "\
                    "FROM student_table AS st "\
                    "INNER JOIN department_table AS dt "\
                    "ON st.department_name = dt.department_name AND "\
                    "st.year = dt.year AND st.semester = dt.semester "\
                    "LEFT JOIN attendance_table AS at "\
                    "ON st.roll_no = at.roll_no AND dt.course = at.course" % date_value
            cursor.execute(query)
            conn.commit()
            query = "SELECT * FROM attendance_final_view"
            cursor.execute(query)
            result = cursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.attendance_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.attendance_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as err:
            QMessageBox.critical(self, self.messagebox_title, str(err))

    def save_all_info(self):
        ret = QMessageBox.warning(self, self.messagebox_title, "Are you sure you want to save all these data? You will "
                                                               "not be able to take any attendance afterwards.",
                                  QMessageBox.Ok | QMessageBox.No)
        if ret == QMessageBox.Ok:
                # Getting all values from view
            try:
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT * FROM attendance_final_view"
                cursor.execute(query)
                result = cursor.fetchall()

                # Adding datas of view to the attendance complete table
                handle_duplicate = database_connection_test.save_to_complete_table(result)
                if type(handle_duplicate) == ms.errors.IntegrityError:
                    QMessageBox.information(self, self.messagebox_title, "Looks like data is already saved.")
                else:
                    QMessageBox.information(self, self.messagebox_title, "saved  "
                                                                         "successfully.")
                    # Droping view
                    query = "DROP VIEW attendance_final_view"
                    cursor.execute(query)
                    conn.commit()

                    # Removing data from attendance table
                    query = "TRUNCATE TABLE attendance_table"
                    cursor.execute(query)
                    conn.commit()

                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))

    def search_attendance(self):
        search_value = '%'+self.attendance_info_search_line_edit.text()+'%'
        selected_radio = ''
        if self.attendance_info_roll_number_radio_box.isChecked():
            selected_radio = 'roll_no'
        elif self.attendance_info_full_name_radio_box.isChecked():
            selected_radio = 'full_name'
        elif self.attendance_info_status_radio_box.isChecked():
            selected_radio = 'attendance_status'
        elif self.attendance_info_course_radio_box.isChecked():
            selected_radio = 'course'
        if selected_radio == '':
            QMessageBox.critical(self, self.messagebox_title, "Please select one of the radio boxes.")
        else:
            try:
                self.attendance_table.setRowCount(0);
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT * FROM attendance_final_view WHERE %s LIKE '%s'" % (selected_radio, search_value)
                cursor.execute(query)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.attendance_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.attendance_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                conn.close()
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))

    def show_courses_attendance(self):
        attendance_department = self.attendance_info_department_combo_box.currentText()
        attendance_year = self.attendance_info_year_combo_box.currentText()
        attendance_semester = self.attendance_info_semester_combo_box.currentText()
        values_list = [attendance_department, attendance_year, attendance_semester]
        if attendance_department and attendance_year and attendance_semester:
            self.attendance_info_course_combo_box.setEnabled(True)
            values = database_connection_test.get_course(values_list)
            if type(values) != ms.errors.InterfaceError:
                self.attendance_info_course_combo_box.clear()
                for course in values:
                    self.attendance_info_course_combo_box.addItem(course[0])
            else:
                QMessageBox.critical(self, self.messagebox_title, str(values))

        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select Department, year and " \
                                                                 "semester field first.")

    def export_attendance(self):
        date_value = self.recognize_date_value.text()
        attendance_course = self.attendance_info_course_combo_box.currentText()
        attendance_department = self.attendance_info_department_combo_box.currentText()
        attendance_year = self.attendance_info_year_combo_box.currentText()
        attendance_semester = self.attendance_info_semester_combo_box.currentText()
        if attendance_department and attendance_year and attendance_semester and attendance_course:
            excel_path = 'excel\\'+attendance_department+'\\'+attendance_year+'\\'+attendance_semester+'\\'+\
                         attendance_course+'\\'
            if not os.path.exists(excel_path):
                os.makedirs(excel_path)

            # Getting data from view
            try:
                conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
                cursor = conn.cursor()
                query = "SELECT * FROM attendance_final_view WHERE department_name = '%s' AND year = '%s' AND " \
                        "semester = '%s' AND course = '%s'" % (attendance_department, attendance_year,
                                                                attendance_semester, attendance_course)
                cursor.execute(query)
                result = cursor.fetchall()
                conn.close()

                # Export as xml file
                dest_file = excel_path + date_value + '.xlsx'
                work_book = Workbook()
                work_sheet = work_book.active
                # heading
                heading_list = ['Roll No', 'Full Name', 'Department Name', 'Year', 'Semester', 'Course', 'Date',
                                'Status']
                work_sheet.append(heading_list)
                for row in result:
                    work_sheet.append(row)
                work_book.save(dest_file)
                QMessageBox.information(self, self.messagebox_title, "Exported Successfully.")
            except Exception as err:
                QMessageBox.critical(self, self.messagebox_title, str(err))

        else:
            QMessageBox.critical(self, self.messagebox_title, "Please select the required fields.")
        self.attendance_info_course_combo_box.setEnabled(False)

    # Logout
    def logout(self):
        login_window = LoginForm()
        stacked_widget.addWidget(login_window)
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex()+1)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dashboard_window = DashboardForm()
#     dashboard_window.show()
#     sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    login_window = LoginForm()
    stacked_widget.addWidget(login_window)
    stacked_widget.setStyleSheet("background-color: rgb(220, 228, 254)")
    stacked_widget.setWindowTitle("FRAS")
    stacked_widget.setWindowIcon(QtGui.QIcon("face_recognition_icon.jpg"))
    stacked_widget.setFixedWidth(1360)
    stacked_widget.setFixedHeight(760)
    stacked_widget.show()
    sys.exit(app.exec_())
