___doc___ = """Describe any object of your choice in the class.
I want the object to be printed to the console in the following format:

class_name: {

key: value

}"""


class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}:\n{{\nmake: {self.brand},\nmodel: {self.model},\nyear: {self.year},\ncolor: " \
 \
               f"{self.color}\n}}"


if __name__ == '__main__':
    car = Car('Toyota', 'Camry', 2022, 'Blue')
    print(car)
