from abc import ABC, abstractmethod


class IdGenerator(ABC):
    @abstractmethod
    def generateId(self) -> str:
        pass
