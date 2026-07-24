class Task:
    def __init__(self, description):
        self.description = description
        self.done = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        print(f'Task "{task.description}" added.')
        self.tasks.append(task)

    def complete_task(self, task):
        if task not in self.tasks:
            print(f'Task "{task.description}" not found.')
            return

        task.done = True
        print(f'\n~~~ Task "{task.description}" completed ~~~')

    def remove_task(self, task):
        if task not in self.tasks:
            print(f'Task "{task.description}" not found.')
            return

        self.tasks.remove(task)
        print(f'Task "{task.description}" removed.')

    def show_tasks(self):
        print('\n===== All tasks =====')

        for task in self.tasks:
            status = 'Completed' if task.done else 'In progress'
            print(f'Description: {task.description}\n Status: {status}\n')


task_manager = TaskManager()

task1 = Task('Defeat the OOP')
task2 = Task('Learn classes and objects')
task3 = Task('Learn the principles of OOP')

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.complete_task(task2)
task_manager.complete_task(task3)

task_manager.show_tasks()
