from QuantityReconciliation.entity.NonReconciledMergedInventoryAndTa import NonReconciledMergedInventoryAndTa
import pandas as pd
import numpy as np

class MergedInventoryAndTa:
    def __init__(self,mergedDataFrames:pd.DataFrame) -> None:
        self.__mergedDataFrames = mergedDataFrames
    
    def filterNotReconsiledData(self) -> NonReconciledMergedInventoryAndTa:
        notReconciledDataDf = self.__mergedDataFrames[self.__mergedDataFrames["Descriptif_x"].isna()]
        notReconciledData = NonReconciledMergedInventoryAndTa(notReconciledDataDf)
        return notReconciledData

    def isEqual(self,expectedMergedData:np.ndarray) -> np.bool_:
       testWithoutComparingTheNaNs = self.__mergedDataFrames.values == expectedMergedData
       mergedDataNumpyArrayFormat = self.__mergedDataFrames.to_numpy()
       testNaNCompare = pd.isnull(expectedMergedData) & pd.isnull(mergedDataNumpyArrayFormat)
       testWithAndWithoutNaNs = testNaNCompare | testWithoutComparingTheNaNs
       areEqual = np.all(testWithAndWithoutNaNs)
       return areEqual


    def debugging(self):
       print(self.__mergedDataFrames.to_numpy())
