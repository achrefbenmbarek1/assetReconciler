from reconciliationStrategy.valueObject.CategorisationPrecision import CategorisationPrecision
from reconciliationStrategy.valueObject.Cycle import Cycle
from reconciliationStrategy.valueObject.ReconciliationKey import ReconciliationKey
from reconciliationStrategy.valueObject.SimilarityThreshold import SimilarityThreshold

class ReconciliationStrategyDtoMapper:
    def mapToObject(self,orderedDtoCycles): 
        orderedCycles = []
        for cycle in orderedDtoCycles:
            reconciliationKeys = [ ReconciliationKey(reconciliationKey) for reconciliationKey in cycle["reconciliationKeys"]]
            orderedCycles.append(Cycle(SimilarityThreshold(cycle["SimilarityThreshold"]), CategorisationPrecision(cycle["categorisationPrecision"]), reconciliationKeys ))
        return orderedCycles

