import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=13.234.53.206;UID=PPE;PWD=10#HammerPPEtest')

#Define a parameter to access the cursor method:
cur = conn.cursor()

cur.execute("CREATE DATABASE mydatabase")