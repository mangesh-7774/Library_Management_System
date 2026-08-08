from services.issue_service import IssueService

service = IssueService()

def issue_menu():
    while True:
        print("\n====== ISSUE & RETURN Management ======\n")
        print("1. Issue Book")
        print("2. View Issued Books")
        print("3. Search Issue")
        print("4. Return Book")
        print("5. View Member Issues")
        print("6. Back TO Main Menu")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            service.issue_book()

        elif choice == "2":
            service.view_issued_books()

        elif choice == "3":
            service.search_issue()

        elif choice == "4":
            service.return_book()

        elif choice == "5":
            service.view_member_issues()

        elif choice == "6":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid Choice! Please Try Again.")

