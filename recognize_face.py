import os
import cv2


# ---------------------------Recognize face----------------------------------------------------
class RecognizeFace:
    def __init__(self):
        self.cascade_path = 'C:\\Users\\LENOVO\\PycharmProjects\\face_recognition_demo\\venv\\' \
                             'Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml'
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("yml/trainingdata.yml")
        self.camera = cv2.VideoCapture(0)
        self.path = 'images//'
        self.names = []

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
                    text1 = '%s %d' % (self.names[id_no], id_no)
                    text2 = 'confidence=%d' % conf
                    if conf >= 77:
                        cv2.putText(frame, text1, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        cv2.putText(frame, text2, (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    else:
                        text = 'unknown image'
                        cv2.putText(frame, text, (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Recognition', frame)
        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    recognize = RecognizeFace()
    recognize.get_name_list()
    recognize.perform_face_recognition()