from shared.eventInfrastructure.DomainEvent import DomainEvent


class MissingAmortizationTableLineItemsExtracted(DomainEvent):
    def __init__(
        self, eventId, aggregateId, missingAmortizatonTableLineItems: list[dict]
    ):
        payload = {
            "missingAmortizationTableLineItems": missingAmortizatonTableLineItems
        }
        super().__init__(eventId, aggregateId, payload)
