from shared.eventInfrastructure.DomainEvent import DomainEvent


class MissingPhysicalInventoryLineItemsExtracted(DomainEvent):
    def __init__(
        self, eventId, aggregateId, missingLineItemsInPhysicalInventory: list[dict]
    ):
        payload = {
            "missingPhysicalInventoryLineItems": missingLineItemsInPhysicalInventory
        }
        super().__init__(eventId, aggregateId, payload)
