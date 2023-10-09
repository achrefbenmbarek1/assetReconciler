from .FileWrapper import FileWrapper
import pandas as pd

class FileWrapperImp(FileWrapper):
    def __init__(self, file) -> None:
        self.file = file
    
    def extractPhysicalInventory(self) -> list[dict]:
        df = pd.read_excel(self.file.file, sheet_name='inv')
        df = df.fillna("Missing")
        return df.to_dict(orient='records')

    def getFileName(self) -> str:
        return self.file.filename

    def extractAmortizationTable(self) -> list[dict]:
        df = pd.read_excel(self.file.file, sheet_name='ta')
        df = df.fillna("Missing")
        return df.to_dict(orient='records')
