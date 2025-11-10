"""Module implementing a simple contact management assistant bot."""


def parse_input(user_input):
    """
    Parse user input into command and arguments.
    
    Args:
        user_input (str): The raw user input string.
        
    Returns:
        tuple: A tuple containing the command (str) and arguments (list).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list): List containing [name, phone] of the contact.
        contacts (dict): Dictionary to store contacts.
        
    Returns:
        str: Confirmation message that contact was added.
    """
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Update an existing contact's phone number.
    
    Args:
        args (list): List containing [name, phone] of the contact to update.
        contacts (dict): Dictionary storing contacts.
        
    Returns:
        str: Confirmation message that contact was updated.
    """
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact updated."

def show_phone(args, contacts):
    """
    Retrieve and return a contact's phone number.
    
    Args:
        args (list): List containing the contact name as first element.
        contacts (dict): Dictionary storing contacts.
        
    Returns:
        str: The phone number of the requested contact.
    """
    name = args[0]
    return contacts[name.lower()]

def show_all(contacts):
    """
    Display all contacts in the contacts dictionary.
    
    Args:
        contacts (dict): Dictionary storing all contacts.
        
    Returns:
        str: Formatted string with all contacts, one per line.
    """
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    """
    Main function to run the assistant bot command-line interface.
    
    Handles user input and executes appropriate commands for managing contacts.
    Supports commands: hello, add, change, phone, all, close, exit.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
