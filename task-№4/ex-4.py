def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Invalid input. Please try again."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return wrapper

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Not enough arguments.")
    
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def get_phone(args, kwargs):
    if not args:
        raise IndexError("No arguments provided.")
    
    if args[0] in contacts:
        return contacts[args[0]]
    
    raise KeyError("This contact does not exist.")

@input_error
def show_all(contacts):
        if not contacts:
            return "No contacts saved yet."
    
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("enter a command: ")
        command, *args = parse_input(user_input)
        # command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit", "bye", "-"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "+":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(args, contacts)
        elif command == "all":
            print(args, contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()