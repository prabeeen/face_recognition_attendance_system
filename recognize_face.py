import os
import cv2


# ---------------------------Recognize face----------------------------------------------------
class RecognizeFace:
    def __init__(self, department, year, semester):
        self.cascade_path = 'C:\\Users\\LENOVO\\PycharmProjects\\face_recognition_demo\\venv\\' \
                             'Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml'
        self.department = department
        self.year = year
        self.semester = semester
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.train_data_path = 'yml//'+self.department+'\\'+self.year+'\\'+self.semester+'\\'
        self.recognizer.read(self.train_data_path+"trainingdata.yml")
        self.camera = cv2.VideoCapture(0)
        self.path = 'images//'+self.department+'\\'+self.year+'\\'+self.semester+'\\'
        self.names = []
        self.detected_name = ''
        self.id_to_return = 0
        self.name_to_return = ''

    def get_name_list(self):
        for directories, subdirectories, filenames in os.walk(self.path):
            for subdirectory in subdirectories:
                self.names.append(subdirectory)

    def perform_face_recognition(self):
        while cv2.waitKey(1) == -1:
            success, frame = self.camera.read()
            if success:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 2)
                    id_no, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])
                    conf = int((100 * (1 - confidence / 300)))
                    # text1 = '%s' % (name[id_no - 1].split('_')[-1])

                    for i in self.names:
                        if int(i.split('-')[-1]) == id_no:
                            n_list = i.split('-')[:-1]
                            self.detected_name = ' '.join(n_list)

                    text1 = '%s %d' % (self.detected_name, id_no)
                    text2 = 'confidence=%d' % conf
                    if conf >= 77:
                        cv2.putText(frame, text1, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        cv2.putText(frame, text2, (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        self.id_to_return = id_no
                        self.name_to_return = self.detected_name
                        self.camera.release()
                        cv2.destroyAllWindows()
                        return self.id_to_return, self.name_to_return
                    else:
                        text = 'unknown image'
                        cv2.putText(frame, text, (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                        self.id_to_return = 'NULL'
                        self.name_to_return = 'Unknown'
                cv2.imshow('Face Recognition', frame)
        self.camera.release()
        cv2.destroyAllWindows()
        return self.id_to_return, self.name_to_return


if __name__ == '__main__':
    recognize = RecognizeFace()
    recognize.get_name_list()
    recognize.perform_face_recognition()