import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin4545'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a db
cursorObject.execute("CREATE DATABASE django_crm")

print("All done!")