from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from services.issue_service import IssueService

console = Console()

service = IssueService()

def issue_menu():
    while True:
        print()
        console.print(
            Panel(
                Align.center(
                    "[bold green]ISSUE & RETURN Management[/]"
                ),
                border_style = "bright_magenta"
            )
        )

        console.print("\n[bold white]1.[/] Issue Book")
        console.print("[bold white]2.[/] View Issued Books")
        console.print("[bold white]3.[/] Search Issue")
        console.print("[bold white]4.[/] Return Book")
        console.print("[bold white]5.[/] View Member Issues")
        console.print("[bold white]6.[/] Back TO Main Menu")

        choice = console.input("\n[bold yellow]Enter Your Choice: [/]")

        if choice == "1":
            service.issue_book()

        elif choice == "2":
            service.view_issued_books()

        elif choice == "3":
            service.search_issue()

        elif choice == "4":
            service.return_book()

        elif choice == "5":
            service.view_member_issues()

        elif choice == "6":
            console.print("\n:heavy_check_mark: [bold green]Back to main menu[/]")
            break

        else:
            console.print("\n:X: [bold red]Invalid Choice! Please Try Again[/]")

