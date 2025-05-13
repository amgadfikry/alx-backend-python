#!/usr/bin/python3
# seed.py
import csv
import mysql.connector

def connect_to_db():
    """Connect to the MySQL database and return the connection object.
    Returns:
        mysql.connector.connection.MySQLConnection: Connection object to the MySQL database.
    Raises:
        mysql.connector.Error: If there is an error connecting to the database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it doesn't exist.
    Args:
        connection to mysql database
    Returns:
        None
    Raises:
        mysql.connector.Error: If there is an error creating the database.
    Finally:
        close the cursor.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database and return the connection object.
    Returns:
        connection to mysql database
    Raises:
        mysql.connector.Error: If there is an error connecting to the database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='ALX_prodev')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create the user_data table if it doesn't exist.
    Args:
        connection to mysql database
    Returns:
        None
    Raises:
        mysql.connector.Error: If there is an error creating the table.
    """
    table = f"CREATE TABLE IF NOT EXISTS  user_data\
        (user_id UUID PRIMARY KEY,\
        name VARCHAR NOT NULL,\
        email VARCHAR NOT NULL,\
        age DECIMAL NOT NULL)\
    "
    try:
        cursor = connection.cursor()
        cursor.execute(table)
        print("Table created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_data(connection, data):
    """insert data from csv file into the user_data table and commit the changes.
    Args:
        connection to mysql database
        data: path to the csv file
    Returns:
        None
    Raises:
        mysql.connector.Error: If there is an error inserting the data.
    """
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
        with open(data, 'r') as file:
            csv_reader = csv.reader(file)
            row = next(csv_reader)
            for row in csv_reader:
                cursor.execute(insert_query, row)
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
