#!/user/bin/env python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """ Generator that fetches users in batches from the user_data table.
    Args:
        batch_size (int): Number of rows to fetch per batch.
    Yields:
        list of tuples: A batch of user rows.
    Raises:
        mysql.connector.Error: If there is an error connecting to the database.
    Finally:
        Closes the database connection and cursor.
    """
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='ALX_prodev',
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Process user data in batches, filtering users over age 25.
    Args:
        batch_size (int): Number of rows per batch.
    Yields:
        tuple: Filtered user row where age > 25.
    Raises:
        mysql.connector.Error: If there is an error connecting to the database.
    Finally:
        Closes the database connection and cursor.
    """
    result = []
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user[3] > 25:
                result.append(user)
    return result
