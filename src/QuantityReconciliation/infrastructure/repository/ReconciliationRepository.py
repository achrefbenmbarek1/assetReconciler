from QuantityReconciliation.Reconciler.domainEvent.DomainEvent import DomainEvent
from QuantityReconciliation.Reconciler.domainEvent.MissingPhysicalInventoryLineItemsExtracted import (
    MissingPhysicalInventoryLineItemsExtracted,
)
from QuantityReconciliation.Reconciler.domainEvent.PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted import (
    PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted,
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
from QuantityReconciliation.Reconciler.domainEvent.StrategyWasChosen import (
    StrategyWasChosen,
)
from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler
from QuantityReconciliation.infrastructure.eventStore.EventStore import EventStore
import json

# from celeryConfig import celery
from tasks import (
    buildAmortizationReadModel,
    buildPhysicalInventoryReadModel,
    buildReportReadModelOfMissingLineItemsInAmortizationTable,
    buildReportReadModelOfMissingLineItemsInPhysicalInventory,
    buildReportReadModelOfProblematicLineItemsInAmortizationTable,
    buildReportReadModelOfProblematicLineItemsInPhysicalInventory,
    buildStrategyCreatorPage,
    buildStrategyReadModel,
)


class ReconciliationRepository(object):
    def __init__(self, eventStore: EventStore) -> None:
        self.eventStore = eventStore

    def save(self, reconciler: Reconciler):
        self.eventStore.appendEvents(
            reconciler.reconciliationState.reconciliationId,
            reconciler.domainEvents,
            reconciler.reconciliationState.version,
        )
        print("here we go again")

        for event in reconciler.domainEvents:
            if isinstance(event, ReconciliationWasInitialized):
                physicalInventoryReadModelData = {
                    "_id": event.reconciliationId,
                    "physicalInventoryLineItems": json.dumps(
                        event.payload["physicalInventory"]
                    ),
                }
                physicalInventoryData = event.payload["physicalInventory"]
                potentialKeys = physicalInventoryData[0].keys() if physicalInventoryData else []
                print("potential keys", potentialKeys)

                strategyPotentialKeys = {
                    "_id": event.reconciliationId,
                    "strategyPotentialKeys": list(potentialKeys),
                }
                buildPhysicalInventoryReadModel.delay(physicalInventoryReadModelData)
                buildStrategyCreatorPage.delay(strategyPotentialKeys)
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
                buildReportReadModelOfProblematicLineItemsInPhysicalInventory.delay(
                    problematicLineItemsInPhysicalInventory
                )

            elif isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                problematicLineItemsInAmortizationTable = {
                    "_id": event.reconciliationId,
                    "problematicLineItemsInAmortizationTable": json.dumps(
                        event.payload["problematicLineItemsInAmortizationTable"]
                    ),
                    "timestamp": event.timestamp,
                }
                buildReportReadModelOfProblematicLineItemsInAmortizationTable.delay(
                    problematicLineItemsInAmortizationTable
                )

            elif isinstance(event, MissingPhysicalInventoryLineItemsExtracted):
                missingLineItemsInPhysicalInventory = {
                    "_id": event.reconciliationId,
                    "missingLineItemsInPhysicalInventory": json.dumps(
                        event.payload["missingPhysicalInventoryLineItems"]
                    ),
                    "timestamp": event.timestamp,
                }
                buildReportReadModelOfMissingLineItemsInPhysicalInventory.delay(
                    missingLineItemsInPhysicalInventory
                )

            elif isinstance(
                event,
                PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted,
            ):
                missingLineItemsInAmortizationTable = {
                    "_id": event.reconciliationId,
                    "missingLineItemsInAmortizationTable": json.dumps(
                        event.payload["missingAmortizationTableLineItems"]
                    ),
                    "timestamp": event.timestamp,
                }
                buildReportReadModelOfMissingLineItemsInAmortizationTable.delay(
                    missingLineItemsInAmortizationTable
                )

            elif isinstance(event, StrategyWasChosen):
                strategy = {
                    "_id": event.reconciliationId,
                    "strategy": json.dumps(event.payload["strategy"]),
                }
                buildStrategyReadModel.delay(strategy)

    def loadEvents(self, reconciliationId) -> list[DomainEvent]:
        return self.eventStore.loadEvents(reconciliationId)
