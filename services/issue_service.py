from rich.console import Console
from rich.table import Table

from database.connection import get_connection
from models.issue import Issue


console = Console()


class IssueService:

    def issue_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:

            book_id = int(input("\nEnter Book ID: "))
            member_id = int(input("Enter Member ID: "))
            issue_date = input(
                "Enter Issue Date (YYYY-MM-DD): "
            )
            due_date = input(
                "Enter Due Date (YYYY-MM-DD): "
            )

            cursor.execute(
                """
                SELECT available_quantity
                FROM books
                WHERE book_id = %s
                """,
                (book_id,)
            )

            book = cursor.fetchone()

            if not book:

                console.print(
                    "\n:X: [bold red]Book Not Found![/]"
                )
                return

            if book[0] <= 0:

                console.print(
                    "\n:warning: [bold yellow]Book Not Available![/]"
                )
                return

            cursor.execute(
                """
                SELECT member_id
                FROM members
                WHERE member_id = %s
                """,
                (member_id,)
            )

            member = cursor.fetchone()

            if not member:

                console.print(
                    "\n:X: [bold red]Member Not Found![/]"
                )
                return

           
            query = """
            INSERT INTO issued_books
            (
                book_id,
                member_id,
                issue_date,
                due_date,
                return_date,
                status
            )
            VALUES (%s, %s, %s, %s, NULL, 'Issued')
            """

            cursor.execute(
                query,
                (
                    book_id,
                    member_id,
                    issue_date,
                    due_date
                )
            )

            cursor.execute(
                """
                UPDATE books
                SET available_quantity =
                    available_quantity - 1
                WHERE book_id = %s
                """,
                (book_id,)
            )

            conn.commit()

            console.print(
                "\n:heavy_check_mark: [bold green]Book Issued Successfully![/]"
            )

        except Exception as e:

            conn.rollback()

            console.print(
                f"\n:X: [bold red]Error: {e}[/]"
            )

        finally:

            cursor.close()
            conn.close()


    def view_issued_books(self):

        conn = get_connection()
        cursor = conn.cursor()
    
        query = """
        SELECT
            issue_id,
            book_id,
            member_id,
            issue_date,
            due_date,
            return_date,
            status
        FROM issued_books
        """
    
        cursor.execute(query)
    
        records = cursor.fetchall()
    
        if not records:
    
            console.print(
                "\n:warning: [bold yellow]No Issued Books Found.[/]"
            )
    
        else:
    
            table = Table(
                title="Issued Books",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True
            )
    
            table.add_column(
                "Issue ID",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Book ID",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Member ID",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Issue Date",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Due Date",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Return Date",
                justify="center",
                style="green"
            )
    
            table.add_column(
                "Status",
                justify="center",
                style="green"
            )
    
            for record in records:
    
                issue_obj = Issue(*record)
    
                table.add_row(
                    str(issue_obj.issue_id),
                    str(issue_obj.book_id),
                    str(issue_obj.member_id),
                    str(issue_obj.issue_date),
                    str(issue_obj.due_date),
                    str(issue_obj.return_date)
                    if issue_obj.return_date
                    else "-",
                    issue_obj.status
                )
    
            console.print()
            console.print(table)
    
        cursor.close()
        conn.close()
    
    def search_issue(self):

        conn = get_connection()
        cursor = conn.cursor()

        issue_id = int(
            input("\nEnter Issue ID: ")
        )

        cursor.execute(
            """
            SELECT
                issue_id,
                book_id,
                member_id,
                issue_date,
                due_date,
                return_date,
                status
            FROM issued_books
            WHERE issue_id = %s
            """,
            (issue_id,)
        )

        issue = cursor.fetchone()

        if issue:

            issue_obj = Issue(*issue)

            table = Table(
                title="Issue Details",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
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
                "Issue ID",
                str(issue_obj.issue_id)
            )

            table.add_row(
                "Book ID",
                str(issue_obj.book_id)
            )

            table.add_row(
                "Member ID",
                str(issue_obj.member_id)
            )

            table.add_row(
                "Issue Date",
                str(issue_obj.issue_date)
            )

            table.add_row(
                "Due Date",
                str(issue_obj.due_date)
            )

            table.add_row(
                "Return Date",
                str(issue_obj.return_date)
                if issue_obj.return_date
                else "-"
            )

            table.add_row(
                "Status",
                issue_obj.status
            )

            console.print()
            console.print(table)

        else:

            console.print(
                "\n:X: [bold red]Issue Record Not Found.[/]"
            )

        cursor.close()
        conn.close()

    
    def return_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:

            issue_id = int(
                input("\nEnter Issue ID: ")
            )

            return_date = input(
                "Enter Return Date (YYYY-MM-DD): "
            )

            cursor.execute(
                """
                SELECT book_id, status
                FROM issued_books
                WHERE issue_id = %s
                """,
                (issue_id,)
            )

            issue = cursor.fetchone()

            if not issue:

                console.print(
                    "\n:X: [bold red]Issue Record Not Found.[/]"
                )
                return

            book_id = issue[0]
            status = issue[1]

            if status == "Returned":

                console.print(
                    "\n:warning: [bold yellow]Book Already Returned.[/]"
                )
                return

            cursor.execute(
                """
                UPDATE issued_books
                SET
                    return_date = %s,
                    status = 'Returned'
                WHERE issue_id = %s
                """,
                (return_date, issue_id)
            )

            cursor.execute(
                """
                UPDATE books
                SET available_quantity =
                    available_quantity + 1
                WHERE book_id = %s
                """,
                (book_id,)
            )

            conn.commit()

            console.print(
                "\n:heavy_check_mark: [bold green]Book Returned Successfully![/]"
            )

        except Exception as e:

            conn.rollback()

            console.print(
                f"\n:X:[bold red] Error: {e}[/]"
            )

        finally:

            cursor.close()
            conn.close()

    def view_member_issues(self):

        conn = get_connection()
        cursor = conn.cursor()

        member_id = int(
            input("\nEnter Member ID: ")
        )

        query = """
        SELECT
            issue_id,
            book_id,
            member_id,
            issue_date,
            due_date,
            return_date,
            status
        FROM issued_books
        WHERE member_id = %s
        """

        cursor.execute(
            query,
            (member_id,)
        )

        records = cursor.fetchall()

        if not records:

            console.print(
                "\n:warning: [bold yellow]No Records Found.[/]"
            )

        else:

            table = Table(
                title="Member Issues",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True
            )

            table.add_column(
                "Issue ID",
                justify="center",
                style="green"
            )

            table.add_column(
                "Book ID",
                justify="center",
                style="green"
            )

            table.add_column(
                "Member ID",
                justify="center",
                style="green"
            )

            table.add_column(
                "Issue Date",
                justify="center",
                style="green"
            )

            table.add_column(
                "Due Date",
                justify="center",
                style="green"
            )

            table.add_column(
                "Return Date",
                justify="center",
                style="green"
            )

            table.add_column(
                "Status",
                justify="center",
                style="green"
            )

            for record in records:

                issue_obj = Issue(*record)

                table.add_row(
                    str(issue_obj.issue_id),
                    str(issue_obj.book_id),
                    str(issue_obj.member_id),
                    str(issue_obj.issue_date),
                    str(issue_obj.due_date),
                    str(issue_obj.return_date)
                    if issue_obj.return_date
                    else "-",
                    issue_obj.status
                )

            console.print()
            console.print(table)

        cursor.close()
        conn.close()