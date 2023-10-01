from shared.eventInfrastructure.DomainEvent import DomainEvent


class ProblematicLineItemsInPhysicalInventoryExtracted(DomainEvent):
    def __init__(
        self, eventId, aggregateId, problematicLineItemsInPhysicalInventory: list[dict]
    ):
        payload = {
            "problematicLineItemsInPhysicalInventory": problematicLineItemsInPhysicalInventory
        }
        super().__init__(eventId, aggregateId, payload)
