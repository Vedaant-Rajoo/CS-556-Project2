import mysql.connector
from datetime import datetime, timedelta, date
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
names = ['jacob', 'olivia', 'noah', 'emma', 'liam', 'ava', 'william', 'sophia', 'michael', 'isabella', 'james', 'mia', 'benjamin', 'charlotte', 'elijah', 'amelia', 'lucas', 'harper', 'mason', 'evelyn']

conn = mysql.connector.connect(**config)
cursor = conn.cursor()




