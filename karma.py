from random import randint, choice

KARMA = 500


class KillError(Exception):
    """ Класс для реализации исключения KillError """
    pass


class DrunkError(Exception):
    """ Класс для реализации исключения DrunkError """
    pass


class CarCrashError(Exception):
    """ Класс для реализации исключения CarCrashError """
    pass


class GluttonyError(Exception):
    """ Класс для реализации исключения GluttonyError """
    pass


class DepressionError(Exception):
    """ Класс для реализации исключения DepressionError """
    pass


class Buddhist:
    """
    Базовый класс описывающий жизнь буддиста

    Аргументы:
        karma_level - уровень кармы буддиста, по умолчанию значение равно 0
    Аттрибуты:
        count_day - количество дней которое необходимо прожить буддисту для достижения цели по количеству кармы
    """
    count_day = 0

    def __init__(self, karma_level: int = 0):
        self.__karma_level = karma_level

    def get_karma_level(self) -> int:
        """
        Геттер для получения стоимости имущества
        :return: __karma_level
        :rtype: int
        """
        return self.__karma_level

    def set_karma_level(self, karma_level: int = 0):
        """
        Сеттер для установления стоимость имущества
        :param karma_level: стоимость имущества
        """
        self.__karma_level = karma_level

    def one_day(self):
        """ Метод позволяет прожить буддисту один день """
        self.count_day += 1
        not_best_day = randint(1, 10)
        try:
            if not_best_day == randint(1, 10):
                raise choice([KillError(), DrunkError(), GluttonyError(), CarCrashError(), DepressionError()])
            else:
                self.set_karma_level(self.get_karma_level() + randint(1, 7))
        except (KillError, DrunkError, GluttonyError, CarCrashError, DepressionError) as err:
            with open('karma.log', 'a', encoding='utf8') as karma_log_file:
                karma_log_file.write(f'{err.__class__.__name__}, день - {self.count_day}\n')

    def life(self):
        """ Метод позволяет жить буддисту и зарабатывать очки кармы для достижения просветления (значения KARMA) """
        file = open('karma.log', 'w')
        file.close()
        while self.get_karma_level() <= KARMA:
            self.one_day()
        print(f'Для достижения цели потребовалось {self.count_day} дней')
        print(f'Теперь ваша карама {self.get_karma_level()}')


def main():
    buddha = Buddhist()
    buddha.life()


if __name__ == '__main__':
    main()
