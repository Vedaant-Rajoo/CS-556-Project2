from datetime import datetime

import mysql.connector

HOST = 'db-mysql-nyc1-25733-do-user-12162670-0.b.db.ondigitalocean.com'
DATABASE = 'cs556'
PORT = 25060
today = datetime.today()


# MySQL connection
def connect(username, password):
    config = {
        'user': username,
        'password': password,
        'host': HOST,
        'database': DATABASE,
        'port': PORT,
        'ssl_ca': 'ca-certificate.crt',
    }
    conn = mysql.connector.connect(**config)
    return conn


def getGraph(conn, obj):
    cursor = conn.cursor(buffered=True)
    query = "SELECT graph_data FROM json_data WHERE obj = %s"
    cursor.execute(query, (obj,))
    result = cursor.fetchone()
    return result[0]


def grant_u(conn, user, obj, privileges=None):
    cursor = conn.cursor(buffered=True)
    query = "GRANT %s on cs556.%s to %s@'%'"
    q2 = "GRANT ALL on cs556.json_data to %s@'%'"
    cursor.execute(query, (privileges, obj, user))
    conn.commit()
    cursor.execute(q2, (user,))
    conn.commit()


def revoke(conn, user, obj, privileges=None):
    cursor = conn.cursor(buffered=True)
    if privileges is None:
        query = "REVOKE ALL PRIVILEGES on cs556.%s from %s@'%'"
        q2 = "REVOKE ALL PRIVILEGES on cs556.json_data from %s@'%'"
        cursor.execute(query, (obj, user))
        conn.commit()
        cursor.execute(q2, (user,))
        conn.commit()
        return
    else:
        query = "REVOKE %s on cs556.%s from %s@'%'"
        cursor.execute(query, (privileges, obj, user))
        conn.commit()
        return


def saveJson(conn, obj, data):
    cursor = conn.cursor(buffered=True)
    query = "UPDATE json_data SET graph_data = %s WHERE obj = %s"
    cursor.execute(query, (data, obj))
    conn.commit()


def delegate(conn, obj, grantee):
    cursor = conn.cursor(buffered=True)
    query = "insert into obj_info (obj,own_cur,type) values (%s,%s,'curator')"
    cursor.execute(query, (obj, grantee))
    conn.commit()
