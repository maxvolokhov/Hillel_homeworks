from abc import ABC, abstractmethod


class Smartphone(ABC):

    @abstractmethod
    def _run_application(self):
        pass

    @abstractmethod
    def _update_software(self):
        pass
