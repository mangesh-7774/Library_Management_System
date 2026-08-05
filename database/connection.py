import mysql.connector
from mysql.connector import Error
from config.db_config import HOST, USER, PASSWORD, DATABASE


def get_connection():

    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        return connection

    except Error as e:
        print("\nDatabase Connection Failed!")
        print("Error :", e)
        return None


def close_connection(connection, cursor=None):
   
    try:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

    except Error as e:
        print("Error while closing connection :", e)


if __name__ == "__main__":

    conn = get_connection()

    if conn:
        print("Database Connected Successfully.")
        close_connection(conn)