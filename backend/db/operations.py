from backend.db.connection import create_connection
from mysql.connector import Error

def execute_query(query, params=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def fetch_data(query, params=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")
            return []
        finally:
            cursor.close()
            connection.close()