from Worker import Worker


class Employee(Worker):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        if isinstance(new_department, str) and len(new_department) < 15:
            self._department = new_department
        else:
            print('**Warning** Please insert correct str name with length less than 15')

    def attend_meeting(self):
        print(f'{self.name} is attending a meeting.')

    def work(self):
        print(f'{self.name} is performing employee duties.')


if __name__ == '__main__':
    employee = Employee('Alice', 23, 'HR')
    employee.attend_meeting()
    employee.work()
