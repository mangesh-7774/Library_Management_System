from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from database.connection import get_connection, close_connection


console = Console()


class UserService:

    @staticmethod
    def register_admin():

        connection = get_connection()

        if connection is None:
            return False

        cursor = connection.cursor()
        print()

        try:

            console.print(
                Panel(
                    Align.center(
                        "[bold green]REGISTER ADMIN[/]"
                    ),
                    border_style="bright_magenta"
                )
            )

            username = console.input(
                "\n[bold yellow]Enter Username : [/]"
            )

            password = console.input(
                "[bold yellow]Enter Password : [/]"
            )

            if not username or not password:

                console.print(
                    "\n:warning:[bold yellow] "
                    "Username and password cannot be empty.[/]"
                )

                return False

            query = """
                SELECT user_id
                FROM users
                WHERE username = %s
            """

            cursor.execute(
                query,
                (username,)
            )

            existing_user = cursor.fetchone()

            if existing_user:

                console.print(
                    "\n:X: [bold red]Username already exists.[/]"
                )

                return False

            query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            """

            cursor.execute(
                query,
                (username, password)
            )

            connection.commit()

            console.print(
                "\n:heavy_check_mark:"
                "[bold green] Admin registered successfully![/]"
            )

            return True

        except Exception as e:

            connection.rollback()

            console.print(
                f"\n:X: [bold red]Error while registering admin: {e}[/]"
            )

            return False

        finally:

            close_connection(
                connection,
                cursor
            )

