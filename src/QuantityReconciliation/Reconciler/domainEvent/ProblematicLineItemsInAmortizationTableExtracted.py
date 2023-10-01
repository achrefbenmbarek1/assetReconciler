from shared.eventInfrastructure.DomainEvent import DomainEvent


class ProblematicLineItemsInAmortizationTableExtracted(DomainEvent):
    def __init__(
        self, eventId, aggregateId, problematicLineItemsInAmortizationTable: list[dict]
    ):
        payload = {
            "problematicLineItemsInAmortizationTable": problematicLineItemsInAmortizationTable
        }

        super().__init__(eventId, aggregateId, payload)
