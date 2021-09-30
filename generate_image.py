import cv2
import os
cascade_path = 'venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)


def generate_photo(roll_no, full_name, department_name, year, sem):
    is_success = False
    full_name_list = full_name.split(' ')
    formatted_full_name = '-'.join(full_name_list)
    full_name_with_roll = formatted_full_name + '-' + roll_no
    # # print("Enter the name of the person to be scanned.")
    # # name = input()
    # Auto id assign.
    # id_to_be_assigned = len(os.listdir('images')) + 1
    # id_no = id_to_be_assigned
    # id_name_combined = str(id_no) + "_" + name
    # output_folder = 'images\\' + id_name_combined
    output_folder = 'images\\' + department_name + '\\' + year + '\\' + sem + '\\' + full_name_with_roll# Remove later
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Capture video.
    try:
        camera = cv2.VideoCapture(0)
        count = 0
        while count < 100 and cv2.waitKey(1) == -1:
            success, frame = camera.read()
            if success:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
                for x, y, w, h in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    face_img = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
                    # face_filename = os.path.join(output_folder, '%s_%d_%d.png' % (name, id_no, count))
                    face_filename = os.path.join(output_folder, '%s_%s_%d.png' % (full_name, roll_no, count))
                    cv2.imwrite(face_filename, face_img)
                    count += 1
                cv2.imshow('Face Detection and Capturing...', frame)
        camera.release()
        cv2.destroyAllWindows()
        is_success = True
        return is_success
    except Exception as err:
        print('failed: '+err)
        return err





