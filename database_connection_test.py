import mysql.connector as ms


def insert_data(values_list):
    is_success = False
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        query = "INSERT INTO student_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (values_list[0], values_list[1], values_list[2], values_list[3], values_list[4], values_list[5],
               values_list[6], values_list[7], values_list[8],  values_list[9], values_list[10])
        cursor.execute(query, val)
        conn.commit()
        conn.close()
        is_success = True
        return is_success
    except ms.Error as err:
        print(f'Error: {err}')
        conn.close()
        return is_success


def update_data(values_list):
    is_success = False
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        query = "UPDATE student_table SET roll_no=%s, full_name=%s, gender=%s, date_of_birth=%s, email=%s, phone=%s," \
                " address=%s, parent_email=%s, department_name=%s, year=%s, semester=%s WHERE roll_no=%s"
        val = (values_list[0], values_list[1], values_list[2], values_list[3], values_list[4], values_list[5],
               values_list[6], values_list[7], values_list[8],  values_list[9], values_list[10], values_list[0])
        cursor.execute(query, val)
        conn.commit()
        conn.close()
        is_success = True
        return is_success
    except ms.Error as err:
        print(f'Error: {err}')
        conn.close()
        return is_success


def delete_data(roll):
    is_success = False
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        query = "DELETE FROM student_table WHERE roll_no="+roll
        cursor.execute(query)
        conn.commit()
        conn.close()
        is_success = True
        return is_success
    except ms.Error as err:
        print(f'Error: {err}')
        conn.close()
        return is_success


def get_course(values_list):
    is_success = False
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        query = "SELECT course FROM department_table WHERE department_name='%s' AND year='%s' AND semester='%s'"\
                % (values_list[0], values_list[1], values_list[2])
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        is_success = True
        return is_success, result
    except ms.Error as err:
        print(f'Error: {err}')
        conn.close()
        return is_success


def add_attendance(roll, course, date):
    is_success = False
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        query = "INSERT INTO attendance_table VALUES ('%s', '%s', '%s', 'P')" % (roll, course, date)
        cursor.execute(query)
        conn.commit()
        conn.close()
        is_success = True
        return is_success
    except ms.Error as err:
        print(f'Error: {err}')
        conn.close()
        return err


def save_to_complete_table(result):
    try:
        conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_database')
        cursor = conn.cursor()
        for row in result:
            query = "INSERT INTO attendance_complete_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            cursor.execute(query, val)
            conn.commit()
        conn.close()
    except ms.Error as err:
        print(f'Error here: {err}')
        conn.close()
        return err

