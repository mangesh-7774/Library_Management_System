from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
from menus.start_menu import start_menu
from menus.main_menu import main_menu

console = Console()

def main():
  console.print(
    Panel(
      Align.center("[bold white]Library Management System[/]"),
      title="[bold white]Welcome[/]",
      border_style="bright_magenta",
      box=box.DOUBLE,
      padding=(1,4)
    )
  )
  
  while True: 

    result = start_menu()

    if result is True:
      main_menu()

    elif result == "exit" :
      console.print("\n[bold green]Thank you for using Library Management System! :wave:[/]")
      break
    
        
main()

