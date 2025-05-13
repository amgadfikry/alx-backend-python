#!/user/bin/env python3
seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """ Generator that fetches users in batches from the user_data table.
    Args:
        batch_size (int): Number of rows to fetch per batch.
    Yields:
        list of tuples: A batch of user rows.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    connection.close()

def batch_processing(batch_size):
    """
    Process user data in batches, filtering users over age 25.
    Args:
        batch_size (int): Number of rows per batch.
    Returns:
        list of tuples: Filtered user rows.
    """
    result = []
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                result.append(user)
    return result
