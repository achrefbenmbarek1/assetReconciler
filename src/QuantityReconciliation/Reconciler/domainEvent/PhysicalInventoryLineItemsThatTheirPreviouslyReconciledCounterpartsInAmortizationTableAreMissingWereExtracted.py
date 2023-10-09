from .DomainEvent import DomainEvent


class PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted(DomainEvent):
    def __init__(
        self, eventId, aggregateId, missingAmortizatonTableLineItems: list[dict]
    ):
        payload = {
            "missingAmortizationTableLineItems": missingAmortizatonTableLineItems
        }
        super().__init__(eventId, aggregateId, payload)
