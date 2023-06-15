from Engineer import Engineer


class Developer(Engineer):
    def __init__(self, name: str, age: int, department: str, programming_language: str, framework: str):
        super().__init__(name, age, department, programming_language)
        self._framework = framework

    @property
    def framework(self):
        return self._framework

    @framework.setter
    def framework(self, new_framework):
        if new_framework == 'Django' or new_framework == 'Pytest':
            self._framework = new_framework
        else:
            print(f'New framework should be a Django or Pytest, {new_framework} received instead')

    def develop(self):
        print(f"{self.name} is developing using {self.framework}.")

    def work(self):
        print(f"{self.name} is performing development duties.")

if __name__ == '__main__':
    developer = Developer("David", 30, "IT", "JavaScript", "React")
    developer.develop()
    developer.framework = 'Django'
