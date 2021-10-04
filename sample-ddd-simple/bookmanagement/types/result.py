from abc import abstractmethod, ABC
from enum import auto


class Result(ABC):
    @abstractmethod
    def get_reason(self) -> str:
        pass


class Success(Result):
    def __init__(self, msg: str):
        self._msg = msg

    def get_reason(self) -> str:
        return self._msg


class Fail(Result):
    def __init__(self, msg: str):
        self._msg = msg

    def get_reason(self) -> str:
        return self._msg
