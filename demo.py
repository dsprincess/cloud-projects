import pypyodbc as odbc # pip install pypyodbc
import pandas as pd # pip install pandas
from credential import username, password

server = 'sqldbservershai.database.windows.net'
database = 'sqldatabase'
connection_string = f'Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

try:
    conn = odbc.connect(connection_string)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")


sql = '''
SELECT ProductId, Name
FROM SalesLT.Product
'''

cursor = conn.cursor()
cursor.execute(sql)

dataset = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame(dataset, columns=columns)
print(df)