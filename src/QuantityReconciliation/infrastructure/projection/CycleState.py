class CycleState(object):
    def __init__(self, similarityThreshold:int, categorizationPrecision:str, reconciliationKeys:list[str], algorithm:str) -> None:
        self.similarityThreshold = similarityThreshold 
        self.categorizationPrecision = categorizationPrecision
        self.reconciliationKeys = reconciliationKeys 
        self.algorithm = algorithm
