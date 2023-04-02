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


def getPolicies():
    query = "SELECT * FROM PAB"
    cursor.execute(query)
    results = cursor.fetchall()
    return results


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
