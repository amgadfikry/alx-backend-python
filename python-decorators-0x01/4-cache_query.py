import time
import sqlite3 
import functools

# Global cache dictionary
query_cache = {}

# Decorator to handle DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('example.db')
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            print(f"[DB ERROR] {e}")
            conn.rollback()
            raise
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results based on the query string
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if not query:
            print("[CACHE] No query found, skipping cache.")
            return func(*args, **kwargs)

        if query in query_cache:
            print("[CACHE] Returning cached result.")
            return query_cache[query]

        print("[CACHE] Caching new result.")
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call - caches the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call - uses cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
