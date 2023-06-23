___doc___ = """Describe the Train object. The class must contain fields and a method for adding wagons (it is necessary
 to add objects, and instances of the wagon class). Describe the class Wagon together with the train. 
 The Wagon must contain a list of passengers and allow adding passengers. In the Wagon can be 10 passengers for example.
  When using the len function on a Wagon, I want to see the number of passengers. 
  When using len on a train, I want to see a list of Wagons without a locomotive. Each wagon must have a number. 
  When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon."""


class Wagon:
    def __init__(self, number: int):
        self.number = number
        self.passengers = []

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("Wagon is full. Cannot add more passengers.")


class Train:
    def __init__(self):
        self.wagons = []

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        wagon_list = ", ".join(str(wagon) for wagon in self.wagons[1:])
        return f"Train: {wagon_list}"

    def add_wagon(self, wagon):
        self.wagons.append(wagon)


if __name__ == '__main__':
    train = Train()

    wagon1 = Wagon(1)
    wagon1.add_passenger("Passenger 1")
    wagon1.add_passenger("Passenger 2")
    train.add_wagon(wagon1)

    wagon2 = Wagon(2)
    wagon2.add_passenger("Passenger 3")
    train.add_wagon(wagon2)

    print(f"Number of wagons in the train: {len(train)}")
    print(f"Wagons in the train: {train}")
    print(f"Number of passengers in wagon 1: {len(wagon1)}")
    print(f"Number of passengers in wagon 2: {len(wagon2)}")
