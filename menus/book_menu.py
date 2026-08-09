from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from services.book_service import BookService

console = Console()

service = BookService()

def book_menu():
    while True:
        print()
        console.print(
            Panel(
                Align.center(
                    "[bold green]BOOK MANAGEMENT[/]"
                ),
                border_style = "bright_magenta"
            )
        )

        console.print("\n[bold white]1.[/] Add Book")
        console.print("[bold white]2.[/] View Books")
        console.print("[bold white]3.[/] Search Book")
        console.print("[bold white]4.[/] Update Book")
        console.print("[bold white]5.[/] Delete Book")
        console.print("[bold white]6.[/] Back To Main Menu")
    
        choice = console.input("\n[bold yellow]Enter your choice: [/]")
    
        if choice == "1":
            service.add_book()
    
        elif choice == "2":
            service.view_books()
    
        elif choice == "3":
            service.search_book()
    
        elif choice == "4":
            service.update_book()
    
        elif choice == "5":
            service.delete_book()
    
        elif choice == "6":
            console.print("\n:heavy_check_mark: [bold green]Back to mani menu, Thank You![/]")
            break
    
        else:
            console.print("\n:X: [bold red]Invalid Choice![/]")