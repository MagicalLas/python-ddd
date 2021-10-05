from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def method(self) -> None:
        pass


class ConcreteClass(Interface):
    def method(self) -> None:
        print("run ConcreteClass::method")


class Env(Interface):
    pass


class ServerEnv(Env):
    def method(self) -> None:
        pass


class Controller(object):
    def __init__(self, env: Env) -> None:
        self._env = env

    def execute(self) -> None:
        self._env.method()
