from Employee import Employee


class Engineer(Employee):
    def __init__(self, name: str, age: int, department: str, programming_language: str):
        super().__init__(name, age, department)
        self._programming_language = programming_language

    @property
    def programming_language(self):
        return self._programming_language

    @programming_language.setter
    def programming_language(self, new_programming_language):
        if new_programming_language == 'Python':
            self._programming_language = new_programming_language
        else:
            print(f'New programming language should be a Python, {new_programming_language} received instead')

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")

    def work(self):
        print(f"{self.name} is performing engineering duties.")

if __name__ == '__main__':
    engineer = Engineer("Eva", 31, "IT", "Python")
    engineer.code()
    engineer.programming_language = 'Java'
