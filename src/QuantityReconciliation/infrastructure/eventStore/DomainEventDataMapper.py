from QuantityReconciliation.Reconciler.Strategy.domainEvents.StrategyWasChosen import StrategyWasChosen
from QuantityReconciliation.Reconciler.domainEvent.FileLoaded import FileLoaded
from QuantityReconciliation.Reconciler.domainEvent.MissingAmortizationTableLineItemsExtracted import (
    MissingAmortizationTableLineItemsExtracted,
)
from QuantityReconciliation.Reconciler.domainEvent.MissingPhysicalInventoryLineItemsExtracted import (
    MissingPhysicalInventoryLineItemsExtracted,
)
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInAmortizationTableExtracted import (
    ProblematicLineItemsInAmortizationTableExtracted,
)
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInPhysicalInventoryExtracted import (
    ProblematicLineItemsInPhysicalInventoryExtracted,
)
from QuantityReconciliation.Reconciler.domainEvent.ReconciliationWasInitialized import (
    ReconciliationWasInitialized,
)
from shared.eventInfrastructure.DomainEvent import DomainEvent
import json


class DomainEventDataMapper:
    def createDomainEvent(self, eventData) -> DomainEvent:
        print("almost there")
        print(eventData["payload"])
        print(type(eventData["payload"]))
        payload = json.loads(eventData["payload"])
        print("did we got past there")
        eventType = eventData["eventType"]

        if eventType == "FileLoaded":
            event = FileLoaded(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["filePath"],
            )
            return event

        elif eventType == "ReconciliationWasInitialized":
            event = ReconciliationWasInitialized(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["physicalInventory"],
                payload["amortizationTable"],
            )
            return event

        elif eventType == "ProblematicLineItemsInPhysicalInventoryExtracted":
            event = ProblematicLineItemsInPhysicalInventoryExtracted(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["problematicLineItemsInPhysicalInventory"],
            )
            return event

        elif eventType == "ProblematicLineItemsInAmortizationTableExtracted":
            event = ProblematicLineItemsInAmortizationTableExtracted(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["problematicLineItemsInAmortizationTable"],
            )
            return event

        elif eventType == "MissingPhysicalInventoryLineItemsExtracted":
            event = MissingPhysicalInventoryLineItemsExtracted(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["missingPhysicalInventoryLineItems"],
            )
            return event

        elif eventType == "MissingAmortizationTableLineItemsExtracted":
            event = MissingAmortizationTableLineItemsExtracted(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["missingAmortizationTableLineItems"],
            )
            return event

        elif eventType == "StrategyWasChosen":
            event = StrategyWasChosen(
                eventData["_id"],
                eventData["reconciliationId"],
                payload["strategy"],
            )
            return event
            
        else:
            raise Exception("event type doesn't exist")
