from services.report_service import (
    book_inventory_report,
    issue_return_report,
    library_summary,
    most_issued_books,
)


def report_menu():
  while True:
    print("\n==============================")
    print("          REPORT MENU")
    print("==============================")
    print("1. Library Summary")
    print("2. Book Inventory Report")
    print("3. Issue & Return Report")
    print("4. Most Issued Books")
    print("5. Back")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
      library_summary()
    elif choice == "2":
      book_inventory_report()
    elif choice == "3":
      issue_return_report()
    elif choice == "4":
      most_issued_books()
    elif choice == "5":
      print("Returning to previous menu...")
      break
    else:
      print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
  report_menu()