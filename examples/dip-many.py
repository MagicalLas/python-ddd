from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def method(self) -> None:
        pass


class ConcreteClass(Interface):
    def method(self) -> None:
        print("run ConcreteClass::method")


class Controller(object):
    def __init__(self, interface: Interface) -> None:
        self._interface = interface

    def execute(self) -> None:
        self._interface.method()
