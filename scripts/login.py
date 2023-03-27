import mysql.connector

HOST='localhost'
USERNAME='root'
PASSWORD='password'
DATABASE='cs556'
# MySQL connection
config = {
    'user': USERNAME,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
    'raise_on_warnings': True,
}

def login(username,password):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT password FROM user_info WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result is not None and result[0] == password:
        return True
    else:
        return False
