from QuantityReconciliation.entity.NonPreviouslyReconciledInventoryAndTaRollingUpdate import NonPreviouslyReconciledInventoryAndTaRollingUpdate
from QuantityReconciliation.infrastructure.query.QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate import QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate


class ExtractNonPreviouslyReconsiledDataImp:
    def __init__(self,queryNonPreviouslyReconsiledMergedInventoryAndTa:QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate) -> None:
       self.queryNonPreviouslyReconsiledData = queryNonPreviouslyReconsiledMergedInventoryAndTa
    def extract(self) -> NonPreviouslyReconciledInventoryAndTaRollingUpdate:
        inv = self.queryNonPreviouslyReconsiledData.inv
        reconciledMergedInventoryAndTa = inv[inv['NumFiche'].isna()]
        wrappedNonReconciledMergedInventoryAndTa = NonPreviouslyReconciledInventoryAndTaRollingUpdate(reconciledMergedInventoryAndTa)
        return wrappedNonReconciledMergedInventoryAndTa

