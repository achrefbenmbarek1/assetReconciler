from abc import ABC, abstractmethod

from reconciliationStrategy.entity.ReconciliationStrategy import ReconciliationStrategy


class ReconciliationStrategyRepository(ABC):
    @abstractmethod
    def save(self,reconciliationStrategy:ReconciliationStrategy):
        pass
