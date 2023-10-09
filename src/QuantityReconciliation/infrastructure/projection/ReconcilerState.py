from QuantityReconciliation.Reconciler.domainEvent.DomainEvent import DomainEvent
from QuantityReconciliation.Reconciler.domainEvent.PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted import PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted
from QuantityReconciliation.Reconciler.domainEvent.MissingPhysicalInventoryLineItemsExtracted import MissingPhysicalInventoryLineItemsExtracted
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInAmortizationTableExtracted import ProblematicLineItemsInAmortizationTableExtracted
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInPhysicalInventoryExtracted import ProblematicLineItemsInPhysicalInventoryExtracted
from QuantityReconciliation.Reconciler.domainEvent.ReconciliationWasInitialized import ReconciliationWasInitialized
from QuantityReconciliation.Reconciler.domainEvent.StrategyWasChosen import StrategyWasChosen
from QuantityReconciliation.infrastructure.projection.CycleState import CycleState

class ReconciliationState:
    def __init__(self) -> None:
         self.reconciliationId:str = ""
         self.physicalInventory:list[dict]  
         self.amortizationTable:list[dict]
         self.potentialReconciliationKeys:list[str] = []
         self.reconciliationStrategyState:list[CycleState] = []
         self.version:int = -1
        
    def apply(self,event:DomainEvent):
        if(isinstance(event, ReconciliationWasInitialized)):
           self.reconciliationId = event.reconciliationId
           self.physicalInventory = event.payload["physicalInventory"]
           self.amortizationTable = event.payload["amortizationTable"]
           self.version += 1
        if(isinstance(event, StrategyWasChosen)):
            print("we're still here",self.version)
            for cycle in event.payload["strategy"]:
               self.reconciliationStrategyState.append(CycleState(cycle["similarityThreshold"], cycle["categorizationPrecision"], cycle["reconciliationKeys"], cycle["algorithm"])) 
            self.version += 1

        if(isinstance(event, ProblematicLineItemsInAmortizationTableExtracted)):
            self.version += 1
            
        if(isinstance(event, ProblematicLineItemsInPhysicalInventoryExtracted)):
            self.version += 1
        
        if(isinstance(event, PhysicalInventoryLineItemsThatTheirPreviouslyReconciledCounterpartsInAmortizationTableAreMissingWereExtracted)):
            self.version += 1
        
        if(isinstance(event, MissingPhysicalInventoryLineItemsExtracted)):
            self.version += 1
