from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.capitalize():
            self._name = new_name
        else:
            print(f'Name should be a string from a capital letter: type{new_name}{new_name[0]}')

    @abstractmethod
    def work(self):
        pass


if __name__ == '__main__':
    worker = Worker("John", 30)
