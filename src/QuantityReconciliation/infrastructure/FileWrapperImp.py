from QuantityReconciliation.infrastructure.FileWrapper import FileWrapper
import pandas as pd

class FileWrapperImp(FileWrapper):
    def __init__(self, file) -> None:
        self.file = file
    
    def extractPhysicalInventory(self) -> list[dict]:
        return pd.read_excel(self.file.file, sheet_name='inv').to_dict(orient='records')

    def getFileName(self) -> str:
        return self.file.filename

    def extractAmortizationTable(self) -> list[dict]:
        return pd.read_excel(self.file.file, sheet_name='ta').to_dict(orient='records')
