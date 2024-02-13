# Задача 1. Налоги
***
Что нужно сделать:
1. Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse.

2. Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога, переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500. 

3. Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.

4. Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества, а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).
***
Что оценивается:
* Результат вычислений корректен.
* Input содержит корректные приглашения для ввода. 
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.

* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Сообщения о процессе получения результата осмысленны и понятны пользователю.
* Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
* Классы и методы/функции имеют прописанную документацию.
***
#### Запуск приложения
Запуск приложения реализуется с помощью файла [main.py](main.py)
***
# Задача 2. Карма
***
Что нужно сделать:

Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления. 

Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
* KillError,
* DrunkError,
* CarCrashError,
* GluttonyError,
* DepressionError.

(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)

Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.

По итогу у вас может быть примерно такая структура программы:

1. открываем файл

2. цикл по набору кармы
```python
  try

      карма += one_day()

   except(ы) с указанием классов исключений, которые нужно поймать
```
3. добавляем запись в файл
4. закрываем файл
***
Что оценивается:
* Результат вычислений корректен.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Сообщения о процессе получения результата осмысленны и понятны пользователю.
* Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
* Классы и методы/функции имеют прописанную документацию.
* Названия используемых файлов соответствуют тем, которые указаны в задаче.
***
#### Запуск приложения
Запуск приложения реализуется с помощью файла [main.py](main.py)
***
# Задача 3. Свой словарь
***
### Что нужно сделать:

В силу обстоятельств Васе постоянно приходится работать со 
словарями и их данными. В том числе и с методом get, который по умолчанию 
возвращает None, если такого ключа в словаре нет. Однако Васю это 
не устраивает: для нормальной работы ему нужно возвращать число 0.

Реализуйте класс MyDict, который будет вести себя точно так же, как и 
обычный словарь (попробуйте унаследовать его от оригинального dict), 
за исключением того, что метод get по умолчанию будет возвращать не None, 
а число 0.
***
### Что оценивается:
* Результат вычислений корректен.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
* Сообщения о процессе получения результата осмысленны и понятны пользователю.
* Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
* Классы и методы/функции имеют прописанную документацию.
*****
# Задача 4. RPG-игра
***
### Что нужно сделать:
Вася решил заняться разработкой компьютерных игр (Python применяется даже в геймдеве!). Ему поручили разрабатывать искусственный интеллект для союзников, которые сражаются бок о бок с реальными игроками. Но так как Вася пока не силён в теме машинного обучения и нейросетей, ему предстоит заменить эти знания смекалкой и набором if/else-условий.
Вася уже написал код, описывающий монстров (файл monsters.py), этот код изменять нельзя.

**В файле heroes.py вы найдёте заготовки системы классов:**

* базовый класс hero, который нельзя изменять;
* наследники класса tank/healer/attacker — их надо изменять.

**Помимо этого, в main.py есть код, который:**

* запускает один год сражений — изменять нельзя;
* создаёт команду для сражения с монстрами — изменять можно, но с условиями;
* запускает 20 раз один год сражений и подсчитывает количество побед — изменять нельзя.

**Ваша задача:**

* Дописать код в классы tank/healer/attacker в файле heroes.py.
* Сформировать команду в main.py.
* Проверить, что с выбранной вами стратегией герои побеждают монстров как минимум в половине случаев (>= 10 побед из 20).

***Цель: из 20 сражений нужно побеждать как минимум в 10. В сражениях много 
случайностей, поэтому убедитесь, что в нескольких разных запусках 
ваша команда набирает нужное количество очков.***

### Советы и рекомендации
* Внимательно изучите код поведения монстров. Изменять его нельзя, но изучать не запрещено.
* При помощи команды print выводите информацию о том, кто и что делает каждый день. Особое внимание уделите информации, которая идёт в последние дни перед поражением героев.
* На основе полученной информации попробуйте изменять приоритеты действий. 

Обратите внимание, что вы можете не только выбирать действие для выполнения, но также выбрать цель для действия. Иногда может быть выгоднее атаковать монстров конкретного класса, чтобы уменьшить урон по вашей команде.
### Что оценивается
* Как минимум в трёх запусках из пяти команда героев побеждает 10+ раз.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
* Модели реализованы согласно инструкциям.
* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Сообщения о процессе получения результата осмысленны и понятны пользователю.
* Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
* Классы и методы/функции имеют прописанную документацию.
### Запуск игры
Игра запускается из основного файла [main.py](main.py)
*****
# Задача 5. Стек

### Что нужно сделать

Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры данных на основе уже существующих. Одной из таких базовых структур является стек. 

Стек — это абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

Простой пример: стек из книг на столе. Единственной книгой, обложка которой видна, является самая верхняя. Чтобы получить доступ, например, к третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.

Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента). 

После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить команду «новая задача», в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе стека (не наследование). При выводе менеджера в консоль все задачи должны быть отсортированы по следующему приоритету: чем меньше число, тем выше задача.

Вот пример основной программы:

manager = TaskManager()

manager.new_task("сделать уборку", 4)

manager.new_task("помыть посуду", 4)

manager.new_task("отдохнуть", 1)

manager.new_task("поесть", 2)

manager.new_task("сдать ДЗ", 2)

print(manager)

Результат:

1 — отдохнуть

2 — поесть; сдать ДЗ

4 — сделать уборку; помыть посуду

Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.
### Что оценивается

* Результат вычислений корректен.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Формат вывода соответствует примеру.
* Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
* Классы и методы/функции имеют прописанную документацию.
### Запуск скрипта
Скрипт запускается из основного файла [main.py](main.py)
# Задача 6. Абстрактный класс
### **Контекст** 

Вы работаете в компании, занимающейся разработкой программного обеспечения для архитектурных проектов. Вам необходимо разработать программу для расчёта площади различных геометрических фигур, таких как круги, прямоугольники и треугольники.
### Задача
Создайте:

* класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area, который наследники должны переопределить;
* класс Circle;
* класс Rectangle;
* класс Triangle. 

Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.

Дополнительно: изучите информацию [о работе с абстрактными классами.](https://docs-python.ru/tutorial/klassy-jazyke-python/abstraktnye-klassy/)

На основе этой информации сделайте так, чтобы:

* Нельзя было создавать объекты класса Shape.
* Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.


### Что оценивается в практической работе

* Задание сдано через GitLab.
* Структура папок и файлов репозитория соответствует репозиторию python_basic.
* Все задачи выполнены в соответствующих папках и файлах main.py.
* Описания коммитов осмысленны и понятны: 111, done, «я сделалъ» — неверно; added m15 homework, 14.3 fix: variables naming — верно.
* Использованы именованные индексы, а не просто i (подробнее — в видео 7.2).
* Использованы правильные числа, без дополнительных действий со стороны пользователя, без +1 (подробнее — в видео 7.4).
* Правильно оформлен input, без пустого приветствия для ввода (подробнее — в видео 2.3).
* Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее — в видео 2.3).
* Присутствуют пробелы после запятых и при бинарных операциях.
* Отсутствуют пробелы после имён функций и перед скобками: print (), input () — неверно; print() — верно.
* Правильно оформлены блоки if-elif-else, циклы и функции, отступы одинаковы во всех блоках одного уровня.
* Все входные и выходные файлы называются так, как указано в заданиях.
* Работа с файлами осуществляется с помощью контекстного менеджера with.
* Для обработки исключений используются блоки try-except.
* Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
* При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
* Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
* Для создания нового класса на основе уже существующего используется наследование.
* Если классы вынесены в отдельный модуль, то импортируются определённые классы (запись вида from garden import * считается плохим тоном).
* Классы и методы/функции имеют прописанную документацию.

### Запуск скрипта
Скрипт запускается из основного файла [main.py](main.py)
