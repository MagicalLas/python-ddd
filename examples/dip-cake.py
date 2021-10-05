from abc import ABC, abstractmethod


class Interface1(ABC):
    @abstractmethod
    def method1(self) -> None:
        pass


class Interface2(ABC):
    @abstractmethod
    def method2(self) -> None:
        pass


# domain
class WithInterface1(ABC):
    @property
    @abstractmethod
    def interface1(self) -> Interface1:
        pass


class WithInterface2(ABC):
    @property
    @abstractmethod
    def interface2(self) -> Interface2:
        pass


# adapter
class ConcreteClass1(Interface1):
    def method1(self) -> None:
        print("run ConcreteClass1::method1")


class ConcreteClass2(Interface2):
    def method2(self) -> None:
        print("run ConcreteClass2::method2")


# use case
class Controller(WithInterface1, ABC):
    def execute(self) -> None:
        self.interface1.method1()


# main
class Components(Controller, WithInterface2, WithInterface1):
    @property
    def interface1(self) -> Interface1:
        return ConcreteClass1()

    @property
    def interface2(self) -> Interface2:
        return ConcreteClass2()


component = Components()
component.execute()
