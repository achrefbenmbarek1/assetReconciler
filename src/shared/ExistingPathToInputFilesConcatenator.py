from abc import ABC, abstractmethod

class ExistingPathToInputFilesConcatenator(ABC):
    @abstractmethod
    def concatenateFileToPath(self, fileName:str) -> str:
        pass
