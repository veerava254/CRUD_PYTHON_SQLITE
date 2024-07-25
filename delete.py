from main import connect_to_db

connection = connect_to_db("mydb.db")
cursor = connection.cursor()

DELETE_SQL = """
DELETE FROM bird
WHERE id = 4
"""

cursor.execute(DELETE_SQL)
connection.commit()
