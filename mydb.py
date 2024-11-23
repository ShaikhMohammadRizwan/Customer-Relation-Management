import mysql.connector

# Replace hardcoded credentials with variables
host = "localhost"  # Change to your host if necessary
user = "your_username"       # Change to your MySQL username
password = "your_password_here"  # Replace with your actual MySQL password

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE CRMDB")

print("Database 'CRMDB' created successfully!")
