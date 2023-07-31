def view_list(task_list):
    print("Current task list:")
    for idx, task in enumerate(task_list, 1):
        status = "completed" if task[1] else "uncompleted"
        print(idx, status, task[0])
def add_task(task_list, task_name):
    task_list.append([task_name, False])
    print(f'Task "{task_name}" added successfully!')
def mark_completed(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        task_list[task_index - 1][1] = True
        print(f'Task "{task_list[task_index - 1][0]}" marked as completed!')
    else:
        print("Error. Wrong task index.")
def delete_task(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        task_name = task_list[task_index - 1][0]
        del task_list[task_index - 1]
        print(f'Task "{task_name}" deleted.')
    else:
        print("Error. Wrong task index.")        
print("Welcome to Task Manager!")
list = []
while True:
    print("\n=== Task Manager ===\n1. View the current task list\n2. Add a new task\n3. Mark a task as completed\n4. Delete a task\n5. Exit")
    selection = input("Choose an action:")
    if selection =='1':
        view_list(list)
    elif selection =='2':
        task_name = input("Enter the task name: ")
        add_task(list, task_name)
    elif selection =='3':
        view_list(list)
        task_index = int(input("Choose a task to mark as completed: "))
        mark_completed(list, task_index)
    elif selection =='4':
        view_list(list)
        task_index = int(input("Choose a task to delete: "))
        delete_task(list, task_index)
    elif selection == '5':
        print("The exit was successful. Have a nice day!")
        break
    else:
        print("Erron. Select a valid action.")