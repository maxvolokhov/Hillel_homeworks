from HW11.interfaces.i_phone import Phone
from HW11.interfaces.i_smartphone import Smartphone
from time import time, sleep


# Inheritance
# Abstraction
class Iphone(Phone, Smartphone):

    def __init__(self):
        self.__power_on_status = False
        self.__battery_percent = 0
        self.__readiness_for_update = False

    # Polymorphism
    # Abstraction
    def _switch_on(self):
        self.__power_on_status = True
        sleep(3)
        print('Welcome to iPhone')

    # Polymorphism
    # Abstraction
    def _switch_off(self):
        self.__power_on_status = False
        sleep(3)
        print('Thanks for your usage, bye')

    # Polymorphism
    # Abstraction
    # Incapsulation
    def _charge(self, battery: int):
        if battery >= 80:
            print('Your iPhone has enough battery percent')
        else:
            while 1 <= battery <= 80:
                print('Your iPhone is charging')
                battery += 1
                if battery >= 80:
                    print('Your iPhone has enough battery percent')
                    break
            print('Your iPhone has been charged up to 80%')
        self.__battery_percent = battery

    # Polymorphism
    # Abstraction
    def _run_application(self):
        sleep(0.1)
        print('Application has been started')

    # Polymorphism
    # Abstraction
    def _update_software(self):
        self.__readiness_for_update = True
        if 51 <= self.__battery_percent <= 100:
            print('Updating will be started in few seconds')
            sleep(3)
            print('Your iPhone has been updated to the last version')
        else:
            print(f'Your battery is {self.__battery_percent}%. Please put it on charging to start software updating')

    # Incapsulation
    def _iphone_testing(self, battery_percent: int):
        while self.__battery_percent < battery_percent:
            self.__battery_percent += 1
            self._run_application()
        print('Application has been finished')

    # Incapsulation
    def full_cycle_of_testing(self, battery_percent: int):
        start_time = time()
        self._switch_on()
        self._iphone_testing(battery_percent)
        self._charge(battery_percent)
        self._update_software()
        self._switch_off()
        finish_time = time()
        print(f'Total time of full cycle took {finish_time - start_time}')


if __name__ == '__main__':
    iphone = Iphone()
    iphone.full_cycle_of_testing(85)
