from services.book_service import BookService

service = BookService()

def book_menu():
    while True:
        print("\n===== BOOK MANAGEMENT =====\n")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Back To Main Menu")
    
        choice = input("\nEnter your choice: ")
    
        if choice == "1":
            service.add_book()
    
        elif choice == "2":
            service.view_books()
    
        elif choice == "3":
            service.search_book()
    
        elif choice == "4":
            service.update_book()
    
        elif choice == "5":
            service.delete_book()
    
        elif choice == "6":
            print("\nThank You!")
            break
    
        else:
            print("\nInvalid Choice!")