from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found."
        except IndexError:
            return "Not found."
        except Exception as e:
            return f"Error : {e}"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args   
    if args[0] in contacts.keys():
        contacts[name] = phone
        return "Contact update."
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def show_phone(args, contacts):
    return contacts[args[0]]  
   

@input_error    
def show_all(args, contacts):
    s = ''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]:10}\n")
    return s

@input_error    
def main():
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
        elif command  == "add":
            print(add_contact(args, contacts))
        elif command  == "change":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
