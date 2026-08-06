from services.member_service import MemberService


def display_member_menu():
    while True:
        print("\n" + "=" * 30)
        print("    MEMBER MANAGEMENT MENU    ")
        print("=" * 30)
        print("1. Add New Member")
        print("2. View All Members")
        print("3. Search Member by ID")
        print("4. Delete Member")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Add New Member ---")
            name = input("Enter Name: ")
            gender = input("Enter Gender: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            membership_date = input("Enter Membership Date (YYYY-MM-DD): ")

            MemberService.add_member(
                name, gender, phone, email, address, membership_date
            )

        elif choice == "2":
            print("\n--- Registered Members ---")
            members = MemberService.get_all_members()
            if members:
                for member in members:
                    print(member)
            else:
                print("No members found in the database.")

        elif choice == "3":
            member_id = input("\nEnter Member ID to search: ")
            member = MemberService.get_member_by_id(member_id)
            if member:
                print("\nMember Details:")
                print(member)
            else:
                print(f"No member found with ID: {member_id}")

        elif choice == "4":
            member_id = input("\nEnter Member ID to delete: ")
            MemberService.delete_member(member_id)

        elif choice == "5":
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")
        