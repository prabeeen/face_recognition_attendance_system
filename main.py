from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QTextEdit, \
    QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, QLabel
# For changing Pydate to Qdate
from PyQt5.QtCore import QDate

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

        # Find the elements in notify parent page:
        self.notify_table = self.findChild(QTableWidget, 'notify_table')

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

        # Display table value on start up
        self.refresh_info()

        # Display today date on recognize page
        today_date = date.today().strftime("%Y-%m-%d")
        self.date_value = self.findChild(QLabel, 'recognize_date_value')
        self.date_value.setText(today_date)

        # Disable course combo box
        self.recognize_course_combo_box.setEnabled(False)

    # Student info page functions:

    def open_student_info_page(self):
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
            if is_complete:
                QMessageBox.information(self, self.messagebox_title,
                                        "Information has been added successfully!")
                self.refresh_info()
                self.reset_info()
            else:
                QMessageBox.information(self, self.messagebox_title, "Please check your roll no value.")
        else:
            QMessageBox.information(self, self.messagebox_title, "Please fill all the values")
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
            update_values = [roll_no, full_name.title(), gender, dob, email, phone, address.title(), parent_email,
                             department, year, semester]
            is_complete = database_connection_test.update_data(update_values)
            if is_complete:
                QMessageBox.information(self, self.messagebox_title,
                                        "Information has been updated successfully!")
                self.refresh_info()
                self.reset_info()
            else:
                QMessageBox.information(self, self.messagebox_title, "Sorry! Please check the values properly")
        else:
            QMessageBox.information(self, self.messagebox_title, "Please fill all the values")
        self.database_table.setEnabled(True)

    def delete_info(self):
        roll_no = self.roll_no_line_edit.text()
        if roll_no:
            ret = QMessageBox.warning(self, self.messagebox_title, "Are you sure you want to delete these data?",
                                      QMessageBox.Ok | QMessageBox.No)
            if ret == QMessageBox.Ok:
                is_complete = database_connection_test.delete_data(roll_no)
                if is_complete:
                    QMessageBox.information(self, self.messagebox_title,
                                            "Information has been deleted successfully!")
                    self.refresh_info()
                    self.reset_info()
        else:
            QMessageBox.information(self, self.messagebox_title, "Please select any one of the data")
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
                                        "Sample photo taken successfully. Save the information")
            else:
                QMessageBox.information(self, self.messagebox_title, "Something went wrong.")
        else:
            QMessageBox.information(self, self.messagebox_title,
                                    "Please fill above information first.")

    def refresh_info(self):
        try:
            self.database_table.setRowCount(0);
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
            print(f"Error: {err}")

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
                print(f"Error: {err}")
        else:
            QMessageBox.information(self, self.messagebox_title, "Please fill all the fields.")

    # Train Data page functions:

    def open_train_data_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_train_data_page)

    def train_data(self):
        train_department = self.train_department_combo_box.currentText()
        train_year = self.train_year_combo_box.currentText()
        train_semester = self.train_semester_combo_box.currentText()
        if train_department and train_year and train_semester:
            test_path = 'images\\' + train_department + '\\' + train_year + '\\' + train_semester
            if os.path.exists(test_path):
                try:
                    train = train_algo.TrainAlgo()
                    train.perform_training(train_department, train_year, train_semester)
                    QMessageBox.information(self, self.messagebox_title,
                                            "Algorithm Trained. Proceed to Recognize Face!")
                except Exception as e:
                    print(f'{e}')
            else:
                QMessageBox.information(self, self.messagebox_title,
                                        "No images found to train")
        else:
            QMessageBox.information(self, self.messagebox_title, "Fill all the fields")

    # open image page functions:
    def open_photo_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_photo_page)

    def open_photo(self):
        photo_department = self.photo_department_combo_box.currentText()
        photo_year = self.photo_year_combo_box.currentText()
        photo_semester = self.photo_semester_combo_box.currentText()
        student_name = self.search_text.text().title()
        if photo_department and photo_year and photo_semester:
            path = 'C:\\Users\\LENOVO\\PycharmProjects\\face_recognition_ui\\images\\' \
                   + photo_department + '\\' + photo_year + '\\' + photo_semester + '\\' + student_name
            if os.path.exists(path):
                webbrowser.open(path)
            else:
                QMessageBox.warning(self, self.messagebox_title, "No Students Found!")
        else:
            QMessageBox.information(self, self.messagebox_title, "Fill all the fields")

    # Recognize page functions:
    def open_recognize_face_page(self):
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
                        QMessageBox.information(self, self.messagebox_title, "Sorry please try again.")
                    else:
                        message_confirm = QMessageBox.question(self, self.messagebox_title, "Name: %s\nRoll: %s" % (name,
                                                                id_no), QMessageBox.Yes | QMessageBox.No)
                        if message_confirm == QMessageBox.Yes:
                            database_connection_test.attendance_add(id_no, course, date)
                            QMessageBox.information(self, self.messagebox_title, "Your attendance is taken successfully.")
                        else:
                            QMessageBox.information(self, self.messagebox_title, "Sorry please try again.")

                except Exception as e:
                    print("error")
                    print(f'{e}')
            else:
                QMessageBox.information(self, self.messagebox_title, "Sorry, no trained files found")
        else:
            QMessageBox.information(self, self.messagebox_title, "Please select the required fields.")
        self.recognize_course_combo_box.setEnabled(False)

    def attendance_change_date(self):
        change_date = str(self.recognize_date_edit.date().toPyDate())
        try:
            self.date_value.setText(change_date)
        except Exception as err:
            print(err)

    def show_courses(self):
        recognize_department = self.recognize_department_combo_box.currentText()
        recognize_year = self.recognize_year_combo_box.currentText()
        recognize_semester = self.recognize_semester_combo_box.currentText()
        values_list = [recognize_department, recognize_year, recognize_semester]
        if recognize_department and recognize_year and recognize_semester:
            self.recognize_course_combo_box.setEnabled(True)
            is_complete, values = database_connection_test.get_course(values_list)
            if is_complete:
                self.recognize_course_combo_box.clear()
                for course in values:
                    self.recognize_course_combo_box.addItem(course[0])
            else:
                QMessageBox.information(self, self.messagebox_title, "Something Went Wrong")

        else:
            QMessageBox.information(self, self.messagebox_title, "Please select Department, year and "\
                                                                 "semester field first.")

    # Notify Guardian Page functions:
    def open_notify_guardian_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_notify_guardian_page)
        try:
            self.notify_table.setRowCount(0);
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            query = "SELECT roll_no, full_name, course, attendance_date, attendance_status" \
                    " FROM attendance_view WHERE attendance_date=CURDATE() AND attendance_status='A'"
            cursor.execute(query)
            result = cursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.notify_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.notify_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as err:
            print(f"Error: {err}")

    def send_mail(self):
        try:
            receiver_email = self.to_line_edit.text()
            subject = self.subject_line_edit.text()
            main_body = self.mail_content_edit.toPlainText()
            is_empty = False
            if receiver_email == '' and subject == '' and main_body == '':
                QMessageBox.warning(self, self.messagebox_title, "Please enter value for all fields")
                is_empty = True

            if not is_empty:
                send = smtp_email.SendEmail(receiver_email, subject, main_body)
                send.send_email()
                QMessageBox.information(self, 'Face Recognition Attendance System',
                                        'The mail has been sent successfully!')
                self.to_line_edit.setText('')
                self.subject_line_edit.setText('')
                self.mail_content_edit.setPlainText('')
        except Exception as e:
            print("error")
            print(f'{e}')

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
            print(result)
            self.to_line_edit.setText(result[0][0])
        except Exception as err:
            print(f"Error: {err}")


    # Attendance Report page functions:
    def open_attendance_report_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_attendance_report_page)

    # Attendance Info page functions:
    def open_attendance_info_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_attendance_info_page)
        try:
            self.attendance_table.setRowCount(0);
            conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
            cursor = conn.cursor()
            query = "CREATE VIEW attendance_final_view AS "\
                    "SELECT st.roll_no, st.full_name, st.department_name, st.year, st.semester, dt.course, "\
                    "IFNULL(at.attendance_date,CURDATE()) AS attendance_date, IFNULL(at.attendance_status,'A') "\
                    "AS attendance_status "\
                    "FROM student_table AS st "\
                    "INNER JOIN department_table AS dt "\
                    "ON st.department_name = dt.department_name AND "\
                    "st.year = dt.year AND st.semester = dt.semester "\
                    "LEFT JOIN attendance_table AS at "\
                    "ON st.roll_no = at.roll_no AND dt.course = at.course"
            # cursor.execute(query)
            # cursor.commit()
            query = "SELECT * FROM attendance_view"
            cursor.execute(query)
            result = cursor.fetchall()
            for row_number, row_data in enumerate(result):
                self.attendance_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.attendance_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception as err:
            print(f"Error: {err}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard_window = DashboardForm()
    dashboard_window.show()
    sys.exit(app.exec_())
