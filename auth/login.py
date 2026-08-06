from database.connection import get_connection, close_connection

def login():
  connection = get_connection()

  if connection is None:
    return False

  cursor = connection.cursor()

  username = input("Enter Username : ")
  password = input("Enter Password : ")

  query = """
  select * from users where username=%s AND password=%s
  """

  cursor.execute(query,(username,password))

  user = cursor.fetchone()

  close_connection(connection,cursor)

  if user:
    print("\nLogin Successfull")
    return True
  else:
    print("\nInvalid Username or Password")
    return False


