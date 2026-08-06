from auth.login import login
from menus.main_menu import main_menu

def main():
  print("\n" + "=" * 30 + "Library Management System" + "=" * 30)
  
  while True: 
    if login():
      main_menu()
    else:
      print("\nInvalid username or password")

      choice = input("\nTry Again? (y/n) : ").lower()

      if choice != "y" : 
        print("Exit system")
        break
        
main()
