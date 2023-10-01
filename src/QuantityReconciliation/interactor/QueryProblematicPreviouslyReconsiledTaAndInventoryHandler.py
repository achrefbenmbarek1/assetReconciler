from src.QuantityReconciliation.infrastructure.query.QueryPreviouslyReconciledTaAndInventory import QueryPreviouslyReconsiledTaAndInventory 
import pandas as pd

class QueryProblematicPreviouslyReconsiledTaAndInventoryHandler:
    def __init__(self,queryPreviouslyReconciledInventoryAndTa:QueryPreviouslyReconsiledTaAndInventory) -> None:
        self.queryNonPreviouslyReconsiledMergedInventoryAndTa = queryPreviouslyReconciledInventoryAndTa
        
    def extract(self):
        inv = self.queryNonPreviouslyReconsiledMergedInventoryAndTa.inv
        ta = self.queryNonPreviouslyReconsiledMergedInventoryAndTa.ta
        potentialReconciledMergedInv = inv[inv['NumFiche'].notnull()]
        mergedData = pd.merge(ta,potentialReconciledMergedInv,left_on="NumFiche",right_on="NumFiche",how="outer")
        problematicData:pd.DataFrame = mergedData[mergedData["cb"].isna()]
        print(problematicData)
        print(mergedData["cb"])
        print(mergedData["NumFiche"])
        problematicData.to_excel("output.xlsx")
