print("Hello")
print("Create List Here")
#padding functions
def pad_string(value):
    x = value * 10
    return x

def pad_left(input_str, integer):
    i = 0
    while i < integer:
        input_str = " " + input_str
        i += 1
    return input_str

def pad_right(input_str, size):
    i = 0
    while len(input_str) < size:
        input_str += " "
        i += 1
    return input_str

#coommand functions
def cmd_help(commands, descriptions):
    print("*** Available commands ***")
    for command, description in zip(commands, descriptions):
        padded_command = pad_right(command, get_max_list_item_size(commands))
        print(f"{padded_command}     {description}")
    print("Empty to exit")

def cmd_add(t):
    while True:
        data = input("Enter data to add (empty to stop adding): ")
        if not data:
            break
        t.append(data)
        print(f"Data '{data}' added. Total items: {len(t)}")

def cmd_delete(t):
    if not t:
        print("List is empty. Nothing to delete.")
        return
    #implement deleting items from list
    while True:
        print("List items:")
        for i, item in enumerate(t, 1):
            print(f"{i}: {item}")

        index_input = input("Enter index to delete (empty to stop deleting): ").strip()

        if not index_input:
            break
        #use boolean expression here
        if index_input.isdigit():
            index = int(index_input) - 1
            if 0 <= index < len(t):
                deleted_item = t.pop(index)
                print(f"Deleted item: {deleted_item}. Total items: {len(t)}")
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid index.")

def cmd_list(t):
    if not t:
        print("List is empty.")
    else:
        print("List items:")
        for i, item in enumerate(t, 1):
            print(f"{i}: {item}")

def cmd_clear(t):
    t.clear()
    print("All items have been cleared. List is empty.")

def get_max_list_item_size(commands):
    max_length = 0
    for command in commands:
        if len(command) > max_length:
            max_length = len(command)
    return max_length

# main program
def main():
    # list variable to hold list items
    my_list = []

    # separate lists for commands and descriptions
    commands = [
        "add",
        "delete",
        "list",
        "clear",
    ]
    descriptions = [
        "Add to list",
        "Delete information",
        "List information",
        "Clear list",
    ]

    #primary input loop
    while True:
        command = input("Enter a command (? for help): ").strip()

        #exit the program if Enter key is pressed with no input
        if not command:  
            print("Goodbye!")
            break

        if command == '?':
            cmd_help(commands, descriptions)
        elif command == 'add':
            cmd_add(my_list)
        elif command == 'delete':
            cmd_delete(my_list)
        elif command == 'list':
            cmd_list(my_list)
        elif command == 'clear':
            cmd_clear(my_list)
        else:
            print("Invalid command. Type '?' for help.")

#run the main program
if __name__ == "__main__":
    main()