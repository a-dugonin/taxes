class MyDict(dict):
    """
    Собственный класс позволяющий создать словарь возвращающий значение 0 вместо None при передаче в метод get ключа
    отсутствующего в словаре.
    Данный класс унаследован от класса dict, поэтому имеет все родительские методы.
    """
    def get(self, key: object) -> object:
        """
        Геттер для получения значения словаря по его ключу.
        В случае если ключ в словаре отсутствует, возвращается '0'
        :param key: object
        :return: object or 0
        """
        if key in self:
            return self[key]
        return 0


if __name__ == '__main__':
    new_dict = MyDict({1: 'a', 2: 'b'})
    print(new_dict.get(1))
    print(new_dict.get(3))
