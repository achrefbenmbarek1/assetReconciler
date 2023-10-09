
from QuantityReconciliation.Reconciler.entity.Reconciler import Reconciler
from QuantityReconciliation.infrastructure.command.CreateAndApplyStrategy import CreateAndApplyStrategy
from QuantityReconciliation.infrastructure.command.CreateStrategy import CreateStrategy
from QuantityReconciliation.infrastructure.repository.ReconciliationRepository import ReconciliationRepository
from QuantityReconciliation.infrastructure.service.IdGenerator import IdGenerator



class CreateAndApplyStrategyHandler:
    def __init__(self, reconciliationRepository:ReconciliationRepository, idGenerator:IdGenerator) -> None:
       self.reconciliationRepository = reconciliationRepository
       self.idGenerator = idGenerator


    def createAndApplyStrategy(self, createAndApplyStrategyCmd:CreateAndApplyStrategy):
        print("this is the second print",createAndApplyStrategyCmd.reconciliationId)
        currentDomainEvents = self.reconciliationRepository.loadEvents(createAndApplyStrategyCmd.reconciliationId)
        print("this is the len", len(currentDomainEvents))
        reconciler:Reconciler = Reconciler(currentDomainEvents)
        print("please",len(reconciler.domainEvents))
        print("or event better", reconciler.reconciliationState.version)
        eventId = self.idGenerator.generateId()
        createStrategy: CreateStrategy = CreateStrategy(createAndApplyStrategyCmd.orderedCycles, eventId)
        reconciler.createStrategy(createStrategy)
        self.reconciliationRepository.save(reconciler)
