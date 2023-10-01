from QuantityReconciliation.Reconciler.Strategy.domainEvents.StrategyWasChosen import StrategyWasChosen
from QuantityReconciliation.Reconciler.domainEvent.MissingAmortizationTableLineItemsExtracted import MissingAmortizationTableLineItemsExtracted
from QuantityReconciliation.Reconciler.domainEvent.MissingPhysicalInventoryLineItemsExtracted import MissingPhysicalInventoryLineItemsExtracted
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInAmortizationTableExtracted import ProblematicLineItemsInAmortizationTableExtracted
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInPhysicalInventoryExtracted import ProblematicLineItemsInPhysicalInventoryExtracted
from QuantityReconciliation.Reconciler.domainEvent.ReconciliationWasInitialized import ReconciliationWasInitialized
from QuantityReconciliation.infrastructure.command.InitializeReconciliation import InitializeReconciliation
from QuantityReconciliation.infrastructure.projection.ReconcilerState import ReconciliationState
from reconciliationStrategy.infrastructure.dto.command.CreateStrategy import CreateStrategy
from shared.eventInfrastructure.DomainEvent import DomainEvent


class Reconciler:
    domainEvents:list[DomainEvent] = list()
    reconciliationState:ReconciliationState
    
    def __init__(self,events:list[DomainEvent]) -> None:
        self.reconciliationState = ReconciliationState()
        for event in events:
            self.reconciliationState.apply(event)
    
    def appendEvent(self,event:DomainEvent):
        self.domainEvents.append(event)
        self.reconciliationState.apply(event)
        if isinstance(event,StrategyWasChosen):
            self.applyStrategy()

    def initializeReconciliation(self, initializeReconciliation:InitializeReconciliation ):
        if self.reconciliationState.reconciliationId:
            raise Exception('reconciliation already initialized')
        
        physicalInventoryLineItems = [physicalLineItem for physicalLineItem in initializeReconciliation.physcialInventoryLineItems if physicalLineItem["cb"] is not None and physicalLineItem["cb"] != '']
        print("we're just before the problematic")
        problematicLineItemsInPhysicalInventory = [physicalInventoryLineItem for physicalInventoryLineItem in initializeReconciliation.physcialInventoryLineItems if physicalInventoryLineItem["cb"] is None and physicalInventoryLineItem["cb"] == '']
        
        amortizationTableLineItems = [amortizationTableLineItem for amortizationTableLineItem in initializeReconciliation.amortizationTable if amortizationTableLineItem["NumFiche"] is not None and amortizationTableLineItem["NumFiche"] != '']
        
        problematicLineItemsInAmortizationTable = [amortizationTableLineItem for amortizationTableLineItem in initializeReconciliation.amortizationTable if amortizationTableLineItem["NumFiche"] is not None and amortizationTableLineItem["NumFiche"] != '']
        
        NumFicheInPhysicalInventory = set(physicalInventoryLineItem["NumFiche"] for physicalInventoryLineItem in physicalInventoryLineItems if physicalInventoryLineItem["NumFiche"] is not None and physicalInventoryLineItem["NumFiche"] != "")

        NumFicheInAmortizationTable = set(amortizationTableLineItem["NumFiche"] for amortizationTableLineItem in amortizationTableLineItems)
        
        missingProductsInThePhysicalInventory = [amortizationTableLineItem for amortizationTableLineItem in amortizationTableLineItems if amortizationTableLineItem["NumFiche"] in NumFicheInAmortizationTable - NumFicheInPhysicalInventory]
        
        missingProductsInTheAmortizationTable = [physicalInventoryLineItem for physicalInventoryLineItem in physicalInventoryLineItems if physicalInventoryLineItem["NumFiche"] in NumFicheInAmortizationTable - NumFicheInPhysicalInventory]
        print("are we just before initializing Events")
        reconciliationWasInitialized = ReconciliationWasInitialized(initializeReconciliation.eventsIds[0], initializeReconciliation.reconciliationId, physicalInventoryLineItems,initializeReconciliation.amortizationTable)
        
        print("did we initialize the reconciliation")
        missingProductsInAmortizationTableLineItemsExtracted = MissingAmortizationTableLineItemsExtracted(initializeReconciliation.eventsIds[1], initializeReconciliation.reconciliationId, missingProductsInTheAmortizationTable)
        
        missingProductsInPhysicalInventoryLineItemsExtracted = MissingPhysicalInventoryLineItemsExtracted(initializeReconciliation.eventsIds[2], initializeReconciliation.reconciliationId, missingProductsInThePhysicalInventory)
        
        problematicLineItemsInPhysicalInventoryExtracted = ProblematicLineItemsInPhysicalInventoryExtracted(initializeReconciliation.eventsIds[3], initializeReconciliation.reconciliationId, problematicLineItemsInPhysicalInventory)
        
        problematicLineItemsInAmortizationTableExtracted = ProblematicLineItemsInAmortizationTableExtracted(initializeReconciliation.eventsIds[4], initializeReconciliation.reconciliationId, problematicLineItemsInAmortizationTable)
        self.appendEvent(reconciliationWasInitialized)
        self.appendEvent(missingProductsInAmortizationTableLineItemsExtracted)
        self.appendEvent(missingProductsInPhysicalInventoryLineItemsExtracted)
        self.appendEvent(problematicLineItemsInPhysicalInventoryExtracted)
        self.appendEvent(problematicLineItemsInAmortizationTableExtracted)
        
        
    def createStrategy(self, createStrategy:CreateStrategy):
        if createStrategy.orderedCycles == []:
            raise Exception("a strategy must have at least one cycle")
        
        previousCycle = createStrategy.orderedCycles[0] 
        for cycle in createStrategy.orderedCycles:
            if cycle["similarityThreshold"] > 100 or cycle["similarityThreshold"] < 0:
                raise Exception("invalid percentage it should be between 0 and 100")
            
            validKeys = ["intitule", "marque", "model", "fournisseur"]
            if any(key not in validKeys for key in cycle["reconciliationKeys"]):
                raise Exception("Invalid reconciliation key")
            
            if cycle["categorizationPrecision"] not in ("groupe", "famille", "sousFamille"):
                raise Exception("invalid categorization")
            
            if cycle["algorithm"] not in ("Levenshtein, Sorensen, Jaccard"):
                raise Exception("algorithm not supported yet, what we currently support is: (Levenshtein, Sorensen, Jaccard)")
            
            previousSimilarityThreshold = previousCycle["similarityThreshold"]
            previousCategorisationPrecision = previousCycle["categorizationPrecision"]
            previousReconciliationKeys = previousCycle["reconciliationKeys"]
            
            if cycle["similarityThreshold"] > previousSimilarityThreshold :
                raise Exception("similarity threshold should be decreasing or at the very least equal to the one of the previous cycle")
             
            # if cycle["categorizationPrecision"].islessSpecif(previousCategorisationPrecision): 
            #     raise Exception("categorisation should be decreasing or at the very least equal to the one of the previous cycle")
            
            possibleCategorisations = ("groupe", "famille", "sousFamille")
            if possibleCategorisations.index(cycle["categorizationPrecision"]) > possibleCategorisations.index(previousCategorisationPrecision): 
                raise Exception("categorisation should be decreasing or at the very least equal to the one of the previous cycle")

            if len(cycle["reconciliationKeys"]) > len(previousReconciliationKeys):
                raise Exception("reconciliation keys number should be declining or the very least equal to the one of the previous cycle")
            previousCycle = cycle
        strategyWasChosen = StrategyWasChosen(createStrategy.eventId, self.reconciliationState.reconciliationId ,createStrategy.orderedCycles) 
        self.appendEvent(strategyWasChosen)
        
        
    def applyStrategy(self):
        pass
