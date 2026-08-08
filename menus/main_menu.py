from menus.book_menu import book_menu
from menus.member_menu import display_member_menu
from menus.issue_menu import issue_menu
from menus.report_menu import report_menu


def main_menu():
  while True:
    print("\n" + "=" * 30 + " Admin Menu " + "=" * 30)

    print("\n1.Book Management")
    print("2.Member Management")
    print("3.Issue & Return Management")
    print("4.Reports")
    print("5.Exit Library Management System")

    choice = int(input("\nEnter your choice : "))

    match choice:
         case 1:
             book_menu()
         case 2:
             display_member_menu()
         case 3:
             issue_menu()
         case 4:
             report_menu()
         case 5:
             print("Exit Library Management System")
             break
         case _ :
             print("Invalid Input") 
              



