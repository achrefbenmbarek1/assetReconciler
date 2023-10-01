from shared.eventInfrastructure.DomainEvent import DomainEvent


class ReconciliationWasInitialized(DomainEvent):
    def __init__(self, eventId, aggregateId, physicalInventory:list[dict], amortizationTable:list[dict]):
         payload = {
             "physicalInventory": physicalInventory,
             "amortizationTable": amortizationTable
            
        }
         super().__init__(eventId, aggregateId, payload)

