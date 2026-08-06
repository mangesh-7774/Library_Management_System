from database.connection import get_connection
from models.book import Book


class BookService:

    # Add Book
    def add_book(self):
        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        category = input("Enter Category: ")
        publisher = input("Enter Publisher: ")
        total_quantity = int(input("Enter Total Quantity: "))
        available_quantity = int(input("Enter Available Quantity: "))

        query = """
        INSERT INTO books
        (book_id, title, author, category, publisher,
        total_quantity, available_quantity)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            book_id,
            title,
            author,
            category,
            publisher,
            total_quantity,
            available_quantity
        )

        cursor.execute(query, values)
        conn.commit()

        print("\nBook added successfully!")

        cursor.close()
        conn.close()

    # View Books
    def view_books(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        if not books:
            print("No books available.")
        else:
            print("\n========== BOOK LIST ==========")
            for book in books:
                print(book)

        cursor.close()
        conn.close()

    # Search Book
    def search_book(self):
        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT * FROM books WHERE book_id=%s",
            (book_id,)
        )

        book = cursor.fetchone()

        if book:
            print("\nBook Found")
            print(book)
        else:
            print("Book not found.")

        cursor.close()
        conn.close()

    # Update Book
    def update_book(self):
        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("Enter Book ID to update: "))

        title = input("Enter New Title: ")
        author = input("Enter New Author: ")
        category = input("Enter New Category: ")
        publisher = input("Enter New Publisher: ")
        total_quantity = int(input("Enter Total Quantity: "))
        available_quantity = int(input("Enter Available Quantity: "))

        query = """
        UPDATE books
        SET
            title=%s,
            author=%s,
            category=%s,
            publisher=%s,
            total_quantity=%s,
            available_quantity=%s
        WHERE book_id=%s
        """

        values = (
            title,
            author,
            category,
            publisher,
            total_quantity,
            available_quantity,
            book_id
        )

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("Book updated successfully!")
        else:
            print("Book not found.")

        cursor.close()
        conn.close()

    # Delete Book
    def delete_book(self):
        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("Enter Book ID to delete: "))

        cursor.execute(
            "DELETE FROM books WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Book deleted successfully!")
        else:
            print("Book not found.")

        cursor.close()
        conn.close()