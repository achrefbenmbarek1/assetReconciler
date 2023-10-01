from shared.eventInfrastructure.DomainEvent import DomainEvent


class NonPreviouslyReconsiledInvAndTaWereFilteredByQuantity(DomainEvent):
    def __init__(self, eventId, aggregateId, filteredData):
        payload = {"filteredData": filteredData}
        super().__init__(eventId, aggregateId, payload)
