from datetime import datetime

import mysql.connector

# The list that contains the names of the DBA's
DBA = ['ava', 'emma', 'liam', 'noah', 'mia']
HOST = 'db-mysql-nyc1-25733-do-user-12162670-0.b.db.ondigitalocean.com'
USERNAME = 'doadmin'
PASSWORD = 'AVNS_4anP4ScJ6ehESNXnl5J'
DATABASE = 'cs556'
PORT = 25060
today = datetime.today()
# MySQL connection
config = {
    'user': USERNAME,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
    'port': PORT,
    'ssl_ca': 'ca-certificate.crt',
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered=True)


# Function to check if the user is a DBA (Database Administrator)


def isDBA(username):
    if username in DBA:
        return True
    else:
        return False


def getPolicies(obj=None):
    if obj is None:
        query = "SELECT * FROM PAB"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    else:
        query = "SELECT * FROM PAB WHERE object = %s"
        cursor.execute(query, (obj,))
        result = cursor.fetchone()
        return result


def getObjectsAdmined(username):
    query = "SELECT obj FROM obj_info WHERE own_cur = %s"
    cursor.execute(query, (username,))
    results = cursor.fetchall()
    return results


def isowner(username):
    """
    Checks if the user is the owner of any object
    :param username:
    :return:
    """
    query = "SELECT * FROM obj_info WHERE own_cur = %s"
    cursor.execute(query, (username,))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False


def isOwner(username, obj):
    """
    Checks if the user is the owner of the object
    :param username:
    :param obj:
    :return:
    """
    query = "SELECT * FROM obj_info WHERE own_cur = %s AND obj = %s AND type = %s"
    cursor.execute(query, (username, obj, 'owner'))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False


def isCurator(username, obj):
    """
    Checks if the user is the curator of the object
    :param username:
    :param obj:
    :return:
    """
    query = "SELECT * FROM obj_info WHERE own_cur = %s AND obj = %s AND type = %s"
    cursor.execute(query, (username, obj, 'curator'))
    results = cursor.fetchone()
    if results:
        return True
    else:
        return False


def getObjects():
    query = "SELECT obj FROM obj_info"
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def add_Policy(obj, policy_type, delegation, transfer, acceptance, revocation):
    query = "INSERT INTO PAB (object, pt, delegation, transfer, acceptance, revoke_opt) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (obj, policy_type, delegation, transfer, acceptance, revocation))
    conn.commit()


def getLogs():
    query = "SELECT * FROM logs"
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def addLog(command, username):
    query = "INSERT INTO logs (command, user) VALUES (%s, %s)"
    cursor.execute(query, (command, username))
    conn.commit()


def getJSONGraph(obj):
    query = "SELECT graph_data FROM json_data WHERE obj = %s"
    cursor.execute(query, (obj,))
    result = cursor.fetchone()
    return result


def addToobjinfo(obj, username, grantor, type):
    query = "INSERT INTO obj_info (obj, own_cur, bi, type) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (obj, username, grantor, type))
    conn.commit()


def removeFromobjinfo(obj, username, bi):
    query = "DELETE FROM obj_info WHERE obj = %s AND own_cur = %s AND bi = %s"
    cursor.execute(query, (obj, username, bi))
    conn.commit()


def allAccessToJson(username):
    query = "GRANT ALL PRIVILEGES ON cs556.json_data TO %s@'%'"
    cursor.execute(query, (username,))
    conn.commit()


def revoke_ad(username, obj):
    q2 = "REVOKE GRANT OPTION on cs556.%s from %s@'%%'" % (obj, username)
    cursor.execute(q2)
    conn.commit()
    if isCurator(username, obj):
        query = "REVOKE ALL PRIVILEGES ON cs556.json_data FROM %s@'%'"
        cursor.execute(query, (username,))
        conn.commit()
        q3 = "REVOKE GRANT OPTION on cs556.%s from %s@'%%'" % (obj, username)
