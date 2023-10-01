from shared.eventInfrastructure.DomainEvent import DomainEvent


class StrategyWasChosen(DomainEvent):
    def __init__(self, eventId, aggregateId, strategy):
        self.strategy = strategy
        super().__init__(eventId, aggregateId)

