
from reconciliationStrategy.domainEvents.StrategyWasChosen import StrategyWasChosen
from reconciliationStrategy.infrastructure.service.IdGenerator import IdGenerator
from reconciliationStrategy.valueObject.CategorisationPrecision import CategorisationPrecision
from reconciliationStrategy.valueObject.Cycle import Cycle
from reconciliationStrategy.valueObject.ReconciliationKey import ReconciliationKey
from reconciliationStrategy.valueObject.SimilarityThreshold import SimilarityThreshold
from shared.eventInfrastructure.DomainEvent import DomainEvent


class ReconciliationStrategy:
    def __init__(self, orderedCycles:list[Cycle],version = 0) -> None:
        self.id = IdGenerator.generateId() 
        self.orderedCycles = orderedCycles
        self.unpublishedDomainEvents:list[DomainEvent] = []
        self.version = version



    def chooseStrategy(self):
        if self.orderedCycles == []:
            raise Exception("a strategy must have at least one cycle")
        
        previousCycle:Cycle = self.orderedCycles[0] 
        for cycle in self.orderedCycles:
            previousSimilarityThreshold : SimilarityThreshold = previousCycle.similarityThreshold
            previousCategorisationPrecision : CategorisationPrecision = previousCycle.categorizationPrecision
            previousReconciliationKeys:list[ReconciliationKey] = previousCycle.reconciliationKeys
            if cycle.similarityThreshold > previousSimilarityThreshold :
                raise Exception("similarity threshold should be decreasing or at the very least equal to the one of the previous cycle")
             
            if cycle.categorizationPrecision.islessSpecif(previousCategorisationPrecision): 
                raise Exception("categorisation should be decreasing or at the very least equal to the one of the previous cycle")

            if len(cycle.reconciliationKeys) > len(previousReconciliationKeys):
                raise Exception("reconciliation keys number should be declining or the very least equal to the one of the previous cycle")
            
        self.unpublishedDomainEvents.append(StrategyWasChosen(IdGenerator.generateId(), self.id, self.orderedCycles))
        self.version += 1
        
    def toDict(self):   
        return {
                "orderedCycles" : [cycle.toDict() for cycle in self.orderedCycles],
                "_id": self.id
                }
