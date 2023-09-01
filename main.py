import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonmysql"
)

# print(database) => check if database connection is established or not

mycursor = database.cursor()

# mycursor.execute("CREATE DATABASE pythonmysql"); => create new database

# mycursor.execute('SHOW DATABASES') => Show databases
#
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") => create table
# mycursor.execute('SHOW TABLES') => Show Tables
#
# for x in mycursor:
#     print(x)

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") => Alter Table

