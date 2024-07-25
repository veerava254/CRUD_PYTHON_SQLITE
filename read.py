from main import connect_to_db

connection = connect_to_db("mydb.db")
cursor = connection.cursor()

READ_SQL = """
SELECT * FROM bird
"""

cursor.execute(READ_SQL)
print(cursor.fetchall())
