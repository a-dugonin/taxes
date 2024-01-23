class Stack(list):
    """
    Дочерний класс Stack, родитель: list
    Позволяет создать стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу
    по принципу переданного индекса для добавления элемента
    Данный класс унаследован от класса list, поэтому имеет все его родительские методы.
    В данном классе переопределен только метод append родительского класса list
    """

    def append(self, elem, index: int = 0) -> None:
        """
        Метод добавляет элементы относительно переданного индекса. Если индекс не передан в метод, то элемент
        по умолчанию становится на последнее место в стеке
        :param elem: Any
        :param index: int
        :return: None
        """
        if index == 0:
            self.insert(len(self), elem)
        else:
            self.insert(index - 1, elem)



class TaskManager:
    """
    Базовый класс TaskManager позволяющий создать менеджер задач.
    Аттрибуты:
        task_list - стек задач, по умолчанию пустой
        task_priorities_available - стек имеющихся приоритетов задач, по умолчанию пустой
    """
    def __init__(self) -> None:
        self.task_list = Stack()
        self.task_priorities_available = Stack()

    @staticmethod
    def create_new_task(task: str, priority: int) -> Stack:
        """
        Метод позволяет создать новый список задач с определенным приоритетом.
        :param task: наименование задачи
        :param priority: приоритет задачи
        :return: Stack
        """
        new_task = Stack()
        new_task.append(priority)
        new_task.append(task)
        return new_task

    def add_task(self, task: str, priority: int) -> None:
        """
        Метод добавляет задачу в менеджер задач согласно приоритета задачи
        :param task: наименование задачи
        :param priority: приоритет задачи
        :return: None
        """
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

    def remove_task(self, task: str) -> None:
        """
        Метод удаляет задачу из менеджера задач
        :param task: наименование задачи
        :return: None
        """
        for tasks in self.task_list:
            if task in tasks and len(tasks) > 2:
                tasks.remove(task)
                break
            else:
                if task in tasks:
                    self.task_list.remove(tasks)
                    break

    def __str__(self) -> str:
        task_list_string = 'Список задач:\n'
        for task in self.task_list[:-1]:
            task_list_string += f"{task[0]} - {'; '.join(task[1:])}\n"
        task_list_string += 'Не приоритетные задачи: ' + '; '.join(self.task_list[-1][1:])
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
    manager.add_task('почистить кофемашину', 1)
    manager.add_task('побриться', 8)
    manager.add_task('постирать', 6)
    manager.add_task('убрать', 7)
    manager.add_task('выпить', 0)
    manager.add_task('сходить в караоке', 0)
    print(manager)
    print()
    manager.remove_task('поесть')
    print(manager)
    print()
    manager.remove_task('сдать ДЗ')
    print(manager)
