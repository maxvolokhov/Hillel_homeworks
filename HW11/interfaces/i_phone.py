from abc import ABC, abstractmethod


class Phone(ABC):

    @abstractmethod
    def _switch_on(self):
        pass

    @abstractmethod
    def _switch_off(self):
        pass

    @abstractmethod
    def _charge(self, battery):
        pass
