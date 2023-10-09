from abc import ABC, abstractmethod


class FileWrapper(ABC):
    @abstractmethod
    def getFileName(self)-> str:
        pass

    @abstractmethod
    def extractPhysicalInventory(self)-> list[dict]:
        pass
    
    @abstractmethod
    def extractAmortizationTable(self)-> list[dict]:
        pass
