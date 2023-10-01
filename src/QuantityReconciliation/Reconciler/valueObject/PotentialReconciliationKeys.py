class PotentialReconciliationKeys:
    def __init__(self, potentialReconciliationKeys: list[str]) -> None:
        if(any(potentialReconciliationKey not in potentialReconciliationKeys for potentialReconciliationKey in ["NumFiche", "cb", "groupe", "sousFamille", "famille"])):
            raise Exception("please make sure that you choose the NumFiche, cb , groupe, sousFamille and famille as part of your reconciliation keys")
        self.potentialReconciliationKeys = potentialReconciliationKeys
        
