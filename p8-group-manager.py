group_list = [
                {'group': "Songs"}, 
                {'group': "mp3"}
            ]

# group_list = {
#                     'Songs': { 
#                         '_fields_': ['title','artists'],
#                         '_data_': 
#                             [
#                                 {'title': 'Believer', 'artist': 'Imagine Dragons'},
#                                 {'title': 'Natural', 'artists': 'Imagine Dragons'}
#                             ],
#                     },
#             },

                
def welcome_msg():
    print("\n\n")
    welcome_msg_2="This program creates groups with dynamic properties"
    print("=" * len(welcome_msg_2))
    print("\t>> Welccome to Group Manager <<")
    print(welcome_msg_2)
    print("=" * len(welcome_msg_2))
    
def display_menu():
    print("?: list commands")
    print("C: Create a new group")
    print("A: Add data to a group")
    print("G: List groups")
    print("L: List data for a group")
    print("X: Exit")

def find_group(d, group_name):
    # If a group name is entered, validate the group doesn't already exist.
    does_group_exist = False
    for key in d:
        # If the group does exist, print a warning and re-prompt
        if key.lower() == group_name.lower():
            does_group_exist = True
            break
    return does_group_exist


def create_group(d):
    print("** Create new group **")

    while True:

        does_group_exist = True
        while does_group_exist:

            group_name = input("\nEnter group name (empty to cancel): ").strip()

            # If nothing is entered, exit the Create New Group.
            if len(group_name) == 0:
                return

            # If a group name is entered, validate the group doesn't already exist.
            does_group_exist = find_group(d, group_name)

            if does_group_exist:
                print("[WARNING] Group already exists")

            # If does_group_exist is False, the inner while loop will end.


        # If the group doesn't exist, prompt for property names
        # This portion of the code still needs to be inside of the outer while loop because
        # the directions indicate a "group name" re-prompt after entering the field names
        field_names = []
        while True:
            field_name = input("Enter field name (empty to stop): ").strip()
            if len(field_name) > 0:
                if field_name in field_names:
                    print("[WARNING] Field already exists")
                else:
                    field_names.append(field_name)
            else:
                break

        # When nothing is entered, save the group and the properties for that group    
        d[group_name] = {"_fields_": field_names, "_data_": []}
            
def list_groups(d):
    print("** List of groups **")

    if len(d) == 0:
        print("No groups found\n")
    else:
        # Display a sorted list of groups
        sorted_group_names = list(d.keys())
        sorted_group_names.sort()
        
        for group_name in sorted_group_names:

            # Display the group name
            display_text = group_name

            # Display the number of properties
            properties = d[group_name]["_fields_"]
            number_of_properties = len(properties)

            # Display a comma-delimited list of property names
            all_the_properties = (", ".join(properties)).strip()

            # All together
            display_text += " : " + str(number_of_properties) + " properties"
            display_text += " (" + all_the_properties + ")"

            print(display_text)
        
def add_group_data(d):
    print("** Add group data **")

    # Display sorted list of groups (tip: call the list_groups() function)
    list_groups(d)

    while True:
        
        does_group_exist =  False
        group_name = ""

        # Prompt for a group name
        while not does_group_exist:
            group_name = input("\nEnter group (empty to cancel): ").strip()

            # When nothing is entered, leave the Add Group Data command
            if len(group_name) == 0:
                return

            # If a group name is entered, validate the group exists
            does_group_exist = find_group(d, group_name)

            # If the group doesn't exist, display an error and re-prompt
            if not does_group_exist:
                print("[ERROR] Group does not exist")

            # If does_group_exist is True, the inner while loop will end, otherwise, it will reprompt

        # If the group does exist, prompt for input for each of the group properties
        entry = {}
        for field in d[group_name]["_fields_"]:
            data_for_field = input("Enter " + field + ": ").strip()
            entry[field] = data_for_field

        # Save the properties for the group
        d[group_name]["_data_"].append(entry)


def list_group_data(d):
    print("** List group data")

    # Display sorted list of groups (tip: call the list_groups() function)
    list_groups(d)

    while True:

        does_group_exist = False
        group_name = ""

        # Prompt for a group name
        while not does_group_exist:

            group_name = input("\nEnter group name (empty to cancel): ").strip()

            # When nothing is entered, leave the List Data for Group command
            if len(group_name) == 0:
                return

            # If a group name is entered, validate the group exists
            does_group_exist = find_group(d, group_name)

            # If the group doesn't exist, display an error and re-prompt
            if not does_group_exist:
                print("[ERROR] Group does not exist")

            # If does_group_exist is True, the inner while loop will end, otherwise, it will reprompt


        # If the group does exist, display a line for each stored group properties displaying the property and the property value
        counter = 0
        for entry in d[group_name]["_data_"]:
            entry_array = []
            for field in d[group_name]["_fields_"]:
                value = entry[field]
                entry_array.append(field + " = " + value)

            print(str(counter) + " " + (", ".join(entry_array)).strip())
            counter+=1

def main():
    welcome_msg()

    d = {}
    while True:
        cmd = input("\nCommand (empty or X to quit, ? for help): ")
        if cmd == "?":
            display_menu()
        elif cmd.upper().strip() == "C":
            create_group(d)            
        elif cmd.upper().strip() == "A":
            add_group_data(d)
        elif cmd.upper().strip() == "G":
            list_groups(d)
        elif cmd.upper().strip() == "L":
            list_group_data(d)
        elif cmd.upper().strip() == "X" or len(cmd) == 0:
            exit()
        else:
            print("Command not recognized, please try again.")



#run the main program
if __name__ == "__main__":
    main()