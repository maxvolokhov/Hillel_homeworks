from Employee import Employee


class Manager(Employee):
    def __init__(self, name: str, age: int, department: str, team_size: int):
        super().__init__(name, age, department)
        self._team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, new_team_size):
        if isinstance(new_team_size, int) and len(str(new_team_size)) < 6:
            self._team_size = new_team_size
        else:
            print('Received wrong type or length of input, please ise int with length less than 6 ')

    def manage_team(self):
        print(f"{self.name} is managing a team.")

    def work(self):
        print(f"{self.name} is performing managerial duties.")

if __name__ == '__main__':
    manager = Manager("Bob", 18, "Sales", 5)
    manager.manage_team()
    manager.team_size = 1250
