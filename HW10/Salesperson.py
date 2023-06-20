from Employee import Employee


class Salesperson(Employee):
    def __init__(self, name, age, department, target):
        super().__init__(name, age, department)
        self._target = target

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, new_target):
        if isinstance(new_target, str) and len(new_target) < 15:
            self._target = new_target
        else:
            print(f'New target should be a string with length less than 15\n'
                  f'{type(new_target)} with length {len(new_target)} received instead')

    def meet_sales_target(self):
        print(f"{self.name} is working towards meeting the sales target of {self.target}.")

    def work(self):
        print(f"{self.name} is performing sales duties.")

if __name__ == '__main__':
    salesperson = Salesperson("Emily", 35, "Sales", "$500,000")
    salesperson.meet_sales_target()
    salesperson.target = 'QA Team'
