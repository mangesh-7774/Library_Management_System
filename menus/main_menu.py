from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from menus.book_menu import book_menu
from menus.member_menu import display_member_menu
from menus.issue_menu import issue_menu
from menus.report_menu import report_menu

console = Console()

def main_menu():
  while True:
    print()
    console.print(
        Panel(
            Align.center(
                "[bold green]ADMIN MENU[/]"
            ),
            border_style="bright_magenta",
        )
    )
    console.print("\n[bold white]1.[/] Book Management")
    console.print("[bold white]2.[/] Member Management")
    console.print("[bold white]3.[/] Issue & Return Management")
    console.print("[bold white]4.[/] Reports")
    console.print("[bold white]5.[/] Exit Library Management System")

    choice = console.input("\n[bold yellow]Enter your choice : [/]")

    match choice:
         case "1":
             book_menu()
         case "2":
             display_member_menu()
         case "3":
             issue_menu()
         case "4":
             report_menu()
         case "5":
             console.print("\n:heavy_check_mark: [bold green]Exit Library Management System[/]")
             break
         case _ :
             console.print("\n:X: [bold red]Invalid Input[/]") 
              



