class Property:
    def __init__(self, worth: float = 0):
        self.__worth = worth  # руб.
        self.set_worth(worth=float(worth))

    def get_worth(self) -> float:
        return self.__worth

    def set_worth(self, worth: float = 0):
        self.__worth = worth

    def calculate_tax(self) -> float:
        pass

    def __str__(self) -> str:
        return f'Объект - {self.__class__.__name__}, стоимсть - {self.get_worth()}, налог - {self.calculate_tax()}'


class Apartment(Property):
    def __init__(self, worth: float):
        super().__init__(worth=worth)

    def calculate_tax(self) -> float:
        return self.get_worth() * 0.001


class Car(Property):
    def __init__(self, worth: float = 0):
        super().__init__(worth=worth)

    def calculate_tax(self) -> float:
        return self.get_worth() * 0.005


class CountryHouse(Property):
    def __init__(self, worth: float = 0):
        super().__init__(worth=worth)

    def calculate_tax(self) -> float:
        return self.get_worth() * 0.002


def main():
    count_money = float(input('Введите количество ваших денег: '))
    apartment = Apartment(float(input('Введите стоимость квартиры: ')))
    print(apartment)
    car = Car(float(input('Введите стоимость авто: ')))
    print(car)
    house = CountryHouse(float(input('Введите стоимость дачи: ')))
    print(house)
    tax_amount = apartment.calculate_tax() + car.calculate_tax() + house.calculate_tax()
    if count_money < tax_amount:
        print('Пришло время заплатить по счетам!')
        print(
            f'Ты должен в казну {tax_amount}, но у тебя {count_money}! Прийдется напрячься, чтобы заплатить по счетам!'
        )
    else:
        print(f'Ты можешь спать спокойно! Налоги уплачены!')


if __name__ == '__main__':
    main()
