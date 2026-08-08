from database.connection import get_connection
from models.issue import Issue

class IssueService:

    # Issue Book
    def issue_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            book_id = int(input("Enter Book ID: "))
            member_id = int(input("Enter Member ID: "))
            issue_date = input("Enter Issue Date (YYYY-MM-DD): ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")

            # Check Book Exists
            cursor.execute(
                "SELECT available_quantity FROM books WHERE book_id=%s",
                (book_id,)
            )
            book = cursor.fetchone()

            if not book:
                print("Book Not Found!")
                return

            if book[0] <= 0:
                print("Book Not Available!")
                return

            # Check Member Exists
            cursor.execute(
                "SELECT member_id FROM members WHERE member_id=%s",
                (member_id,)
            )
            member = cursor.fetchone()

            if not member:
                print("Member Not Found!")
                return

            # Insert Issue Record
            query = """
            INSERT INTO issued_books
            (book_id, member_id, issue_date, due_date, return_date, status)
            VALUES (%s, %s, %s, %s, NULL, 'Issued')
            """

            cursor.execute(query, (book_id, member_id, issue_date, due_date))

            # Decrease Available Quantity
            cursor.execute(
                """
                UPDATE books
                SET available_quantity = available_quantity - 1
                WHERE book_id=%s
                """,
                (book_id,)
            )

            conn.commit()
            print("Book Issued Successfully!")

        except Exception as e:
            conn.rollback()
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Issued Books
    def view_issued_books(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            ib.issue_id,
            b.title,
            m.name,
            ib.issue_date,
            ib.due_date,
            ib.return_date,
            ib.status
        FROM issued_books ib
        JOIN books b
         ON ib.book_id = b.book_id
        JOIN members m
            ON ib.member_id = m.member_id
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("No Issued Books Found")

        else:
            print("\n========== ISSUED BOOKS ==========")

            for record in records:
                # print(
                #     f"""
                #     Issue ID     : {record[0]}
                #     Book Title   : {record[1]}
                #     Member Name  : {record[2]}
                #     Issue Date   : {record[3]}
                #     Due Date     : {record[4]}
                #     Return Date  : {record[5]}
                #     Status       : {record[6]}
                #     ----------------------------------"""
                # )
                issue_obj=Issue(*record)
                print(issue_obj)
            

        cursor.close()
        conn.close()

    # Search Issue
    def search_issue(self):

        conn = get_connection()
        cursor = conn.cursor()

        issue_id = int(input("Enter Issue ID: "))

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
            WHERE issue_id=%s
            """,
            (issue_id,)
        )

        issue = cursor.fetchone()

        if issue:
            print("\nIssue Found")

            issue_obj = Issue(*issue)
            print(issue_obj)

        else:
            print("Issue Record Not Found")

        cursor.close()
        conn.close()

    # Return Book
    def return_book(self):

        conn = get_connection()
        cursor = conn.cursor()

        try:

            issue_id = int(input("Enter Issue ID: "))
            return_date = input("Enter Return Date (YYYY-MM-DD): ")

            cursor.execute(
                """
                SELECT book_id, status
                FROM issued_books
                WHERE issue_id=%s
                """,
                (issue_id,)
            )

            issue = cursor.fetchone()

            if not issue:
                print("Issue Record Not Found")
                return

            book_id = issue[0]
            status = issue[1]

            if status == "Returned":
                print("Book Already Returned")
                return

            cursor.execute(
                """
                UPDATE issued_books
                SET return_date=%s,
                    status='Returned'
                WHERE issue_id=%s
                """,
                (return_date, issue_id)
            )

            cursor.execute(
                """
                UPDATE books
                SET available_quantity = available_quantity + 1
                WHERE book_id=%s
                """,
                (book_id,)
            )

            conn.commit()
            print("Book Returned Successfully!")

        except Exception as e:
            conn.rollback()
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Member Issues
    def view_member_issues(self):

        conn = get_connection()
        cursor = conn.cursor()

        member_id = int(input("Enter Member ID: "))

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
        WHERE member_id=%s
        """

        cursor.execute(query, (member_id,))

        records = cursor.fetchall()

        if not records:
            print("No Records Found")

        else:
            print("\n====== MEMBER ISSUES ======")

            for record in records:
                issue_obj = Issue(*record)
                print(issue_obj)

        cursor.close()
        conn.close()