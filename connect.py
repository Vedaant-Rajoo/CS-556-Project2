import mysql.connector
from datetime import datetime, timedelta, date

# The list that contains the names of the DBA's
DBA = ['ava','emma','liam','noah']
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
cursor = conn.cursor()




