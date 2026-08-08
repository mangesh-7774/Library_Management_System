from auth.login import login
from services.user_service import UserService

def start_menu():

    while True:
        print("\n ----- Login/Register -----\n")
        print("1. Login")
        print("2. Register Admin")
        print("3. Exit")
        print("-"*20)

        choice = input("Enter your choice : ")

        if choice == "1":

            if login():
                return True
        elif choice == "2":
          UserService.register_admin()

        elif choice == "3":
            print("\nThank you for using Library Management System!")
            return False

        else:
            print("\nInvalid choice. Please try again.")
