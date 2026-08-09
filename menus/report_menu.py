from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from services.report_service import ReportService

console = Console()

def report_menu():

    while True:
        print()
        
        console.print(
            Panel(
                Align.center(
                    "[bold green]Reports[/]"
                ),
                border_style="bright_magenta",
            )
        )
        console.print("\n[bold white]1.[/] Library Summary")
        console.print("[bold white]2.[/] Book Inventory Report")
        console.print("[bold white]3.[/] Issue & Return Report")
        console.print("[bold white]4.[/] Most Issued Books")
        console.print("[bold white]5.[/] Back To Main Menu")

        choice = console.input("\n[bold yellow]Enter your choice: [/]")

        if choice == "1":
            ReportService.library_summary()

        elif choice == "2":
            ReportService.book_inventory_report()

        elif choice == "3":
            ReportService.issue_return_report()

        elif choice == "4":
            ReportService.most_issued_books()

        elif choice == "5":
            console.print("\n:heavy_check_mark: [bold green]Back to main menu[/]")
            break

        else:
            console.print("\n:X: [bold red]Invalid choice. Please try again[/]")