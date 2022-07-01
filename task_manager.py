# imported modules.
import datetime

# Empty lists to store data.
user_contents = []
user_names = []
user_passwords = []

# Let's user inputs username to login.
user_name = input("Enter username: ").lower()

# Opens 'user.txt' file.
# Appends user names, from 'user.txt' file, to 'user_names' list.
# Appends passwords, from 'user.txt' file, to 'user_passwords' list.
with open('user.txt', 'r+') as ofile_user_contents:

    for line in ofile_user_contents:

        line = line.split(", ")
        user_names.append(line[0])
        user_passwords.append(line[1].strip())
        
# Validates entered user name.
while user_name not in user_names:
    user_name = input("Enter a valid user name: ")
else:
    # Gets 'user_name' index.
    # Asks user to enter password.
    i = user_names.index(user_name)
    user_password = input("Enter password: ").lower()

    # Validates user's password.
    while user_password != user_passwords[i]:
        user_password = input(
                "Enter a valid password: ").lower()
    else:
        print(f"\nWelcome back {user_name}! \n")        

while True:

    # Menu for user's that are not admin.
    if user_name != "admin":
    
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
    
    else:

        # Admin's menu.
            menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - generate reports
    ds - Dispaly statistics
    e - Exit
    : ''').lower() 


    # Let's admin register a new user. 
    def reg_user(menu):
        
        user_contents = ""
        ofile_user_contents = open('user.txt', 'r+')

        for line in ofile_user_contents:
            user_contents += line
            
        if menu == "r" and user_name == "admin":
            new_user_name = input("Enter user name: ").lower()

            # Checks if username already exists.
            while new_user_name in user_contents:

                print("User already exist.")
                new_user_name = input("Enter user name: ").lower()
            else: 
                new_password = input("Enter new password: ").lower()
                confirm_password = input("Confirm password: ").lower()

            # Checks if 'new_password' matches 'confirm_password'.
            # Stores registered user's information in 'user.txt' file.
            if confirm_password == new_password:
                ofile_user_contents.write(f"\n{new_user_name}, {new_password}")
                ofile_user_contents.close()   

            else:
                # Let's user set password again, when passwords don't match.
                while confirm_password != new_password:
                    print("Passwords don't match")
                    new_password = input("Enter new password: ").lower()
                    confirm_password = input("Confirm password: ").lower()
                    
                else:
                    
                    # Checks if 'new_password' matches 'confirm_password'.
                    # Stores registered user's information in 'user.txt' file.      
                    ofile_user_contents = open('user.txt', 'a')
                    ofile_user_contents.write(f"\n{new_user_name}, {new_password}")
                    ofile_user_contents.close()

            # New user welcome message.       
            print(f"\nNew account created! Welcome {new_user_name}. \n")

    # Lets admin generate user and task
    # statistics when "gr" is selected.
    def reports(menu):

        if menu == "gr" and user_name == "admin":

            # Opens 'task.txt' and user.txt' files.
            with open(
                'tasks.txt', 'r') as ofile_tasks_contents, open(
                    'user.txt', 'r') as ofile_user_contents:

                tasks_contents, user_contents = ofile_tasks_contents.readlines(), ofile_user_contents.readlines()

            # Opens 'task_overview.txt' and 'user_overview.txt' files.
            with open(
                'task_overview.txt', 'w') as task_overview, open(
                    'user_overview.txt', 'w') as user_overview:

                # Counters
                number_of_tasks = 0
                completed_tasks = 0
                uncompleted_tasks = 0  
                overdue_tasks = 0 
                uncompleted_overdue = 0
                
                # Splits each line in 'task_contents' file, to a list,
                # converts 'due_date' string to datetime data type,
                # increaments 'number_of_tasks' by 1.
                for line in tasks_contents:

                    line = line.split(", ")
                    due_date = datetime.datetime.strptime(line[4], "%d %b %Y") 
                    number_of_tasks += 1

                    # Increaments respective counter, by 1,
                    # when the condition is met.
                    if line[-1] == "Yes ":
                        completed_tasks += 1

                    if line[-1] != "Yes ":
                        uncompleted_tasks += 1

                    if due_date < datetime.datetime.today():
                        overdue_tasks += 1

                    if (due_date < datetime.datetime.today()) and (line[4] != "Yes "):
                        uncompleted_overdue += 1
                
                # Writes data to 'task_overview' file.
                task_overview.write("OVERALL REPORTS.\n")
                task_overview.write(f"Total number of tasks: {number_of_tasks}\n")  
                task_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                task_overview.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
                task_overview.write(f"Total number of uncompleted and overdue tasks: {(uncompleted_overdue)}\n") 
                task_overview.write(f"Percentage of incomplete tasks: {round(((uncompleted_tasks/number_of_tasks)*100),2)}%\n")
                task_overview.write(f"Percentage of overdue tasks: {round(((overdue_tasks/number_of_tasks)*100),2)}%\n")

                # Counters and lists.
                registered_users = 0                
                user_name_list = []

                # Splits each line in 'user_contents' file, to a list,
                # Appends each item at line, index 0, to 'user_name_list' list.
                # increaments 'registered_users' counter by 1.
                for line in user_contents:   
                    line = line.split(", ")
                    user_name_list.append(line[0])
                    registered_users += 1   
                   
                # Loops through 'user_name_list' list.
                for user in user_name_list:
                    # Counters and lists.
                    number_of_tasks = 0
                    user_task_list = []

                    # Loops through 'task_contents' file.
                    # Increaments 'number_of_tasks' by 1
                    for task in tasks_contents:
                        task = task.split(", ")
                        number_of_tasks += 1

                        # Adds user to user_task_list.
                        if user == task[0]:
                            user_task_list.append(task)

                            #Counters
                            user_uncompleted_overdue = 0
                            user_overdue_tasks = 0
                            completed_user_tasks = 0
                            uncompleted_user_tasks = 0
                            
                            # Increaments respective counters, by 1,
                            # when the condition is met.
                            for task_in_list in user_task_list:
                                if task_in_list[-1] == "Yes ":
                                    completed_user_tasks += 1

                                if task_in_list[-1] != "Yes ":
                                    uncompleted_user_tasks += 1

                                user_due_date = datetime.datetime.strptime(task_in_list[4], "%d %b %Y") 
                                if user_due_date < datetime.datetime.today():
                                    user_overdue_tasks += 1

                                if (user_due_date < datetime.datetime.today()) and (task_in_list[-1] != "Yes "):
                                    user_uncompleted_overdue += 1
                                    
                    # Writes to 'user_overview' file.
                    user_overview.write("\nUser: " + user + "\n")
                    user_overview.write(f"Percentange of total number tasks assigned: {round(((len(user_task_list)/number_of_tasks)*100),2)}%\n")                           
                    user_overview.write(f"Percentage of tasks completed: {round(((completed_user_tasks/len(user_task_list))*100),2)}%\n")
                    user_overview.write(f"Percentage of tasks that must be completed: {round(((uncompleted_user_tasks/len(user_task_list))*100),2)}%\n")
                    user_overview.write(f"Percentage of tasks overdue and uncompleted: {round(((user_uncompleted_overdue/len(user_task_list))*100),2)}%\n")

                # Writes to 'user_overview' file.
                user_overview.write("\nOVERALL REPORTS.\n")
                user_overview.write(f"Total number of registered users: {registered_users}\n")  
                user_overview.write(f"Total number of tasks: {number_of_tasks}\n")  
                user_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                user_overview.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
                user_overview.write(f"Total number of uncompleted and overdue tasks: {(uncompleted_overdue)}\n") 
                user_overview.write(f"Percentage of incomplete tasks: {round(((uncompleted_tasks/number_of_tasks)*100),2)}%\n")
                user_overview.write(f"Percentage of overdue tasks: {round(((overdue_tasks/number_of_tasks)*100),2)}%\n")

                print("\nReports Generated!\n")

    def display_stats(menu):

        if menu == "ds" and user_name == "admin":

            print("\nUSER REPORTS.\n")

            # Opens 'tasks.txt' and 'user.txt' files,
            # when admin selects 'ds'.
            with open(
                'tasks.txt', 'r') as ofile_tasks_contents, open(
                    'user.txt', 'r') as ofile_user_contents:

                tasks_contents, user_contents = ofile_tasks_contents.readlines(), ofile_user_contents.readlines()

                # Counters
                number_of_tasks = 0
                completed_tasks = 0
                uncompleted_tasks = 0  
                overdue_tasks = 0 
                uncompleted_overdue = 0
                
                # Splits each line in 'task_contents' file, to a list,
                # converts 'due_date' string to datetime data type,
                # increaments 'number_of_tasks' by 1.
                for line in tasks_contents:

                    line = line.split(", ")
                    due_date = datetime.datetime.strptime(line[4], "%d %b %Y") 
                    number_of_tasks += 1

                    # Increaments respective counter, by 1,
                    # when the condition is met.
                    if line[-1] == "Yes ":
                        completed_tasks += 1

                    if line[-1] != "Yes ":
                        uncompleted_tasks += 1

                    if due_date < datetime.datetime.today():
                        overdue_tasks += 1

                    if (due_date < datetime.datetime.today()) and (line[4] != "Yes "):
                        uncompleted_overdue += 1

                # Counters and lists.
                registered_users = 0                
                user_name_list = []

                # Splits each line in 'user_contents' file, to a list,
                # Appends each item at line, index 0, to 'user_name_list' list.
                # increaments 'registered_users' counter by 1.
                for line in user_contents:
                    line = line.split(", ")
                    user_name_list.append(line[0])
                    registered_users += 1   
                   
                # Loops through 'user_name_list' list.
                for user in user_name_list:
                    # Counters ans empty lists
                    number_of_tasks = 0
                    user_task_list = []

                    # Loops through 'task_contents' file.
                    # Increaments 'number_of_tasks' by 1
                    for task in tasks_contents:
                        task = task.split(", ")
                        number_of_tasks += 1

                        # Adds user to user_task_list.# Adds user to user_task_list.
                        if user == task[0]:
                            user_task_list.append(task)

                            # Counters.
                            user_uncompleted_overdue = 0
                            user_overdue_tasks = 0
                            completed_user_tasks = 0
                            uncompleted_user_tasks = 0
                            
                            # Increaments respective counters, by 1,
                            # when the condition is met.
                            for task_in_list in user_task_list:
                                if task_in_list[-1] == "Yes ":
                                    completed_user_tasks += 1

                                if task_in_list[-1] != "Yes ":
                                    uncompleted_user_tasks += 1

                                user_due_date = datetime.datetime.strptime(task_in_list[4], "%d %b %Y") 
                                if user_due_date < datetime.datetime.today():
                                    user_overdue_tasks += 1

                                if (user_due_date < datetime.datetime.today()) and (task_in_list[-1] != "Yes "):
                                    user_uncompleted_overdue += 1
                    # Displays user reports.
                    print("User: " + user + "\n")
                    print(f"Percentange of total number tasks assigned: {round(((len(user_task_list)/number_of_tasks)*100),2)}%")                           
                    print(f"Percentage of tasks completed: {round(((completed_user_tasks/len(user_task_list))*100),2)}%")
                    print(f"Percentage of tasks that must be completed: {round(((uncompleted_user_tasks/len(user_task_list))*100),2)}%")
                    print(f"Percentage of tasks overdue and uncompleted: {round(((user_uncompleted_overdue/len(user_task_list))*100),2)}%\n")
                
                # Displays overall reports.  
                print("OVERALL REPORTS.\n")
                print(f"Total number of registered users: {registered_users}")  
                print(f"Total number of tasks: {number_of_tasks}")  
                print(f"Total number of completed tasks: {completed_tasks}")
                print(f"Total number of uncompleted tasks: {uncompleted_tasks}")
                print(f"Total number of uncompleted and overdue tasks: {(uncompleted_overdue)}") 
                print(f"Percentage of incomplete tasks: {round(((uncompleted_tasks/number_of_tasks)*100),2)}%")
                print(f"Percentage of overdue tasks: {round(((overdue_tasks/number_of_tasks)*100),2)}%\n")

    # Lets user fill in task information,
    # when user selects 'a'. 
    def add_task(menu):

        if menu == "a":
            # User's input
            task_assigned_to = input("Task assigned to? ")
            task_title = input("Task title: ")
            task_description = input("Task description: ")
            current_date = datetime.datetime.today()
            current_date_format = current_date.strftime("%d %b %Y")
            task_due_date =input("Due date(exp. 28 Jan 2022): ")
            complition_status = "No"
            task_contents = (f'''{task_assigned_to}, {task_title}, {task_description}, {current_date_format}, {task_due_date}, {complition_status}''')

            # Opens 'tasks.txt file.
            # Adds user's task to 'tasks.txt file.
            # Closes file.
            ofile_task_contents = open('tasks.txt', 'a')
            ofile_task_contents.write(f"\n{task_contents}")
            ofile_task_contents.close()
            print("\nTask Added!\n")

    # Opens 'tasks.txt file, when user select 'va'.
    def view_all(menu):

        if menu == 'va':
            
            # Displays all tasks.
            ofile_task_contents = open('tasks.txt', 'r')        
            for line in ofile_task_contents:
                
                line = line.split(",")
            
                print(f'''
                    Task             :{line[1]}
                    Task Description :{line[2]}
                    Assigned to      :{line[0]}
                    Date Assigned    :{line[3]}
                    Due Date         :{line[4]}
                    Task complete?    {line[-1]}''')
  
    # Displays user's tasks.
    def view_mine(menu):
        
        if menu == "vm":
            
            # Opens 'tasks.txt file, when user select.
            # Reads contents inside the file.
            ofile_task_contents = open('tasks.txt', 'r')
            task_contents = ofile_task_contents.readlines()

            # Counter and empty lists
            task_number = 0
            list_of_user_tasks = []
            list_of_all_tasks = []
            
            while True:                    
                # Adds all tasks in 'tasks.txt' to 'list_of_all_tasks' list.
                for line in task_contents:
                    line = line.split(", ")
                    user = line[0]
                    list_of_all_tasks.append(line)

                    # Appends user's task to 'list_of_user_tasks' and 
                    # Increaments 'task_number' counter, by 1,
                    # when the condition is met.
                    if user == user_name:
                        list_of_user_tasks.append(line)
                        task_number += 1 

                        # Displays user's tasks and task number.
                        task_text = (f'''
                                Task number {task_number}
                        Task             :{line[1]}
                        Task Description :{line[2]}
                        Assigned to      :{line[0]}
                        Date Assigned    :{line[3]}
                        Due Date         :{line[4]}
                        Task complete?    {line[-1]}''')

                        print(task_text)

                # Reserts task_number to 0.
                # user's selects which task to view
                # Or return to main menu.
                task_number = 0
                view_task = int(input('''\nEnter task number to view task or '-1' to return to main menu: ''')) - 1

                # Let's user return to main menu when '-1' is entered.
                if view_task == -2:
                    break

                # Displays the task selected.   
                while view_task:
                    try:
                        selected_task = list_of_user_tasks[view_task]
                        selected_task_text = (f'''
                                Task             :{selected_task[1]}
                                Task Description :{selected_task[2]}
                                Assigned to      :{selected_task[0]}
                                Date Assigned    :{selected_task[3]}
                                Due Date         :{selected_task[4]}
                                Task complete?    {selected_task[-1]}''')
                        print(selected_task_text)
                        break

                    # Error displayed when selected task doesn't exist.
                    except IndexError:
                        print("Task selected doesn't exist.")
                        break

                # Closes file.
                ofile_task_contents.close()

                # Opens file for writing
                ofile_task_contents = open('tasks.txt', 'w')

                # Let's user choose to mark task as complete
                # or edit task.
                if 0 <= view_task <= (len(list_of_user_tasks) - 1):
                    complete_or_edit_task = input(
                        "To mark task as complete enter 'y' or enter 'e' to edit task: ").lower()

                    # Changes task's completion status to "Yes
                    if complete_or_edit_task == "y":
                        selected_task[-1] = "Yes\n"
                
                    # User's input.
                    if complete_or_edit_task == "e":
                        username_or_due_date = input("Enter 'u' to edit username or 'd' to edit due date: ")

                        # Re-assigns task to another user.
                        if username_or_due_date == "u":
                            reassign_task = input("Enter the username to re-assign task to: ")
                            selected_task[0] = reassign_task

                        # Changes task's due date.
                        if username_or_due_date == "d" and selected_task[-1] != "Yes":                           
                            #edit_due_date = datetime.datetime.strptime(input("Enter new due date: "), "%d %b %Y").date()
                            edit_due_date =input("Enter new due date(20 Jan 2000): ")
                            selected_task[-2] = edit_due_date

                # Writes to 'ofile_task_contents' file.
                for lst in list_of_all_tasks:
                    ofile_task_contents.write(", ".join(str(string) for string in lst))
                ofile_task_contents.close()

    # Exits the loop when user selects 'e'.
    def exit_error(menu):

        if menu == 'e':
            print('\nGoodbye!!!\n')
            exit()     

    # Calls the functions.
    reg_user(menu)
    reports(menu)
    display_stats(menu)
    add_task(menu)
    view_mine(menu)
    view_all(menu)
    exit_error(menu)