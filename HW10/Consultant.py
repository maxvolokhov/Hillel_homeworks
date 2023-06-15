from Worker import Worker


class Consultant(Worker):
    def __init__(self, name: str, age: int, area_of_expertise: str):
        super().__init__(name, age)
        self._area_of_expertise = area_of_expertise

    @property
    def area_of_expertise(self):
        return self._area_of_expertise

    @area_of_expertise.setter
    def area_of_expertise(self, new_area_of_expertise):
        if isinstance(new_area_of_expertise, str) and len(new_area_of_expertise) < 15:
            self._area_of_expertise = new_area_of_expertise
        else:
            print(f'New area of expertise should be a string with length less than 15\n'
                  f'{type(new_area_of_expertise)} with length {len(new_area_of_expertise)} received instead')

    def provide_consultation(self):
        print(f"{self.name} is providing consultation in {self.area_of_expertise}.")

    def work(self):
        print(f"{self.name} is performing consulting duties.")

if __name__ == '__main__':
    consultant = Consultant("Sarah", 35, "Marketing")
    consultant.provide_consultation()
    consultant.area_of_expertise = 'QA'
