from main import connect_to_db

connection = connect_to_db("mydb.db")
cursor = connection.cursor()

UPDATE_SQL = """
UPDATE bird
SET name = "Indian bird"
WHERE id = 1
"""

cursor.execute(UPDATE_SQL)
connection.commit()
