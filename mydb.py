import mysql.connector

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE CRMDB")

print("Database 'CRMDB' created successfully!")
