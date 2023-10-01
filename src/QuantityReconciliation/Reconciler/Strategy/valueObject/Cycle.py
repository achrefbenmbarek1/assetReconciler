from reconciliationStrategy.valueObject.CategorisationPrecision import CategorisationPrecision
from reconciliationStrategy.valueObject.ReconciliationKey import ReconciliationKey
from reconciliationStrategy.valueObject.SimilarityThreshold import SimilarityThreshold


class Cycle:
    def __init__(self, similarityThreshold:SimilarityThreshold,categorisationPrecision:CategorisationPrecision, reconciliationKeys:list[ReconciliationKey]) -> None:
        self.similarityThreshold = similarityThreshold
        self.categorizationPrecision = categorisationPrecision
        self.reconciliationKeys = reconciliationKeys

    def toDict(self):
        return {
                "similarityThreshold":self.similarityThreshold.percentage,
                "categorisationPrecision": self.categorizationPrecision.categorizationType,
                "reconciliationKeys": [reconciliationKey.reconciliationKey for reconciliationKey in self.reconciliationKeys]
                }
