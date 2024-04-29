task_list = []  # empty list for tasks

def Task_add(task_list):
    tasks_count = int(input("HOW MANY TASKS YOU WANT TO ADD: "))  # inputs the number of tasks
    for i in range(tasks_count):
        task = input(f"Task {i+1}: ")  # input task one by one
        task_list.append(task)  # adds task to the list

def Task_display(task_list):
    print("Task List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")  # prints the list of tasks

def Task_mark(task_list):
    completed = 0 # counter for tasks
    task_indices = input("Enter the indices of tasks you want to mark as done (separated by commas): ").split(',')
    for index in task_indices: # loop to iterate through the task indexes 
        task_index = int(index.strip()) - 1 # removes spaces in the task index
        if 0 <= task_index < len(task_list):  # check for valid task index
            task_list[task_index] += " - Completed"  # adds " - Completed" to the task specified by user
            completed += 1  # increases the counter of completed tasks
        else:
            print(f"Invalid Task Index {index}")
        
    print("Tasks Marked As Done")

def Task_remove(task_list):
    task_indices = input("Enter the indices of tasks you want to remove (separated by commas): ").split(',')
    removed_indices = []
    for index in task_indices: # loop to iterate through indexes
        task_index = int(index.strip()) - 1 # removes whitespaces 
        if 0 <= task_index < len(task_list):  # check for valid task index
            removed_indices.append(index)  
        else:
            print(f"Invalid Task Index {index}")
            print("Current task list length:", len(task_list))

    if removed_indices:  # If there are tasks to remove
        print(f"Tasks to be removed: {', '.join(removed_indices)}")
        confirm = input("Do you want to remove these tasks? (yes/no): ").lower()
        if confirm == 'yes':
            for index in removed_indices:
                del task_list[int(index.strip()) - 1]  # deletes the task of the specified task index
            print("Tasks Removed From the List")
        else:
            print("Tasks removal cancelled.")
    else:
        print("No tasks to remove.")


#calling the functions in order . 
def TodoList():
    Task_add(task_list)
    Task_display(task_list)
    Task_mark(task_list)
    Task_remove(task_list)
    Task_display(task_list)
    
    #calling the to do list 
TodoList()
