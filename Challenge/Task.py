
class Task:

    def __init__(self, task):
        """
        Constructor for the Task class.
        :param task: (str) The description of the task.
        """
        self.task = task # Store the task description
        self.completed = False # Marks the task is completed (default is False)

    def mark_complete(self):
        """
        Marks the task as completed.
        """
        self.completed = True

    def __str__(self):
        """
        Return string representation of the task.
        :return: Show status and description.
        """
        status = 'Completed' if self.completed else 'Not Completed'
        return f'{status} : {self.task}'