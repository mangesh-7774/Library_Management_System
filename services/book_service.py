from rich.table import Table
from rich.console import Console

from database.connection import get_connection
from models.book import Book


console = Console()


class BookService:

    def add_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        title = input("\nEnter Book Title: ")
        author = input("Enter Author: ")
        category = input("Enter Category: ")
        publisher = input("Enter Publisher: ")
        total_quantity = int(input("Enter Total Quantity: "))

        query = """
        INSERT INTO books
        (title, author, category, publisher,
        total_quantity, available_quantity)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            title,
            author,
            category,
            publisher,
            total_quantity,
            total_quantity
        )

        cursor.execute(query, values)
        conn.commit()

        console.print(
            "\n:heavy_check_mark: [bold green]Book added successfully![/]"
        )

        cursor.close()
        conn.close()

    def view_books(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        if not books:

            console.print(
                "\n:warning: [bold yellow]No books available.[/]"
            )

        else:

            table = Table(
                title="Book List",
                title_style="bold bright_magenta",
                border_style="white",
                header_style="bold white",
                show_lines=True
            )

            table.add_column(
                "ID",
                justify="center",
                style="green"
            )

            table.add_column(
                "Title",
                style="green"
            )

            table.add_column(
                "Author",
                style="green"
            )

            table.add_column(
                "Category",
                style="green"
            )

            table.add_column(
                "Publisher",
                style="green"
            )

            table.add_column(
                "Total",
                justify="center",
                style="green"
            )

            table.add_column(
                "Available",
                justify="center",
                style="green"
            )

            for book in books:

                book_obj = Book(*book)

                table.add_row(
                    str(book_obj.book_id),
                    book_obj.title,
                    book_obj.author,
                    book_obj.category,
                    book_obj.publisher,
                    str(book_obj.total_quantity),
                    str(book_obj.available_quantity)
                )

            console.print()
            console.print(table)

        cursor.close()
        conn.close()

    def search_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT * FROM books WHERE book_id = %s",
            (book_id,)
        )

        book = cursor.fetchone()

        if book:

            book_obj = Book(*book)

            table = Table(
                title="Book Details",
                title_style="bold bright_magenta",
                border_style="white",
                header_style="bold white",
                show_lines=True
            )

            table.add_column(
                "Field",
                style="bold white"
            )

            table.add_column(
                "Details",
                style="green"
            )

            table.add_row(
                "Book ID",
                str(book_obj.book_id)
            )

            table.add_row(
                "Title",
                book_obj.title
            )

            table.add_row(
                "Author",
                book_obj.author
            )

            table.add_row(
                "Category",
                book_obj.category
            )

            table.add_row(
                "Publisher",
                book_obj.publisher
            )

            table.add_row(
                "Total Quantity",
                str(book_obj.total_quantity)
            )

            table.add_row(
                "Available Quantity",
                str(book_obj.available_quantity)
            )

            console.print()
            console.print(table)

        else:

            console.print(
                "\n:X: [bold red]Book not found.[/]"
            )

        cursor.close()
        conn.close()

    def update_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(input("\nEnter Book ID to update : "))

        title = input("\nEnter New Title: ")
        author = input("Enter New Author: ")
        category = input("Enter New Category: ")
        publisher = input("Enter New Publisher: ")

        total_quantity = int(
            input("Enter Total Quantity: ")
        )

        available_quantity = int(
            input("Enter Available Quantity: ")
        )

        query = """
        UPDATE books
        SET
            title = %s,
            author = %s,
            category = %s,
            publisher = %s,
            total_quantity = %s,
            available_quantity = %s
        WHERE book_id = %s
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

            console.print(
                "\n:heavy_check_mark: [bold green]Book updated successfully![/]"
            )

        else:

            console.print(
                "\n:X: [bold red]Book not found.[/]"
            )

        cursor.close()
        conn.close()

    def delete_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        book_id = int(
            input("Enter Book ID to delete: ")
        )

        cursor.execute(
            "DELETE FROM books WHERE book_id = %s",
            (book_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:

            console.print(
                "\n:heavy_check_mark: [bold green]Book deleted successfully![/]"
            )

        else:

            console.print(
                "\n:X: [bold red]Book not found.[/]"
            )

        cursor.close()
        conn.close()