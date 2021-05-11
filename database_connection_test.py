import mysql.connector as ms

uname = "sumit"
password = "sumit123"

try:
    conn = ms.connect(host='localhost', user='root', password='', database='face_recognition_test')
    cursor = conn.cursor()
    # query = "INSERT INTO login_table VALUES ('%s', '%s')" % (uname, password)
    select_query = "SELECT username FROM login_table"
    print(select_query)
    cursor.execute(select_query)
    result = cursor.fetchall()
    print(f"{result}")
    for x in result:
        print(x)
    conn.commit()
    conn.close()
    print('Done')
except ms.Error as e:
    print('Could not connect to the database.')
    print(f'{e}')