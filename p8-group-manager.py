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
    welcome_msg_2="This program creates groups with dynamic properties"
    print("\t>> Welccome to Group Manager <<")
    print(welcome_msg_2)
    print("=" * len(welcome_msg_2))
    
def display_menu():
    print("?: list commands")
    print("C: Create a new group")
    print("L: List group")
    print("A: Add data to a group")
    print("L: List data for a group")
    print("X: Exit\n")

def find_group(group_name):
    # if len(group_name.strip()) > 0:
    for grp in group_list:
        if grp['group'] == group_name.strip():
            print("Group already found, you will need a new group name")
            return True # Found
        else: 
            return False # Not found 
    
def create_group():
    group_name = input("Enter a group name (empty to cancel): ")
    if len(group_name) == 0:
        print("Need a name for your group.")
        return
    resp = find_group(group_name)
    if resp == False:  # Not found
        print("Creating new group...: ", group_name.strip())
        new_group = {}
        new_group["group"] = group_name
        group_list.append(new_group)
        print("New group added: ", group_name.strip())
            
def list_groups():
    if len(group_list) == 0:
        print("No groups found\n")
    else:
        i = 1
        for grp in group_list:
            print(str(i) + ". " + grp["group"]) # + " (" + str(grp[1]) + ")")
            i += 1
        print()
        
def add_group_data():
    pass

def list_group_data():
    pass

def main():
    welcome_msg()
    display_menu()
    
    while True:
        cmd = input("Command (empty or C to quit, ? for help): ")
        if cmd == "?":
            display_menu()
        elif cmd.upper().strip() == "C":
            create_group()            
        elif cmd.upper().strip() == "L":
            list_groups()
        elif cmd.upper().strip() == "A":
            pass
        elif cmd.upper().strip() == "L":
            pass
        elif cmd.upper().strip() == "X" or len(cmd) == 0:
            exit()            

#run the main program
if __name__ == "__main__":
    main()