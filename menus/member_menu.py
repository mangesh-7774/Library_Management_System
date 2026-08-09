from rich.panel import Panel
from rich.align import Align
from rich.console import Console

from services.member_service import MemberService

console = Console()


service = MemberService()


def display_member_menu():

    while True:

        console.print()

        console.print(
            Panel(
                Align.center(
                    "[bold green]MEMBER MANAGEMENT[/]"
                ),
                border_style="bright_magenta",
            )
        )

        console.print("\n[bold white]1.[/] Add New Member")
        console.print("[bold white]2.[/] View All Members")
        console.print("[bold white]3.[/] Search Member by ID")
        console.print("[bold white]4.[/] Delete Member")
        console.print("[bold white]5.[/] Back to Main Menu")

        choice = console.input(
            "\n[bold yellow]Enter your choice: [/]"
        )

        match choice:

            case "1":
                service.add_member()

            case "2":
                service.get_all_members()

            case "3":
                service.get_member_by_id()

            case "4":
                service.delete_member()

            case "5":
                console.print(
                    "\n:heavy_check_mark: [bold green]Back to Main Menu. Thank You![/]"
                )
                break

            case _:
                console.print(
                    "\n:x: [bold red]Invalid Choice![/]"
                )