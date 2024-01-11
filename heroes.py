from monsters import *


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нет кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.

    """
    Базовый класс позволяющий создать героя
    Аргументы:
        name - имя героя
    Аттрибуты:
        max_hp - здоровье героя, по умолчанию равно 150
        start_power - сила героя, по умолчанию равна 10
    """

    max_hp = 150
    start_power = 10

    def __init__(self, name: str):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self) -> int | float:
        """
        Геттер для получения информации о состоянии здоровья героя
        :return: __hp
        :rtype: int | float
        """
        return self.__hp

    def set_hp(self, new_value: int | float):
        """
        Сеттер для изменения состояния здоровья героя
        :param new_value: значение которое необходимо установить
        """
        self.__hp = max(new_value, 0)

    def get_power(self) -> int | float:
        """
        Геттер для получения информации о силе героя
        :return: __power
        :rtype: int | float
        """
        return self.__power

    def set_power(self, new_power: int | float):
        """
        Сеттер для изменения силы героя
        :param new_power: значение которое необходимо установить
        """
        self.__power = new_power

    def is_alive(self) -> bool:
        """
        Метод позволяет определить жив ли объект. Возвращает True если объект жив, иначе False
        :return: bool
        """
        return self.__is_alive

    def attack(self, target: Monster):
        """
        Метод позволяет атаковать врага. Для каждого героя определяется правилами своего класса
        :param target: экземпляр класса Monster
        """
        # Каждый наследник будет наносить урон согласно правилам своего класса
        pass

    def take_damage(self, damage: int | float):
        """
        Метод наносит урон герою при атаке врага
        :param damage: количество урона нанесенное врагом
        """
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить
        # выживаемость героев
        print("\t", self.name, f"Получил удар с силой равной = {round(damage)}. Осталось здоровья -",
              round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends: list, enemies: list):
        """
        Метод позволяющий герою выполнить одно из действий согласно правилам своего класса
        :param friends: список союзников
        :param enemies: список врагов
        """
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self) -> str:
        return 'Имя: {0} | Здоровье: {1}'.format(self.name, self.get_hp())


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
    # действий (атака, исцеление) на выбранную им цель

    """
    Дочерний класс Healer, родитель: Hero
    Позволяет создать героя целителя
    Аргументы:
        name - имя героя
    Атрибуты:
        magic_power - магическая сила равная НАЧАЛЬНОМУ показателю силы умноженному на 3
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def attack(self, target: Monster):
        """
        Метод позволяет атаковать врага с силой в два раза меньшей базового значения
        :param target: экземпляр класса Monster
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: int | float):
        """
        Метод наносит урон герою при атаке врага. Защита целителя слаба - он получает на 20% больше урона
        :param damage: количество входящего урона нанесенного врагом
        """
        self.set_hp(self.get_hp() - damage * 1.2)
        super().take_damage(damage)

    def healing(self, target: Hero):
        """
        Метод позволяет исцелить себя или союзника. Увеличивает здоровье цели на величину равную своей магической силы
        :param target: экземпляр класса Hero
        """
        target.set_hp(target.get_hp() + self.magic_power)

    def make_a_move(self, friends: list, enemies: list):
        """
        Метод позволяющий герою выполнить действие (атака или исцеление) на выбранную им цель
        :param friends: список союзников
        :param enemies: список врагов
        """
        print(self.name, end=': ')
        target_for_healing = friends[0]
        min_health = target_for_healing.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_for_healing = friend
                min_health = target_for_healing.get_hp()

        if min_health <= 70:
            print("исцеляю", target_for_healing.name)
            self.healing(target_for_healing)
        else:
            if not enemies:
                print("изготавливаю новую микстуру")
            else:
                target = enemies[0]
                print("атакую ближайшего -", target.name)
                self.attack(target)
        print('\n')
        super().make_a_move(friends, enemies)


class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом
    # отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает
    # показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает
    # показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет
    # ОДНО из действий (атака, поднять щит/опустить щит) на выбранную им цель

    """
    Дочерний класс Tank, родитель: Hero
    Позволяет создать героя 'танк'
    Аргументы:
        name - имя героя
    Атрибуты:
        defense - показатель защиты танка изначально равен 1, может увеличиваться и уменьшаться
        shield_up - этот атрибут показывает поднят ли щит в данный момент, по умолчанию значение False
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.defense = 1
        self.shield_up = False

    def attack(self, target: Monster):
        """
        Метод позволяет атаковать врага с силой в два раза меньшей базового значения
        :param target: экземпляр класса Monster
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: int | float):
        """
        Метод наносит урон герою при атаке врага. Весь входящий урон делится на показатель защиты
        :param damage: количество входящего урона нанесенного врагом
        """
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)

    def raise_shield(self):
        """
        Метод поднимает щит и увеличивает показатель защиты героя в два раза, но при этом уменьшается сила в два раза
        """
        self.shield_up = True
        self.defense *= 2
        self.set_power(self.get_power() / 2)

    def lower_shield(self):
        """
        Метод опускает щит и уменьшает показатель защиты героя в два раза, но при этом увеличивается сила в два раза
        """
        self.shield_up = False
        self.defense /= 2
        self.set_power(self.get_power() * 2)

    def make_a_move(self, friends: list, enemies: list):
        """
        Метод позволяющий герою выполнить действие (атаку на выбранную им цель или поднять щит/опустить щит) в
        зависимости от выбранной стратегии
        :param friends: список союзников
        :param enemies: список врагов
        """
        print(self.name, end=': ')
        if self.get_hp() < 50 and not self.shield_up:
            print(self.name, 'поднял щит')
            self.raise_shield()
        elif self.get_hp() > 120 and self.shield_up:
            print(self.name, 'опустил щит')
            self.lower_shield()
        else:
            if not enemies:
                print('провожу разведку\n')
            else:
                target = random.choice(enemies)
                print("случайно атакую -", target.name)
                self.attack(target)
        print('\n')
        super().make_a_move(friends, enemies)


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления
    # урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления
    # урона - damage * (self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет
    # ОДНО из действий (атака, усиление, ослабление) на выбранную им цель

    """
    Дочерний класс Attacker, родитель: Hero
    Позволяет создать героя убийцу
    Аргументы:
        name - имя героя
    Атрибуты:
        power_multiply - коэффициент усиления урона (входящего и исходящего)
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target: Monster):
        """
        Метод позволяет атаковать врага с силой умноженной на коэффициент усиления урона
        :param target: экземпляр класса Monster
        """
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def take_damage(self, damage: int | float):
        """
        Метод наносит урон герою при атаке врага. Весь входящий урон равный входящему урону умноженному на половину
        коэффициента усиления урона
        :param damage: количество входящего урона нанесенного врагом
        """
        self.set_hp(self.get_hp() - (damage * (self.power_multiply / 2)))
        super().take_damage(damage)

    def power_up(self):
        """
        Метод увеличивает коэффициента усиления урона в 2 раза
        """
        self.power_multiply *= 2

    def power_down(self):
        """
        Метод уменьшает коэффициента усиления урона в 2 раза
        """
        self.power_multiply /= 2

    def make_a_move(self, friends: list, enemies: list):
        """
        Метод позволяющий герою выполнить действие (атаку на выбранную им цель или увеличения/уменьшения коэффициента
        усиления урона) в зависимости от выбранной стратегии
        :param friends: список союзников
        :param enemies: список врагов
        """
        print(self.name, end=': ')
        if self.power_multiply <= 2:
            print('наращиваю силу')
            self.power_up()
        else:
            if not enemies:
                print('охраняю границы')
            else:
                target = [enemy for enemy in enemies if isinstance(enemy, MonsterBerserk)]
                if target:
                    print("атакую -", target[0].name)
                    self.attack(target[0])
                else:
                    target = random.choice(enemies)
                    print("случайно атакую -", target.name)
                    self.attack(target)
        print('\n')
        super().make_a_move(friends, enemies)


if __name__ == '__main__':
    healer = Healer('Антон')
    tank = Tank('Дарина')
    attacker = Attacker('Аня')
    print(attacker, healer, tank, sep='\n')
