# import matplotlib.pyplot as plt


# def get_db_connection():
#   # Uses the project's connection utility if available, falls back to mysql.connector
#   try:
#     from database.connection import get_connection

#     return get_connection()
#   except ImportError:
#     import mysql.connector

#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="hanipatil",  # Update with your MySQL password if required
#         database="library_db",
#     )


# def _get_column_sum(cursor, table, possible_columns):
#   try:
#     cursor.execute(f"SHOW COLUMNS FROM {table}")
#     existing_cols = [row[0].lower() for row in cursor.fetchall()]
#     for col in possible_columns:
#       if col.lower() in existing_cols:
#         cursor.execute(f"SELECT SUM({col}) FROM {table}")
#         val = cursor.fetchone()[0]
#         return val if val is not None else 0
#   except Exception:
#     pass
#   return 0


# def library_summary():
#   conn = get_db_connection()
#   cursor = conn.cursor()
#   try:
#     total_books = _get_column_sum(
#         cursor, "books", ["total_copies", "quantity", "copies", "total_stock"]
#     )
#     avail_copies = _get_column_sum(
#         cursor,
#         "books",
#         ["available_copies", "available", "stock", "qty_available"],
#     )
#     issued_copies = _get_column_sum(
#         cursor, "books", ["issued_copies", "issued", "borrowed"]
#     )

#     if total_books == 0:
#       cursor.execute("SELECT COUNT(*) FROM books")
#       total_books = cursor.fetchone()[0] or 0

#     try:
#       cursor.execute("SELECT COUNT(*) FROM members")
#       total_members = cursor.fetchone()[0] or 0
#     except Exception:
#       total_members = 0

#     active_issues = 0
#     try:
#       cursor.execute("SELECT COUNT(*) FROM issues WHERE status = 'active'")
#       active_issues = cursor.fetchone()[0] or 0
#     except Exception:
#       try:
#         cursor.execute(
#             "SELECT COUNT(*) FROM issues WHERE return_date IS NULL"
#         )
#         active_issues = cursor.fetchone()[0] or 0
#       except Exception:
#         pass

#     returned_books = 0
#     try:
#       cursor.execute("SELECT COUNT(*) FROM issues WHERE status = 'returned'")
#       returned_books = cursor.fetchone()[0] or 0
#     except Exception:
#       try:
#         cursor.execute(
#             "SELECT COUNT(*) FROM issues WHERE return_date IS NOT NULL"
#         )
#         returned_books = cursor.fetchone()[0] or 0
#       except Exception:
#         pass

#     print("\n==============================")
#     print("        LIBRARY SUMMARY")
#     print("==============================")
#     print(f"Total Books: {total_books}")
#     print(f"Available Copies: {avail_copies}")
#     print(f"Issued Copies: {issued_copies}")
#     print(f"Total Members: {total_members}")
#     print(f"Active Issues: {active_issues}")
#     print(f"Returned Books: {returned_books}")
#   finally:
#     cursor.close()
#     conn.close()


# def book_inventory_report():
#   conn = get_db_connection()
#   cursor = conn.cursor()
#   try:
#     total = _get_column_sum(
#         cursor, "books", ["total_copies", "quantity", "copies", "total_stock"]
#     )
#     available = _get_column_sum(
#         cursor,
#         "books",
#         ["available_copies", "available", "stock", "qty_available"],
#     )
#     issued = _get_column_sum(
#         cursor, "books", ["issued_copies", "issued", "borrowed"]
#     )

#     if total == 0:
#       cursor.execute("SELECT COUNT(*) FROM books")
#       total = cursor.fetchone()[0] or 0

#     print("\n==============================")
#     print("    BOOK INVENTORY REPORT")
#     print("==============================")
#     print(f"Total Copies: {total}")
#     print(f"Available Copies: {available}")
#     print(f"Issued Copies: {issued}")

#     categories = ["Available Copies", "Issued Copies"]
#     values = [available, issued]

#     plt.figure(figsize=(6, 4))
#     plt.bar(categories, values, color=["#4CAF50", "#FF9800"], width=0.5)
#     plt.title("Book Inventory: Available vs Issued")
#     plt.ylabel("Number of Copies")
#     plt.tight_layout()
#     plt.show()
#   finally:
#     cursor.close()
#     conn.close()


# def issue_return_report():
#   conn = get_db_connection()
#   cursor = conn.cursor()
#   try:
#     try:
#       cursor.execute("SELECT COUNT(*) FROM issues")
#       total_issues = cursor.fetchone()[0] or 0
#     except Exception:
#       total_issues = 0

#     active_issues = 0
#     try:
#       cursor.execute("SELECT COUNT(*) FROM issues WHERE status = 'active'")
#       active_issues = cursor.fetchone()[0] or 0
#     except Exception:
#       try:
#         cursor.execute(
#             "SELECT COUNT(*) FROM issues WHERE return_date IS NULL"
#         )
#         active_issues = cursor.fetchone()[0] or 0
#       except Exception:
#         pass

#     returned_issues = 0
#     try:
#       cursor.execute("SELECT COUNT(*) FROM issues WHERE status = 'returned'")
#       returned_issues = cursor.fetchone()[0] or 0
#     except Exception:
#       try:
#         cursor.execute(
#             "SELECT COUNT(*) FROM issues WHERE return_date IS NOT NULL"
#         )
#         returned_issues = cursor.fetchone()[0] or 0
#       except Exception:
#         pass

#     print("\n==============================")
#     print("     ISSUE & RETURN REPORT")
#     print("==============================")
#     print(f"Total Issues: {total_issues}")
#     print(f"Active Issues: {active_issues}")
#     print(f"Returned Issues: {returned_issues}")

#     categories = ["Active Issues", "Returned Issues"]
#     values = [active_issues, returned_issues]

#     plt.figure(figsize=(6, 4))
#     plt.bar(categories, values, color=["#2196F3", "#9C27B0"], width=0.5)
#     plt.title("Issue & Return Status Comparison")
#     plt.ylabel("Count")
#     plt.tight_layout()
#     plt.show()
#   finally:
#     cursor.close()
#     conn.close()


# def most_issued_books():
#   conn = get_db_connection()
#   cursor = conn.cursor()
#   results = []
#   try:
#     query = """
#             SELECT b.title, COUNT(i.book_id) as issue_count 
#             FROM issues i 
#             JOIN books b ON i.book_id = b.id 
#             GROUP BY b.id, b.title 
#             ORDER BY issue_count DESC 
#             LIMIT 5
#         """
#     cursor.execute(query)
#     results = cursor.fetchall()
#   except Exception:
#     try:
#       query = """
#                 SELECT b.title, COUNT(*) as issue_count 
#                 FROM issues i 
#                 JOIN books b ON i.book_id = b.book_id 
#                 GROUP BY b.title 
#                 ORDER BY issue_count DESC 
#                 LIMIT 5
#             """
#       cursor.execute(query)
#       results = cursor.fetchall()
#     except Exception:
#       results = []

#   print("\n==============================")
#   print("    TOP 5 MOST ISSUED BOOKS")
#   print("==============================")
#   book_titles = []
#   issue_counts = []

#   if not results:
#     print("No issue data available.")
#   else:
#     for row in results:
#       title, count = row
#       book_titles.append(title)
#       issue_counts.append(count)
#       print(f"Book: {title} | Issues: {count}")

#     plt.figure(figsize=(8, 5))
#     plt.barh(book_titles[::-1], issue_counts[::-1], color="#E91E63")
#     plt.xlabel("Number of Issues")
#     plt.title("Top 5 Most Issued Books")
#     plt.tight_layout()
#     plt.show()

#   cursor.close()
#   conn.close()

import matplotlib.pyplot as plt

from database.connection import get_connection


class ReportService:

    @staticmethod
    def library_summary():
        connection = get_connection()

        if not connection:
            print("Database connection failed.")
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

            print("\n========================================")
            print("           LIBRARY SUMMARY")
            print("========================================")
            print(f"Total Book Copies  : {total_books}")
            print(f"Available Copies   : {available_copies}")
            print(f"Issued Copies      : {issued_copies}")
            print(f"Total Members      : {total_members}")
            print(f"Total Issues       : {total_issues}")
            print(f"Active Issues      : {active_issues}")
            print(f"Returned Books     : {returned_books}")
            print("========================================")

        except Exception as e:
            print("Error generating library summary:", e)

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def book_inventory_report():
        connection = get_connection()

        if not connection:
            print("Database connection failed.")
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

            print("\n========================================")
            print("        BOOK INVENTORY REPORT")
            print("========================================")
            print(f"Total Copies      : {total}")
            print(f"Available Copies  : {available}")
            print(f"Issued Copies     : {issued}")
            print("========================================")

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
            print("Error generating inventory report:", e)

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def issue_return_report():
        connection = get_connection()

        if not connection:
            print("Database connection failed.")
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

            print("\n========================================")
            print("        ISSUE & RETURN REPORT")
            print("========================================")
            print(f"Total Issues      : {total_issues}")
            print(f"Active Issues     : {active_issues}")
            print(f"Returned Issues   : {returned_issues}")
            print("========================================")

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
            print("Error generating issue/return report:", e)

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def most_issued_books():
        connection = get_connection()

        if not connection:
            print("Database connection failed.")
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

            print("\n========================================")
            print("        TOP 5 MOST ISSUED BOOKS")
            print("========================================")

            if not results:
                print("No issue data available.")
                return

            book_titles = []
            issue_counts = []

            for index, row in enumerate(results, start=1):

                title = row[0]
                count = row[1]

                book_titles.append(title)
                issue_counts.append(count)

                print(f"{index}. {title} - {count} issues")

            print("========================================")

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
            print("Error generating most issued books report:", e)

        finally:
            cursor.close()
            connection.close()