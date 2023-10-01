from QuantityReconciliation.Reconciler.Strategy.domainEvents.StrategyWasChosen import StrategyWasChosen
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
from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler
from QuantityReconciliation.infrastructure.eventStore.EventStore import EventStore
from shared.eventInfrastructure.DomainEvent import DomainEvent
from shared.eventInfrastructure.eventBus.EventBus import EventBus
import json
# from celeryConfig import celery
from tasks import buildAmortizationReadModel, buildPhysicalInventoryReadModel, buildReportReadModelOfMissingLineItemsInAmortizationTable, buildStrategyReadModel

class ReconciliationRepository(object):
    def __init__(self, eventStore: EventStore) -> None:
        self.eventStore = eventStore

    def save(self, reconciler: Reconciler):
        self.eventStore.appendEvents(
            reconciler.reconciliationState.reconciliationId,
            reconciler.domainEvents,
            reconciler.reconciliationState.version,
        )
        print("finally")
        for event in reconciler.domainEvents:
            if isinstance(event, ReconciliationWasInitialized):
                physicalInventoryReadModelData = {
                    "_id": event.reconciliationId,
                    "physicalInventoryLineItems": json.dumps(
                        event.payload["physicalInventory"]
                    ),
                }
                buildPhysicalInventoryReadModel.delay(physicalInventoryReadModelData)
                amortizationTableReadModelData = {
                    "_id": event.reconciliationId,
                    "amortizationTableLineItems": json.dumps(
                        event.payload["amortizationTable"]
                    ),
                }
                buildAmortizationReadModel.delay(amortizationTableReadModelData)
                
            elif isinstance(event, ProblematicLineItemsInPhysicalInventoryExtracted):
                problematicLineItemsInPhysicalInventory = {
                    "_id": event.reconciliationId,
                    "problematicLineItemsInPhysicalInventory": json.dumps(
                        event.payload["problematicLineItemsInPhysicalInventory"]
                    ),
                    "timestamp": event.timestamp,
                }

            elif isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                problematicLineItemsInPhysicalInventory = {
                    "_id": event.reconciliationId,
                    "problematicLineItemsInAmortizationTable": json.dumps(
                        event.payload["problematicLineItemsInAmortizationTable"]
                    ),
                    "timestamp": event.timestamp,
                }

            elif isinstance(event, MissingPhysicalInventoryLineItemsExtracted):
                missingLineItemsInPhysicalInventory = {
                    "_id": event.reconciliationId,
                    "missingLineItemsInPhysicalInventory": json.dumps(
                        event.payload["missingPhysicalInventoryLineItems"]
                    ),
                    "timestamp": event.timestamp,
                }
            elif isinstance(event, MissingAmortizationTableLineItemsExtracted):
                missingLineItemsInAmortizationTable = {
                    "_id": event.reconciliationId,
                    "missingLineItemsInAmortizationTable": json.dumps(
                        event.payload["missingAmortizationTableLineItems"]
                    ),
                    "timestamp": event.timestamp,
                }
                buildReportReadModelOfMissingLineItemsInAmortizationTable.delay(missingLineItemsInAmortizationTable)
            elif isinstance(event, StrategyWasChosen):
                strategy = {
                    "_id": event.reconciliationId,
                    "strategy": json.dumps(
                        event.payload["strategy"]
                    ),
                }
                buildStrategyReadModel.delay(strategy)

    def loadEvents(self, reconciliationId) -> list[DomainEvent]:
        return self.eventStore.loadEvents(reconciliationId)
