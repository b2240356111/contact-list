def run_manager(all_contacts):
    #this fuction is the main menu, it helps user to choose which thing they want to do
    while True:
        print("========================================")
        print("SIMPLE CONTACT MANAGER MENU")
        print("========================================")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("----------------------------------------")

        choice = input("Enter your choice 1-5:").strip()
        if choice == "":
            print("Invalid input. Please enter a number")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
            print("Invalid input. Please enter a number between 1 and 5")
        if choice == "1":
            result = new_contact(all_contacts)

            if result is not None:
                all_contacts = result
        elif choice == "2":
            view_contacts(all_contacts)
        elif choice == "3":
            edit_contact(all_contacts)
        elif choice == "4":
            delete_contact(all_contacts)
        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break

def new_contact(all_contacts):
    #this function creates a new contact with the inputs taken from user. It appends the information taken from user to a list
    print("--- ADD NEW CONTACT (Type ’cancel’ to return to menu)---")
    new_name = input("Enter the contacts name: ").strip()
    #invalid inputs are checked
    if new_name == "cancel":
        print("Operation cancelled. Returning to main menu.")
        return
    if new_name == "":
        print("Invalid input. Please enter a name")
        return

    while True:
        #this while loop checks if the phone number is 11 digits or not
        new_phonenumber = input("Enter the contacts phone number: ").strip()
        if new_phonenumber == "cancel":
            print("Operation cancelled. returning to main menu.")
            return
        if new_phonenumber == "":
            print("Phone number can not be empty.")
            return

        elif len(new_phonenumber) != 11 or not new_phonenumber.isdigit():
            print("Phone numbers must contain only 11 digits")
        else:
            break

    email = input("Enter the contacts email: ").strip()
    if email == "cancel":
        print("Operation cancelled. returning to main menu.")
        return
    if email == "":
        print("Email address can't be empty")
        return
    country = input("Enter the contacts country: ").strip()
    if country == "cancel":
        print("Operation cancelled. returning to main menu.")
        return
    if country == "":
        print("Country can not be empty.")
        return

    print(f"Success, contact {new_name} added.\n")
    contact = {
        "name": new_name,
        "phone_number": new_phonenumber,
        "email": email,
        "country": country,
    }
    all_contacts.append(contact)
    return all_contacts

def view_contacts(all_contacts):
    #this function prints the contacts information from dictionary
    if len(all_contacts) == 0:
        print("The contact list is currently empty.\n")
        return
    print("============================================================================")
    print("Index | Name            | Phone           | Email           | Country        ")
    print("============================================================================")
    i = 1
    for contact in all_contacts:
        name = contact["name"]
        phone_number = contact["phone_number"]
        email = contact["email"]
        country = contact["country"]
        print(f"{i:5} |{name:15} |{phone_number:15} |{email:15} |{country:15}|")
        i += 1
    print("----------------------------------------------------------------------------\n")

def edit_contact(all_contacts):
    print("----EDIT CONTACT----")
    selected_contact = select_contact(all_contacts, "edit")
    if not selected_contact:
        return
    index, contact = selected_contact

    print(f"Editing contact: {contact['name']}")
    print("Which field do you want to change?")
    print(f"1: Name (Current: {contact['name']})")
    print(f"2: Phone number (Current: {contact['phone_number']})")
    print(f"3: Email (Current: {contact['email']})")
    print(f"4: Country (Current: {contact['country']})")
    choosen_number2 = input("Enter choice(1-4): ").strip()
    if choosen_number2 == "cancel":
        print("Operation cancelled. Returning to main menu.\n")
        return
    choosen_number2 = int(choosen_number2)
    if choosen_number2 == 1:
        new_value = input("Enter the new name: ").strip()
        if new_value == "cancel":
            print("Operation cancelled. Returning to main menu.\n")
            return
        if new_value == "":
            print("Name can not be empty. Operation cancelled.\n")
            return
        all_contacts[index]['name'] = new_value
        print(f"Success! You have updated name for {all_contacts[index]['name']}")
    elif choosen_number2 == 2:
        new_value = input("Enter the new phone number: ").strip()
        if new_value == "cancel":
            print("Operation cancelled. Returning to main menu.\n")
            return
        if new_value == "":
            print("Phone number can not be empty. Operation cancelled.\n")
            return
        all_contacts[index]['phone_number'] = new_value
        print(f"Success! You have updated number for {all_contacts[index]['phone_number']}")
    elif choosen_number2 == 3:
        new_value = input("Enter the new email: ").strip()
        if new_value == "cancel":
            print("Operation cancelled. Returning to main menu.\n")
            return
        if new_value == "":
            print("Email can not be empty. Operation cancelled.\n")
            return
        all_contacts[index]['email'] = new_value
        print(f"Success! You have updated email for {all_contacts[index]['email']}")
    elif choosen_number2 == 4:
        new_value = input("Enter the new country: ").strip()
        if new_value == "cancel":
            print("Operation cancelled. Returning to main menu.\n")
            return
        if new_value == "":
            print("Country can not be empty. Operation cancelled.\n")
            return
        all_contacts[index]['country'] = new_value
        print(f"Success! You have updated country for {all_contacts[index]['country']}")
    else:
        print("Invalid choice")

def delete_contact(all_contacts):
    print("----DELETE CONTACT----")
    print("write 'cancel' to return to menu")

    gone_contact = select_contact(all_contacts, "delete")

    if not gone_contact:
        return

    index, contact = gone_contact # it seperates the tuple into two pieces
    answer = input(f"Are you sure you want to delete {contact['name']}? ").strip()
    if answer == "yes":
        deleted = all_contacts.pop(index)
        print(f"Successfully deleted {deleted['name']}")
    elif answer == "no":
        print("Returning to main menu")

def select_contact(all_contacts, operation_type):
    name = input(f"Enter the name (or part of the name) of the contact to {operation_type}: ").strip()
    found_contacts = []
    if name == "cancel" or name == "":
        print("Operation cancelled. Returning to main menu.\n")
        return

    for i in range(0, len(all_contacts)):
        if all_contacts[i]['name'] == name:
            information = (i, all_contacts[i])
            found_contacts.append(information)
    if len(found_contacts) == 0:
        print(f"No contacts found matching '{name}'.\n")
        return
    if len(found_contacts) == 1:
        choosen_number = 1
    else:
        a = 0
        print("Contacts are found.")
        for i in range(1, len(found_contacts) + 1):
            contact = found_contacts[a][1]
            print(f"{i:5} | {contact['name']} ({contact['phone_number']})")
            a += 1
        choosen_number = int(input(f"Enter number of contact to {operation_type}, or type 0 to cancel:").strip())
    if choosen_number == 0:
        print("Operation cancelled. Returning to main menu.\n")
        return
    if choosen_number < 1 or choosen_number > len(found_contacts):
        print("You have entered an invalid number")
        return
    return found_contacts[choosen_number-1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        try:
            sys.stdin = open(input_file_path, 'r')
        except FileNotFoundError:
            sys.exit(1)
    contacts_list  = []
    run_manager(contacts_list)
    if len(sys.argv) > 1:
        sys.stdin.close()
