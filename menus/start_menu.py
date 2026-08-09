from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from auth.login import login
from services.user_service import UserService

console = Console()


def start_menu():

    while True:
         print()
         console.print(
             Panel(
                 Align.center(
                     "[bold bold green]Login / Register[/]"
                 ),
                 border_style="bright_magenta",
             )
         )
         console.print("\n[bold white]1.[/] Login")
         console.print("[bold white]2.[/] Register Admin")
         console.print("[bold white]3.[/] Exit")
 
         choice = console.input("\n[bold yellow]Enter your choice : [/]")
 
         if choice == "1":
 
             if login():
                 return True
         elif choice == "2":
           UserService.register_admin()
 
         elif choice == "3":
            return "exit"
 
         else:
             console.print("\n:X: [bold red]Invalid choice. Please try again.[/]")
