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