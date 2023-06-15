from Employee import Employee


class Administrator(Employee):
    def __init__(self, name: str, age: int, department: str, responsibility: str):
        super().__init__(name, age, department)
        self._responsibility = responsibility

    @property
    def responsibility(self):
        return self._responsibility

    @responsibility.setter
    def responsibility(self, new_responsibility):
        if isinstance(new_responsibility, str) and len(new_responsibility) < 15:
            self._responsibility = new_responsibility
        else:
            print(f'New responsibility should be a string with length less than 15\n'
                  f'{type(new_responsibility)} with length {len(new_responsibility)} received instead')

    def manage_systems(self):
        print(f"{self.name} is managing systems and {self.responsibility}.")

    def work(self):
        print(f"{self.name} is performing administrative duties.")

if __name__ == '__main__':
    administrator = Administrator("Mike", 28, "Operations", "ensuring smooth operations")
    administrator.manage_systems()
    administrator.responsibility = 'Development'
