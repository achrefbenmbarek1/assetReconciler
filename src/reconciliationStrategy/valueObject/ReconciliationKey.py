class ReconciliationKey:
    def __init__(self, reconciliationKey:str) -> None:
        if reconciliationKey not in ("intitule", "marque", "modele", "fournisseur"):
            raise Exception("invalid reconciliation key")
        self.reconciliationKey = reconciliationKey

