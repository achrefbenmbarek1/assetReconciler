from abc import ABC, abstractmethod
from shared.eventInfrastructure.DomainEvent import DomainEvent


class EventBus(ABC):
    @abstractmethod
    def subscribe(self,eventType:str, subscriber):
        pass

    @abstractmethod
    def publish(self,domainEvent:DomainEvent):
        pass
