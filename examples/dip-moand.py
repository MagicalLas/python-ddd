from abc import ABC, abstractmethod
from typing import Callable


class Interface(ABC):
    @abstractmethod
    def method(self) -> None:
        pass


class ConcreteClass(Interface):
    def method(self) -> None:
        print("run ConcreteClass::method")


class Controller(object):
    @staticmethod
    def execute() -> Callable[[Interface], None]:
        def _execute(interface: Interface):
            interface.method()
        return _execute


concrete_class = ConcreteClass()
Controller.execute()(concrete_class)
