from main import connect_to_db

connection = connect_to_db("mydb.db")

INSERT_SQL = """
INSERT INTO bird(name)
VALUES
("humming2 bird"),
("hill2 jay")
"""

with connect_to_db("mydb.db") as connection:
  connection.execute(INSERT_SQL)
