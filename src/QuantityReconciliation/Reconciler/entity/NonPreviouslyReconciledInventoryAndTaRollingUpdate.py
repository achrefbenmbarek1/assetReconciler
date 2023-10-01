import pandas as pd
import numpy as np

class NonPreviouslyReconciledInventoryAndTaRollingUpdate:
    def __init__(self,nonReconsiledMergedInventoryAndTa:pd.DataFrame) -> None:
        self.__nonReconsiledMergedInventoryAndTa = nonReconsiledMergedInventoryAndTa

    def write(self):
        self.__nonReconsiledMergedInventoryAndTa.to_excel("output")

    def isEqual(self,expectedNonReconsiledMergedInventoryAndTaData:list) -> np.bool_:
       expectedNonReconsiledMergedInventoryAndTa = np.array(expectedNonReconsiledMergedInventoryAndTaData,dtype=object)
       testWithoutComparingTheNaNs = self.__nonReconsiledMergedInventoryAndTa.values == expectedNonReconsiledMergedInventoryAndTa
       mergedDataNumpyArrayFormat = self.__nonReconsiledMergedInventoryAndTa.to_numpy()
       testNaNCompare = pd.isnull(expectedNonReconsiledMergedInventoryAndTa) & pd.isnull(mergedDataNumpyArrayFormat)
       testWithAndWithoutNaNs = testNaNCompare | testWithoutComparingTheNaNs
       areEqual = np.all(testWithAndWithoutNaNs)
       return areEqual
    
    def debug(self):
       print(self.__nonReconsiledMergedInventoryAndTa.values)
