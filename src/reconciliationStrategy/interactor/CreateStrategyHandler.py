from reconciliationStrategy.entity.ReconciliationStrategy import ReconciliationStrategy
from reconciliationStrategy.infrastructure.dto.command.CreateStrategy import CreateStrategy
from reconciliationStrategy.infrastructure.repository.ReconciliationStrategyRepository import ReconciliationStrategyRepository
from reconciliationStrategy.infrastructure.service.ReconciliationStrategyDtoMapper import ReconciliationStrategyDtoMapper
from reconciliationStrategy.valueObject.Cycle import Cycle
import json


class CreateStrategyHandler:
    def __init__(self,reconciliationStrategyRepository:ReconciliationStrategyRepository, messageBus) -> None:
        self.reconciliationStrategyRepository = reconciliationStrategyRepository
        self.messageBus = messageBus
        
    def createStrategy(self, createStrategy: CreateStrategy):
        reconciliationStrategyDtoMapper: ReconciliationStrategyDtoMapper = ReconciliationStrategyDtoMapper()
        orderedCycles:list[Cycle] = reconciliationStrategyDtoMapper.mapToObject(createStrategy.orderedCycles)
        reconciliationStrategy:ReconciliationStrategy = ReconciliationStrategy(orderedCycles)
        self.reconciliationStrategyRepository.save(reconciliationStrategy)
        unpublishedDomainEvents = reconciliationStrategy.unpublishedDomainEvents
        for unpublishedDomainEvent in unpublishedDomainEvents:
              # self.messageBus.publish(unpublishedDomainEvent)
              self.messageBus.publish("reconciliation_events", json.dumps(unpublishedDomainEvent.__dict__) )

            
