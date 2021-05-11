from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QTextEdit

from PyQt5 import uic
import sys
import webbrowser
import os
import train_algo
import recognize_face
import smtp_email


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
        # Get the buttons in stackWidget
        self.dashboard_pushButton = self.findChild(QPushButton, 'pushButton')
        self.dashboard_pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.dashboard_pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.dashboard_pushButton_4 = self.findChild(QPushButton, 'pushButton_4')
        self.dashboard_pushButton_5 = self.findChild(QPushButton, 'pushButton_5')
        self.dashboard_pushButton_6 = self.findChild(QPushButton, 'pushButton_6')
        # Set the first page of Stack Widget.
        self.stack_pages.setCurrentWidget(self.stack_pages_student_info_page)
        # Signals generated in stack widget page.
        self.dashboard_pushButton.clicked.connect(self.open_student_info_page)
        self.dashboard_pushButton_2.clicked.connect(self.open_train_data_page)
        self.dashboard_pushButton_3.clicked.connect(self.open_photo_page)
        self.dashboard_pushButton_4.clicked.connect(self.open_recognize_face_page)
        self.dashboard_pushButton_5.clicked.connect(self.open_notify_guardian_page)
        self.dashboard_pushButton_6.clicked.connect(self.open_attendance_report_page)
        # Signals generated to open photo.
        self.photo_button.clicked.connect(self.open_photo)
        # Signals generated to train algorithm.
        self.train_pushbutton.clicked.connect(self.train_data)
        # Signals generated to recognize face
        self.recognize_face_button.clicked.connect(self.recognize_face)
        # Signals generated to send email
        self.send_mail_button.clicked.connect(self.send_mail)

    def open_student_info_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_student_info_page)

    def open_train_data_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_train_data_page)

    def train_data(self):
        try:
            train = train_algo.TrainAlgo()
            train.perform_training()
            QMessageBox.information(self, self.messagebox_title,
                                    "Algorithm Trained. Proceed to Recognize Face!")
        except Exception as e:
            print(f'{e}')

    def open_photo_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_photo_page)

    def open_photo(self):
        student_name = self.search_text.text()
        path = 'C:\\Users\\LENOVO\\PycharmProjects\\face_recognition_demo_final\\images\\' + student_name
        if os.path.exists(path):
            webbrowser.open(path)
        else:
            QMessageBox.warning(self, self.messagebox_title, "No Students Found!")

    def open_recognize_face_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_recognize_face_page)

    def recognize_face(self):
        try:
            recognize = recognize_face.RecognizeFace()
            recognize.get_name_list()
            recognize.perform_face_recognition()
        except Exception as e:
            print("error")
            print(f'{e}')

    def open_notify_guardian_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_notify_guardian_page)

    def send_mail(self):
        try:
            receiver_email = self.to_line_edit.text()
            subject = self.subject_line_edit.text()
            main_body = self.mail_content_edit.toPlainText()
            is_empty = False
            if receiver_email == '' or subject == '' or main_body == '':
                QMessageBox.warning(self, self.messagebox_title, "Please enter value for all fields")
                is_empty = True

            if not is_empty:
                send = smtp_email.SendEmail(receiver_email, subject, main_body)
                send.send_email()
                QMessageBox.information(self, 'Face Recognition Attendance System', 'The mail has been sent successfully!')
                self.to_line_edit.setText('')
                self.subject_line_edit.setText('')
                self.mail_content_edit.setPlainText('')
        except Exception as e:
            print("error")
            print(f'{e}')

    def open_attendance_report_page(self):
        self.stack_pages.setCurrentWidget(self.stack_pages_attendance_report_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard_window = DashboardForm()
    dashboard_window.show()
    sys.exit(app.exec_())
