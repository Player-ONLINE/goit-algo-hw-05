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
def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

@input_error
def add_contact(args, contacts):
    name, phone = args  
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    return contacts[args[0]]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    raise KeyError("This contact does not exist.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "-"]:
            print("Good bye!")
            break
        elif command in ["hello", "+"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

# Виходе, помилка була в тому, що я просто не поставив ось цю "*" і все ? 