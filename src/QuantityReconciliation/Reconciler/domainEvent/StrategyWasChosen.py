from .DomainEvent import DomainEvent


class StrategyWasChosen(DomainEvent):
    def __init__(self, eventId, aggregateId, strategy):
        payload = {"strategy": strategy}
        super().__init__(eventId, aggregateId, payload)
