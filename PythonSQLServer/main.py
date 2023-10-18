
import pyodbc

server ='.\MARGI'
database='BDInfiniteQIA'
username='sa'
password='margi.123'

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
)
cursor = conn.cursor()

cursor.execute(
    """     select c.name, t.name from sys.columns as c
            join sys.tables as t on c.object_id=t.object_id
            where c.object_id in (Select object_id from sys.tables)         
    """
)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(" select * from InfiniteQIA.Disciplina")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()


