from stack import TaskManager

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