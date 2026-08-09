import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from database.connection import get_connection


console = Console()


class ReportService:

    @staticmethod
    def library_summary():

        connection = get_connection()

        if not connection:

            console.print(
                "\n:X: [bold red]Database connection failed.[/]"
            )
            return

        cursor = connection.cursor()

        try:

            cursor.execute(
                "SELECT SUM(total_quantity) FROM books"
            )
            total_books = cursor.fetchone()[0] or 0

            cursor.execute(
                "SELECT SUM(available_quantity) FROM books"
            )
            available_copies = cursor.fetchone()[0] or 0

            issued_copies = total_books - available_copies

            cursor.execute(
                "SELECT COUNT(*) FROM members"
            )
            total_members = cursor.fetchone()[0] or 0

            cursor.execute(
                "SELECT COUNT(*) FROM issued_books"
            )
            total_issues = cursor.fetchone()[0] or 0

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM issued_books
                WHERE status = 'Issued'
                """
            )
            active_issues = cursor.fetchone()[0] or 0

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM issued_books
                WHERE status = 'Returned'
                """
            )
            returned_books = cursor.fetchone()[0] or 0

            table = Table(
                title="Library Summary",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True,
                expand=True,
                width=70
            )

            table.add_column(
                "Report",
                style="bold white",
                justify="left",
                width=40
            )

            table.add_column(
                "Count",
                style="green",
                justify="center",
                width=20
            )

            table.add_row(
                "Total Book Copies",
                str(total_books)
            )

            table.add_row(
                "Available Copies",
                str(available_copies)
            )

            table.add_row(
                "Issued Copies",
                str(issued_copies)
            )

            table.add_row(
                "Total Members",
                str(total_members)
            )

            table.add_row(
                "Total Issues",
                str(total_issues)
            )

            table.add_row(
                "Active Issues",
                str(active_issues)
            )

            table.add_row(
                "Returned Books",
                str(returned_books)
            )

            console.print()
            console.print(table)

        except Exception as e:

            console.print(
                f"\n:X: [bold red]Error generating library summary: {e}[/]"
            )

        finally:

            cursor.close()
            connection.close()

    @staticmethod
    def book_inventory_report():

        connection = get_connection()

        if not connection:

            console.print(
                "\n:X: [bold red]Database connection failed.[/]"
            )
            return

        cursor = connection.cursor()

        try:

            cursor.execute(
                "SELECT SUM(total_quantity) FROM books"
            )
            total = cursor.fetchone()[0] or 0

            cursor.execute(
                "SELECT SUM(available_quantity) FROM books"
            )
            available = cursor.fetchone()[0] or 0

            issued = total - available

            table = Table(
                title="Book Inventory Report",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True,
                expand=True,
                width=70
            )

            table.add_column(
                "Inventory",
                style="bold white",
                justify="left",
                width=40
            )

            table.add_column(
                "Copies",
                style="green",
                justify="center",
                width=20
            )

            table.add_row(
                "Total Copies",
                str(total)
            )

            table.add_row(
                "Available Copies",
                str(available)
            )

            table.add_row(
                "Issued Copies",
                str(issued)
            )

            console.print()
            console.print(table)

            categories = [
                "Available Copies",
                "Issued Copies"
            ]

            values = [
                available,
                issued
            ]

            plt.figure(figsize=(7, 5))

            plt.bar(
                categories,
                values
            )

            plt.title("Book Inventory")
            plt.ylabel("Number of Copies")

            plt.tight_layout()
            plt.show()

        except Exception as e:

            console.print(
                f"\n:X: [bold red]Error generating inventory report: {e}[/]"
            )

        finally:

            cursor.close()
            connection.close()

    @staticmethod
    def issue_return_report():

        connection = get_connection()

        if not connection:

            console.print(
                "\n:X: [bold red]Database connection failed.[/]"
            )
            return

        cursor = connection.cursor()

        try:

            cursor.execute(
                "SELECT COUNT(*) FROM issued_books"
            )
            total_issues = cursor.fetchone()[0] or 0

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM issued_books
                WHERE status = 'Issued'
                """
            )
            active_issues = cursor.fetchone()[0] or 0

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM issued_books
                WHERE status = 'Returned'
                """
            )
            returned_issues = cursor.fetchone()[0] or 0

            table = Table(
                title="Issue & Return Report",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True,
                expand=True,
                width=70
            )

            table.add_column(
                "Report",
                style="bold white",
                justify="left",
                width=40
            )

            table.add_column(
                "Count",
                style="green",
                justify="center",
                width=20
            )

            table.add_row(
                "Total Issues",
                str(total_issues)
            )

            table.add_row(
                "Active Issues",
                str(active_issues)
            )

            table.add_row(
                "Returned Issues",
                str(returned_issues)
            )

            console.print()
            console.print(table)

            categories = [
                "Active Issues",
                "Returned Issues"
            ]

            values = [
                active_issues,
                returned_issues
            ]

            plt.figure(figsize=(7, 5))

            plt.bar(
                categories,
                values
            )

            plt.title("Issued vs Returned Books")
            plt.ylabel("Number of Issues")

            plt.tight_layout()
            plt.show()

        except Exception as e:

            console.print(
                f"\n:X: [bold red]Error generating issue/return report: {e}[/]"
            )

        finally:

            cursor.close()
            connection.close()

    @staticmethod
    def most_issued_books():

        connection = get_connection()

        if not connection:

            console.print(
                "\n:X: [bold red]Database connection failed.[/]"
            )
            return

        cursor = connection.cursor()

        try:

            query = """
                SELECT
                    b.title,
                    COUNT(ib.book_id) AS issue_count
                FROM issued_books ib
                JOIN books b
                    ON ib.book_id = b.book_id
                GROUP BY b.book_id, b.title
                ORDER BY issue_count DESC
                LIMIT 5
            """

            cursor.execute(query)

            results = cursor.fetchall()

            if not results:

                console.print(
                    "\n:warning: [bold yellow]No issue data available.[/]"
                )
                return

            table = Table(
                title="Top 5 Most Issued Books",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True,
                expand=True,
                width=80
            )

            table.add_column(
                "Rank",
                justify="center",
                style="green",
                width=10
            )

            table.add_column(
                "Book Title",
                style="green",
                width=50
            )

            table.add_column(
                "Issue Count",
                justify="center",
                style="green",
                width=20
            )

            book_titles = []
            issue_counts = []

            for index, row in enumerate(
                results,
                start=1
            ):

                title = row[0]
                count = row[1]

                book_titles.append(title)
                issue_counts.append(count)

                table.add_row(
                    str(index),
                    title,
                    str(count)
                )

            console.print()
            console.print(table)

            plt.figure(figsize=(9, 5))

            plt.barh(
                book_titles[::-1],
                issue_counts[::-1]
            )

            plt.title("Top 5 Most Issued Books")
            plt.xlabel("Number of Issues")

            plt.tight_layout()
            plt.show()

        except Exception as e:

            console.print(
                f"\n:X: [bold red]Error generating most issued books report: {e}[/]"
            )

        finally:

            cursor.close()
            connection.close()

