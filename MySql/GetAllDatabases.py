import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=13.58.119.123;DATABASE=HO3_DIEP;UID=DIEP;PWD=10#HammerD!ep')

#Define a parameter to access the cursor method:
cur = conn.cursor()

cur.execute("select name from sys.databases")

for x in cur:
  print(x)