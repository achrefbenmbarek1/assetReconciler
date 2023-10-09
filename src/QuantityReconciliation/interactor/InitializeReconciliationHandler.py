from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler
from QuantityReconciliation.infrastructure.command.InitializeReconciliation import InitializeReconciliation
from QuantityReconciliation.infrastructure.repository.ReconciliationRepository import ReconciliationRepository
from QuantityReconciliation.infrastructure.service.FileWrapper import FileWrapper
from QuantityReconciliation.infrastructure.service.IdGenerator import IdGenerator



class InitializeReconciliationHandler:
    def __init__(self, reconciliationRepository:ReconciliationRepository, idGenerator:IdGenerator, fileWrapper:FileWrapper) -> None:
       self.reconciliationRepository = reconciliationRepository
       self.idGenerator = idGenerator
       self.fileWrapper = fileWrapper

    def initializeReconciliation(self):
        if self.fileWrapper.getFileName() is None:
            raise Exception("file must have a filename")
        domainEvents = self.reconciliationRepository.loadEvents(self.fileWrapper.getFileName())
        if len(domainEvents) > 0:
            raise Exception("you can't initialize an already initialized reconciliation")
        physicalInventory = self.fileWrapper.extractPhysicalInventory()
        amortizationTable = self.fileWrapper.extractAmortizationTable()
        print(physicalInventory)
        reconciler:Reconciler = Reconciler(domainEvents)
        eventIds = [self.idGenerator.generateId() for _ in range(4)]
        initializeReconiliation = InitializeReconciliation(self.fileWrapper.getFileName(), physicalInventory, amortizationTable, eventIds)
        reconciler.initializeReconciliation(initializeReconiliation)
        self.reconciliationRepository.save(reconciler)
        
