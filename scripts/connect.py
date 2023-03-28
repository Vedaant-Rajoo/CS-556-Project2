import mysql.connector
from datetime import datetime

# The list that contains the names of the DBA's
DBA = ['ava','emma','liam','noah','mia']
HOST='localhost'
USERNAME='root'
PASSWORD='password'
DATABASE='cs556'
today = datetime.today()
# MySQL connection
config = {
    'user': USERNAME,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
    'raise_on_warnings': True,
    
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
    query = ("SELECT * FROM PAB")
    cursor.execute(query)
    results =  cursor.fetchall() 
    return results
 
def getObjectsAdmined(username):
    query = ("SELECT obj FROM obj_info WHERE own_cur = %s")
    cursor.execute(query,(username,))
    results =  cursor.fetchall() 
    return results

def isowner(username):
    query = ("SELECT * FROM obj_info WHERE own_cur = %s")
    cursor.execute(query,(username,))
    results =  cursor.fetchone() 
    if results:
        return True
    else:
        return False


