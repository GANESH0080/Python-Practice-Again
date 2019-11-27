import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=13.58.119.123;DATABASE=HO3_DIEP;UID=DIEP;PWD=10#HammerD!ep')

#Define a parameter to access the cursor method:
cur = conn.cursor()

# Returning all database names via query
cur.execute('SELECT policyinfoid FROM [pas].[PolicyInfo_trn]')
for row in cur:
    print(row)
