from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from database.connection import get_connection, close_connection

console = Console()

def login():
    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()
    print()
    console.print(
        Panel(
            Align.center(
                "[bold green]ADMIN LOGIN[/]"
            ),
            border_style="bright_magenta",
        )
    )

    username = console.input("\n[bold yellow]Enter Username : [/]")
    password = console.input("[bold yellow]Enter Password : [/]")

    query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    close_connection(connection, cursor)

    if user:
        console.print("\n:heavy_check_mark: [bold green]Login Successful![/]")
        return True

    console.print("\n:X: [bold red]Invalid Username or Password.")
    return False

