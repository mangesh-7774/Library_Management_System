from rich.table import Table
from rich.console import Console

from database.connection import get_connection
from models.member import Member


console = Console()


class MemberService:

    def add_member(self):

        conn = get_connection()
        cursor = conn.cursor()

        name = input("\nEnter Name: ")
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        membership_date = input(
            "Enter Membership Date (YYYY-MM-DD): "
        )

        query = """
        INSERT INTO members
        (name, gender, phone, email, address, membership_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            gender,
            phone,
            email,
            address,
            membership_date
        )

        cursor.execute(query, values)
        conn.commit()

        console.print(
            "\n:heavy_check_mark: [bold green]Member added successfully![/]"
        )

        cursor.close()
        conn.close()

    def get_all_members(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members")

        members = cursor.fetchall()

        if not members:

            console.print(
                "\n:warning: [bold yellow]No members available.[/]"
            )

        else:

            table = Table(
                title="Member List",
                title_style="bold bright_magenta",
                border_style="bright_magenta",
                header_style="bold white",
                show_lines=True
            )

            table.add_column(
                "ID",
                justify="center",
                style="green"
            )

            table.add_column(
                "Name",
                style="green"
            )

            table.add_column(
                "Gender",
                justify="center",
                style="green"
            )

            table.add_column(
                "Phone",
                style="green"
            )

            table.add_column(
                "Email",
                style="green"
            )

            table.add_column(
                "Address",
                style="green"
            )

            table.add_column(
                "Membership Date",
                justify="center",
                style="green"
            )

            for member in members:

                member_obj = Member(*member)

                table.add_row(
                    str(member_obj.member_id),
                    member_obj.name,
                    member_obj.gender,
                    member_obj.phone,
                    member_obj.email,
                    member_obj.address,
                    str(member_obj.membership_date)
                )

            console.print()
            console.print(table)

        cursor.close()
        conn.close()

    def get_member_by_id(self):

        conn = get_connection()
        cursor = conn.cursor()

        member_id = int(
            input("\nEnter Member ID: ")
        )

        cursor.execute(
            "SELECT * FROM members WHERE member_id = %s",
            (member_id,)
        )

        member = cursor.fetchone()

        if member:

            member_obj = Member(*member)

            table = Table(
                title="Member Details",
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
                "Member ID",
                str(member_obj.member_id)
            )

            table.add_row(
                "Name",
                member_obj.name
            )

            table.add_row(
                "Gender",
                member_obj.gender
            )

            table.add_row(
                "Phone",
                member_obj.phone
            )

            table.add_row(
                "Email",
                member_obj.email
            )

            table.add_row(
                "Address",
                member_obj.address
            )

            table.add_row(
                "Membership Date",
                str(member_obj.membership_date)
            )

            console.print()
            console.print(table)

        else:

            console.print(
                "\n:X: [bold red]Member not found.[/]"
            )

        cursor.close()
        conn.close()

    def delete_member(self):

        conn = get_connection()
        cursor = conn.cursor()

        member_id = int(
            input("\nEnter Member ID to delete: ")
        )

        cursor.execute(
            "DELETE FROM members WHERE member_id = %s",
            (member_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:

            console.print(
                "\n:heavy_check_mark: [bold green]Member deleted successfully![/]"
            )

        else:

            console.print(
                "\n:X: [bold red]Member not found.[/]"
            )

        cursor.close()
        conn.close()