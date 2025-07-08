from TaskManager import TaskManager

def menu():
    """
    Display the menu options
    """
    manager = TaskManager()

    try:
        while True:
            print('\n----------Menu Tasks----------')
            print('1. Add Task.')
            print('2. View all tasks.')
            print('3. Mark a Task to completed.')
            print('4. Delete Task.')
            print('0. Exit.')
            op = input('Select an option: ')
            if op == '1':
                description = input('Enter task description: ')
                manager.add_task(description)
                print(f'Task Description: {description} \n added successfully!')
                input('Press to continue...')
            elif op == '2':
                print('\n----------All Tasks----------')
                manager.view_tasks()
                input('Press to continue...')
            elif op == '3':
                while True:
                    try:
                        print('\n----------Tasks----------')
                        manager.view_tasks()
                        index = int(input('\nEnter the task number to mark as completed: ')) - 1
                        manager.complete_task(index)
                        input('Press to continue...')
                        break
                    except ValueError:
                        print('Invalid input. Please try again.')
            elif op == '4':
                while True:
                    try:
                        index = int(input('Enter the task number to delete: ')) - 1
                        manager.delete_task(index)
                        input('Press to continue...')
                        break
                    except ValueError:
                        print('Invalid input. Please try again.')
            elif op == '0':
                print('Goodbye!')
                break
    except ValueError:
        print('Invalid input. Please try again.')