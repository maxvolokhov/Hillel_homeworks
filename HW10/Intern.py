from Developer import Developer


class Intern(Developer):
    def __init__(self, name: str, age: int, department: str, programming_language: str, framework: str,
                 experience: int | float):
        super().__init__(name, age, department, programming_language, framework)
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new_experience):
        if isinstance(new_experience, int | float) and len(str(new_experience)) <= 6:
            self._experience = new_experience
        else:
            print(f'New experience should be indicated like int or float with length equal or less than 6\n'
                  f'{type(new_experience)} with length {len(str(new_experience))} received instead')

    def learn(self):
        print(f"{self.name} is learning and gaining experience.")

    def work(self):
        print(f"{self.name}, {self.age} is performing intern duties.")

if __name__ == '__main__':
    intern = Intern("Emma", 22, "IT", "Python", "Django", 4.5)
    intern.learn()
    intern.work()
    intern.experience = 25.10
