from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def execute(self, command):
        pass
