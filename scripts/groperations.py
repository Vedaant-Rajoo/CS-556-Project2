from datetime import datetime

import mysql.connector

from scripts.connect import addToobjinfo

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


def grant_u(conn, user, bi, obj, privileges=None):
    cursor = conn.cursor(buffered=True)
    query = "GRANT %s ON cs556.%s TO %s@'%' WITH GRANT OPTION"
    cursor.execute(query, (privileges, obj, user))
    conn.commit()


def revoke(conn, user, obj, privileges=None):
    cursor = conn.cursor(buffered=True)
    if privileges is None:
        query = "REVOKE ALL PRIVILEGES ON cs556.%s FROM %s@'%'"
        cursor.execute(query, (obj, user))
        conn.commit()
        return
    else:
        query = "REVOKE %s ON cs556.%s FROM %s@'%'"
        cursor.execute(query, (privileges, obj, user))
        conn.commit()
        return


def saveJson(conn, obj, data):
    cursor = conn.cursor(buffered=True)
    query = "UPDATE json_data SET graph_data = %s WHERE obj = %s"
    cursor.execute(query, (data, obj))
    conn.commit()


def delegate(conn, obj, grantee, grantor):
    cursor = conn.cursor(buffered=True)
    addToobjinfo(obj, grantee, grantor, 'curator')
    # delegate admin privileges by giving them grant option
    q2 = "GRANT GRANT OPTION on cs556.%s to %s@'%%'" % (obj, grantee)
    cursor.execute(q2)
    q3 = "grant index on cs556.%s to %s@'%%'" % (obj, grantee)
    cursor.execute(q3)
    conn.commit()


def revoke_admin(conn, obj, grantee):
    cursor = conn.cursor(buffered=True)
    q1 = "REVOKE GRANT OPTION on cs556.%s from %s@'%%'" % (obj, grantee)
    cursor.execute(q1)
    q2 = "REVOKE index on cs556.%s from %s@'%%'" % (obj, grantee)
    cursor.execute(q2)
    conn.commit()
