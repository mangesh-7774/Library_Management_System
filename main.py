from menus.start_menu import start_menu
from menus.main_menu import main_menu

def main():
  print("\n" + "=" * 30 + " Library Management System " + "=" * 30 + "\n")
  
  while True: 
    if start_menu():
      main_menu()
    elif start_menu() == False :
      break
    else:
      print("\nInvalid username or password")

      choice = input("\nTry Again? (y/n) : ").lower()

      if choice != "y" : 
        print("\nExit system")
        break
        
main()
