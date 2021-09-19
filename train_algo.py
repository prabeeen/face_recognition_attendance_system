import os
import cv2
import numpy as np
from PIL import Image


class TrainAlgo:
    def __init__(self):
        self.names = []
        self.faces_list = []
        self.id_nos = []
        self.id_no = 0
        self.path = "images//"
        self.ids, self.face, self.name = [], [], []

    def train_algorithm(self, department_name, year, sem):
        self.path = self.path + department_name + '\\' + year + '\\' + sem + '\\'
        for directories, subdirectories, filenames in os.walk(self.path):
            for subdirectory in subdirectories:
                self.names.append(subdirectory)
                subject_path = os.path.join(directories, subdirectory)
                image_paths = [os.path.join(subject_path, f) for f in os.listdir(subject_path)]

                for image_path in image_paths:
                    face_img = Image.open(image_path).convert("L")
                    face_np = np.array(face_img, "uint8")
                    self.id_no = int(os.path.split(image_path)[-1].split("_")[1])
                    self.faces_list.append(face_np)
                    self.id_nos.append(self.id_no)
                    cv2.imshow("Training.....", face_np)
                    cv2.waitKey(2)
                # self.id_no += 1
        return self.id_nos, self.faces_list, self.names

    def perform_training(self, department_name, year, sem):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.ids, self.face, self.name = self.train_algorithm(department_name, year, sem)
        cv2.destroyAllWindows()
        recognizer.train(self.face, np.array(self.ids))
        save_path = 'yml\\' + department_name + '\\' + year + '\\' + sem
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        recognizer.save(save_path+'\\'+'trainingdata.yml')


if __name__ == '__main__':
    train = TrainAlgo()
    train.perform_training()
