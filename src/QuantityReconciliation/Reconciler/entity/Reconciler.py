from QuantityReconciliation.Reconciler.domainEvent.DomainEvent import DomainEvent
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
from QuantityReconciliation.Reconciler.domainEvent.StrategyWasChosen import StrategyWasChosen
from QuantityReconciliation.infrastructure.command.CreateStrategy import CreateStrategy
from QuantityReconciliation.infrastructure.command.InitializeReconciliation import (
    InitializeReconciliation,
)
from QuantityReconciliation.infrastructure.projection.ReconcilerState import (
    ReconciliationState,
)

class Reconciler:
    reconciliationState: ReconciliationState

    def __init__(self, events: list[DomainEvent]) -> None:
        self.reconciliationState = ReconciliationState()
        self.domainEvents: list[DomainEvent] = []
        for event in events:
            self.reconciliationState.apply(event)
            print("this is the last resort", len(self.domainEvents))

    def appendEvent(self, event: DomainEvent):
        self.domainEvents.append(event)
        self.reconciliationState.apply(event)
        if isinstance(event, StrategyWasChosen):
            self.applyStrategy()

    def initializeReconciliation(
        self, initializeReconciliation: InitializeReconciliation
    ):
        if self.reconciliationState.reconciliationId:
            raise Exception("reconciliation already initialized")

        physicalInventoryLineItems = [
            physicalLineItem
            for physicalLineItem in initializeReconciliation.physcialInventoryLineItems
            if physicalLineItem["cb"] != "Missing"
        ]
        
        problematicLineItemsInPhysicalInventory = [
            physicalInventoryLineItem
            for physicalInventoryLineItem in initializeReconciliation.physcialInventoryLineItems
            if (
                physicalInventoryLineItem["cb"] == "Missing"
                or physicalInventoryLineItem["cb"] == ""
            )
        ]

        amortizationTableLineItems = [
            amortizationTableLineItem
            for amortizationTableLineItem in initializeReconciliation.amortizationTable
            if amortizationTableLineItem["NumFiche"] != "Missing"
        ]

        problematicLineItemsInAmortizationTable = [
            amortizationTableLineItem
            for amortizationTableLineItem in initializeReconciliation.amortizationTable
            if amortizationTableLineItem["NumFiche"] == "Missing"
            or amortizationTableLineItem["NumFiche"] == ""
        ]

        numFicheInPhysicalInventory = set(
            physicalInventoryLineItem["NumFiche"]
            for physicalInventoryLineItem in physicalInventoryLineItems
            if (physicalInventoryLineItem["NumFiche"] != "Missing")
        )

        numFicheInAmortizationTable = set(
            amortizationTableLineItem["NumFiche"]
            for amortizationTableLineItem in amortizationTableLineItems
        )

        numFichesOfMissingLineItemsInAmortizationTable = (
            numFicheInPhysicalInventory - numFicheInAmortizationTable
        )
        physicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissing = [
            physicalInventoryLineItem
            for physicalInventoryLineItem in physicalInventoryLineItems
            if physicalInventoryLineItem["NumFiche"]
            in numFichesOfMissingLineItemsInAmortizationTable
        ]

        readyToBeReconciledLineItemsInPhysicalInventory = [
            physicalInventoryLineItem
            for physicalInventoryLineItem in physicalInventoryLineItems
            if physicalInventoryLineItem["NumFiche"]
            not in numFichesOfMissingLineItemsInAmortizationTable
        ]
        reconciliationWasInitialized = ReconciliationWasInitialized(
            initializeReconciliation.eventsIds[0],
            initializeReconciliation.reconciliationId,
            readyToBeReconciledLineItemsInPhysicalInventory,
            amortizationTableLineItems,
        )

        physicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted = PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted(
            initializeReconciliation.eventsIds[1],
            initializeReconciliation.reconciliationId,
            physicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissing,
        )


        problematicLineItemsInPhysicalInventoryExtracted = (
            ProblematicLineItemsInPhysicalInventoryExtracted(
                initializeReconciliation.eventsIds[2],
                initializeReconciliation.reconciliationId,
                problematicLineItemsInPhysicalInventory,
            )
        )

        problematicLineItemsInAmortizationTableExtracted = (
            ProblematicLineItemsInAmortizationTableExtracted(
                initializeReconciliation.eventsIds[3],
                initializeReconciliation.reconciliationId,
                problematicLineItemsInAmortizationTable,
            )
        )
        self.appendEvent(reconciliationWasInitialized)
        self.appendEvent(
            physicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted
        )
        self.appendEvent(problematicLineItemsInPhysicalInventoryExtracted)
        self.appendEvent(problematicLineItemsInAmortizationTableExtracted)

    def createStrategy(self, createStrategy: CreateStrategy):
        if self.reconciliationState.version == -1:
            raise Exception("The reconciliation need to be initialized at first")

        if createStrategy.orderedCycles == []:
            raise Exception("a strategy must have at least one cycle")

        previousCycle = createStrategy.orderedCycles[0]
        for cycle in createStrategy.orderedCycles:
            if cycle["similarityThreshold"] > 100 or cycle["similarityThreshold"] < 0:
                raise Exception("invalid percentage it should be between 0 and 100")

            validKeys = ["intitule", "marque", "model", "fournisseur"]
            if any(key not in validKeys for key in cycle["reconciliationKeys"]):
                raise Exception("Invalid reconciliation key")

            if cycle["categorizationPrecision"] not in (
                "groupe",
                "famille",
                "sousFamille",
            ):
                raise Exception("invalid categorization")

            if cycle["algorithm"] not in ("Levenshtein, Sorensen, Jaccard"):
                raise Exception(
                    "algorithm not supported yet, what we currently support is: (Levenshtein, Sorensen, Jaccard)"
                )

            previousSimilarityThreshold = previousCycle["similarityThreshold"]
            previousCategorisationPrecision = previousCycle["categorizationPrecision"]
            previousReconciliationKeys = previousCycle["reconciliationKeys"]

            if cycle["similarityThreshold"] > previousSimilarityThreshold:
                raise Exception(
                    "similarity threshold should be decreasing or at the very least equal to the one of the previous cycle"
                )

            possibleCategorisations = ("groupe", "famille", "sousFamille")
            if possibleCategorisations.index(
                cycle["categorizationPrecision"]
            ) > possibleCategorisations.index(previousCategorisationPrecision):
                raise Exception(
                    "categorisation should be decreasing or at the very least equal to the one of the previous cycle"
                )

            if len(cycle["reconciliationKeys"]) > len(previousReconciliationKeys):
                raise Exception(
                    "reconciliation keys number should be declining or the very least equal to the one of the previous cycle"
                )
            previousCycle = cycle
        strategyWasChosen = StrategyWasChosen(
            createStrategy.eventId,
            self.reconciliationState.reconciliationId,
            createStrategy.orderedCycles,
        )
        self.appendEvent(strategyWasChosen)

    def applyStrategy(self):
        pass
