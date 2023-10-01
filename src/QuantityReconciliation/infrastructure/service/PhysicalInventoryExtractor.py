from abc import ABC, abstractmethod

# from QuantityReconciliation.entity.NonPreviouslyReconciledInventoryAndTaRollingUpdate import NonPreviouslyReconciledInventoryAndTaRollingUpdate

class PhysicalInventoryExtractor(ABC):
#     @abstractmethod
#     def findNonPreviouslyReconsiledInvAndTa(self, filePath:str) -> NonPreviouslyReconciledInventoryAndTaRollingUpdate:
#         pass
    
    @abstractmethod
    def findByFileName(self, invId:str):
        pass
    
    @abstractmethod
    def getKeys(self, invId:str) -> list[str]:
        pass
