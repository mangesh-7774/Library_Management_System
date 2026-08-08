from database.connection import get_connection, close_connection


def login():
    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    print("\n======= ADMIN LOGIN =======\n")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    close_connection(connection, cursor)

    if user:
        print("\nLogin Successful!")
        return True

    print("\nInvalid Username or Password.")
    return False

