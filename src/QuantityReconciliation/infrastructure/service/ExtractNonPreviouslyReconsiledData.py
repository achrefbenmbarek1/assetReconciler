from abc import ABC, abstractmethod

class QueryNonPreviouslyReconsiledData(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def unexecute(self):
        pass

