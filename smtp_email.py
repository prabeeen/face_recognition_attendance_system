import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    def __init__(self, receiver_email, subject, main_body):
        self.smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        self.receiver_email = receiver_email
        self.subject = subject
        self.main_body = main_body
        self.msg = {}

    def send_email(self):
        self.smtp_obj.ehlo()
        self.smtp_obj.starttls()
        self.smtp_obj.login('facerecognition01@gmail.com', 'Facerecognition1')
        self.msg = MIMEMultipart()
        self.msg['From'] = "facerecognition01@gmail.com"
        self.msg['To'] = self.receiver_email
        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.main_body, 'plain'))
        self.smtp_obj.sendmail('facerecognition01@gmail.com', self.receiver_email, self.msg.as_string())
        self.smtp_obj.quit()


if __name__ == '__main__':
    send = SendEmail('kthmndunpl@gmail.com', 'test', 'HEL+LO WORLD')
    send.send_email()

