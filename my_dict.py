class MyDict(dict):
    def get(self, key):
        if key in self:
            return self[key]
        return 0


if __name__ == '__main__':
    new_dict = MyDict({1: 'a', 2: 'b'})
    print(new_dict.get(1))
