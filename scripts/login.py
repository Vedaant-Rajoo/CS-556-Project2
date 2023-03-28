import mysql.connector

HOST = 'db-mysql-nyc1-25733-do-user-12162670-0.b.db.ondigitalocean.com'
USERNAME = 'doadmin'
PASSWORD = 'AVNS_4anP4ScJ6ehESNXnl5J'
DATABASE = 'cs556'
PORT = 25060
# MySQL connection
config = dict(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE, raise_on_warnings=True, port=PORT, ssl_ca='ca-certificate.crt')


def login(username, password):
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

