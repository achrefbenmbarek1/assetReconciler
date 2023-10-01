from QuantityReconciliation.infrastructure.command.ReconcileByQuantityNonPreviouslyReconsiledInvAndTa import ReconcileByQuantityNonPreviouslyReconciledInvAndTa
from QuantityReconciliation.infrastructure.repository.InvRepository import InvRepository
from shared.ExistingPathToInputFilesConcatenator import ExistingPathToInputFilesConcatenator
from src.QuantityReconciliation.entity.NonPreviouslyReconciledInventoryAndTaRollingUpdate import NonPreviouslyReconciledInventoryAndTaRollingUpdate 

class NonPreviouslyReconciledInvAndTaQuantityReconciler:
    def __init__(self, reconcileByQuantityNonPreviouslyReconciledInvAndTa:ReconcileByQuantityNonPreviouslyReconciledInvAndTa,existingPathToInputFilesConcatenator:ExistingPathToInputFilesConcatenator,invRepository:InvRepository
         ) -> None:
        self.queryNonPreviouslyReconsiledMergedInventoryAndTa = reconcileByQuantityNonPreviouslyReconciledInvAndTa
        self.existingPathToInputFilesConcatenator = existingPathToInputFilesConcatenator
        self.invRepository = invRepository
        
    def reconsilateByQuantity(self) -> None:
        fileName = self.queryNonPreviouslyReconsiledMergedInventoryAndTa.fileName
        invPath = self.existingPathToInputFilesConcatenator.concatenateFileToPath(fileName)
        nonReconciledMergedInventoryAndTa:NonPreviouslyReconciledInventoryAndTaRollingUpdate = self.invRepository.findNonPreviouslyReconsiledInvAndTa(invPath)
        
        

