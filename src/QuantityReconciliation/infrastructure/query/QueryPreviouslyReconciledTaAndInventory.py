import pandas as pd
import os

class QueryPreviouslyReconsiledTaAndInventory:
    def __init__(self,fileName) -> None:
        inputFile = os.path.join("..","inputFiles",fileName)
        self.inv:pd.DataFrame = pd.read_excel(inputFile,sheet_name = "inv") 
        self.ta:pd.DataFrame = pd.read_excel(inputFile, sheet_name= "ta")
