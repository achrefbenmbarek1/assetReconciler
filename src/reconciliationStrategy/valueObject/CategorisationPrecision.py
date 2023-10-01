

class CategorisationPrecision:
    def __init__(self, categorizationType) -> None:
        if categorizationType not in ("groupe", "famille", "sous famille"):
            raise Exception("invalid categorization")
        self.categorizationType = categorizationType

    def islessSpecif(self,otherCategorizationPrecision:"CategorisationPrecision") -> bool:
            possibleCategorisations = ("groupe", "famille", "sous famille")
            return possibleCategorisations.index(self.categorizationType) < possibleCategorisations.index(otherCategorizationPrecision.categorizationType) 
