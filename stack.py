class Stack(list):
    def append(self, elem, index: int = 0):
        self.insert(index - 1, elem)


class TaskManager:
    def __init__(self):
        self.task_list = Stack()
        self.task_priorities_available = Stack()

    @staticmethod
    def create_new_task(task, priority):
        new_task = Stack()
        new_task.append(priority)
        new_task.append(task)
        return new_task

    def add_task(self, task, priority):
        if priority not in self.task_priorities_available:
            self.task_list.append(self.create_new_task(task, priority), priority)
            self.task_priorities_available.append(priority, priority)
        else:
            if len(self.task_list) <= priority:
                if task not in self.task_list[-1]:
                    self.task_list[-1].append(task)
            else:
                if task not in self.task_list[priority - 1]:
                    self.task_list[priority - 1].append(task)

    def remove_task(self, task):
        for tasks in self.task_list:
            if task in tasks and len(tasks) > 2:
                tasks.remove(task)
            else:
                if task in tasks:
                    self.task_list.remove(tasks)

    def __str__(self):
        task_list_string = 'Список задач:\n'
        for task in self.task_list:
            task_list_string += f"{task[-1]} - {'; '.join(task[:-1])}\n"
        return f'{task_list_string}'


if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task("сделать уборку", 4)
    manager.add_task("помыть посуду", 4)
    manager.add_task("отдохнуть", 1)
    manager.add_task("поесть", 2)
    manager.add_task("поесть", 2)
    manager.add_task("сдать ДЗ", 2)
    manager.add_task("погладить кошку", 5)
    manager.add_task("выпить кофе", 3)
    print(manager)
    print()
    manager.remove_task('поесть')
    print(manager)
    print()
    manager.remove_task('сдать ДЗ')
    print(manager)
