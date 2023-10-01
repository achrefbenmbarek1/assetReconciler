# from QuantityReconciliation.entity.NonPreviouslyReconciledInventoryAndTaRollingUpdate import NonPreviouslyReconciledInventoryAndTaRollingUpdate
from QuantityReconciliation.infrastructure.service.PhysicalInventoryExtractor import PhysicalInventoryExtractor
import pandas as pd


class PhysicalInventoryExtractorImp(PhysicalInventoryExtractor):
    # def findNonPreviouslyReconsiledInvAndTa(self,filePath) -> NonPreviouslyReconciledInventoryAndTaRollingUpdate:
    #     inv = pd.read_excel(filePath,sheet_name = "inv")
    #     reconciledMergedInventoryAndTa = inv[inv['NumFiche'].isna()]
    #     wrappedNonReconciledMergedInventoryAndTa = NonPreviouslyReconciledInventoryAndTaRollingUpdate(reconciledMergedInventoryAndTa)
    #     return wrappedNonReconciledMergedInventoryAndTa

    def findByFileName(self,invId):
        inventoryLineItems = pd.read_excel(invId, sheet_name = "inv").to_dict() 
        return inventoryLineItems
    
    def getKeys(self, filePath) -> list[str]:
        inv = pd.read_excel(filePath,sheet_name = "inv")
        invKeys = inv.columns.tolist()
        return invKeys



