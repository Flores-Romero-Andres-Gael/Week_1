from operator import index
from Task import Task

class TaskManager:

    def __init__(self):
        """
        Constructor for the Task Manager class.
        Initializes an empty list to store tasks.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the list
        :param task: (str) The task description.
        """
        task = Task(task) # Create a new task object
        self.tasks.append(task) # Add the task object to the list.

    def view_tasks(self):
        """
        Displays all tasks in the list with their corresponding index.
        If there are no tasks, display an empty list.
        :return:
        """
        if not self.tasks:
            print('Not tasks aviables.')
        else:
            for i, task in enumerate(self.tasks):
                print(f'Task {i + 1}. {task}') # Show index starting from 1

    def complete_task(self, index):
        """
        Marks a task as completed by its index.
        :param index: (in) The index of the task.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f'Task {index + 1} is completed.')
        else:
            print('Error task, invalid number.')

    def delete_task(self, index):
        """
        Deletes a taks by its index.
        :param index: (int) The index of the task.
        """
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index) # Remove and return the task
            print(f'Task {index + 1} is deleted: {removed}')
        else:
            print('Error task, invalid number.')
