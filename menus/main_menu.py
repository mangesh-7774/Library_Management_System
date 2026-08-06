from menus.book_menu import book_menu
from menus.member_menu import display_member_menu


def main_menu():
  while True:
    print("\n" + "=" * 30 + "Library Management System" + "=" * 30)

    print("\n1.Book Management")
    print("2.Member Management")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Reports")
    print("6.Exit")

    choice = int(input("Enter your choice : "))

    match choice:
         case 1:
             book_menu()
         case 2:
             display_member_menu()
         case 3:
             pass
         case 4:
             pass
         case 5:
             pass
         case _ :
             print("Invalid Input") 
              



