"""Module implementing a simple contact management assistant bot."""


def input_error(func):
    """
    Decorator to handle input errors in contact management functions.
    
    Handles KeyError, ValueError, and IndexError exceptions and returns
    appropriate user-friendly error messages.
    
    Args:
        func: The function to be decorated.
        
    Returns:
        function: The wrapped function with error handling.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
    return inner


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

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    
    Args:
        args (list): List containing [name, phone] of the contact.
        contacts (dict): Dictionary to store contacts.
        
    Returns:
        str: Confirmation message that contact was added.
    """
    name = args[0]
    phone = args[1]

    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Update an existing contact's phone number.
    
    Args:
        args (list): List containing [name, phone] of the contact to update.
        contacts (dict): Dictionary storing contacts.
        
    Returns:
        str: Confirmation message that contact was updated.
    """
    name = args[0]
    phone = args[1]

    contacts[name.lower()] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """
    Retrieve and return a contact's phone number.
    
    (Ця функція вже коректна, залишаємо без змін)
    
    Args:
        args (list): List containing the contact name as first element.
        contacts (dict): Dictionary storing contacts.
        
    Returns:
        str: The phone number of the requested contact.
    """
    name = args[0]
    return contacts[name.lower()]

@input_error
def show_all(contacts):
    """
    Display all contacts in the contacts dictionary.
    
    Args:
        contacts (dict): Dictionary storing all contacts.
        
    Returns:
        str: Formatted string with all contacts, one per line.
    """
    if not contacts:
        return "No contacts found."
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
        if not user_input.strip():
            continue

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
