from abc import ABC, abstractmethod

from QuantityReconciliation.Reconciler.domainEvent.DomainEvent import DomainEvent


class EventStore(ABC):
    @abstractmethod
    def appendEvents(self,aggregateId, events:list[DomainEvent],expectedVersion:int) -> None:
        pass

    @abstractmethod
    def loadEvents(self, aggregateId) -> list[DomainEvent]:
        pass

