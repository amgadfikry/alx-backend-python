#!/usr/bin/python3
import mysql.connector


def stream_users(connection):
    """Generator connecting to the database and yielding rows from the users table.
    Args:
        connection (mysql.connector.connection.MySQLConnection): Connection object to the MySQL database.
    Yields:
        tuple: A row from the users table.
    Raises:
        mysql.connector.Error: If there is an error executing the query.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
