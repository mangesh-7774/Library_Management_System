from database.connection import get_connection, close_connection


class UserService:

    @staticmethod
    def register_admin():
        connection = get_connection()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            print("\n========== REGISTER ADMIN ==========\n")

            username = input("Enter Username : ")
            password = input("Enter Password : ")

            if not username or not password:
                print("\nUsername and password cannot be empty.")
                return False

            # Check whether username already exists
            query = """
                SELECT user_id
                FROM users
                WHERE username = %s
            """

            cursor.execute(query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                print("\nUsername already exists.")
                return False

            # Insert new admin
            query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            """

            cursor.execute(query, (username, password))

            connection.commit()

            print("\nAdmin registered successfully!")
            return True

        except Exception as e:
            connection.rollback()
            print("\nError while registering admin:", e)
            return False

        finally:
            close_connection(connection, cursor)