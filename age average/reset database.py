
import mysql.connector as sql

connection = sql.connect(user="root",
                            password="",
                            host="localhost",
                            database="age")
cursor = connection.cursor()
cursor.execute("Drop database age")