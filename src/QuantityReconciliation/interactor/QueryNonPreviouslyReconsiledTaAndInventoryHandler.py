from QuantityReconciliation.infrastructure.repository.InvRepository import InvRepository
from shared.ExistingPathToInputFilesConcatenator import ExistingPathToInputFilesConcatenator
from src.QuantityReconciliation.entity.NonPreviouslyReconciledInventoryAndTaRollingUpdate import NonPreviouslyReconciledInventoryAndTaRollingUpdate 
from src.QuantityReconciliation.infrastructure.query.QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate import QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate

class QueryNonPreviouslyReconsiledTaAndInventoryHandler:
    def __init__(self,queryNonPreviouslyReconciledInventoryAndTa:QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate,existingPathToInputFilesConcatenator:ExistingPathToInputFilesConcatenator,invRepository:InvRepository
         ) -> None:
        self.queryNonPreviouslyReconsiledMergedInventoryAndTa = queryNonPreviouslyReconciledInventoryAndTa
        self.existingPathToInputFilesConcatenator = existingPathToInputFilesConcatenator
        self.invRepository = invRepository
        
    def extract(self) -> NonPreviouslyReconciledInventoryAndTaRollingUpdate:
        fileName = self.queryNonPreviouslyReconsiledMergedInventoryAndTa.fileName
        invPath = self.existingPathToInputFilesConcatenator.concatenateFileToPath(fileName)
        nonReconciledMergedInventoryAndTa = self.invRepository.findNonPreviouslyReconsiledInvAndTa(invPath)
        return nonReconciledMergedInventoryAndTa
