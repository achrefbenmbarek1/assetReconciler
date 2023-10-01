from src.QuantityReconciliation.entity.MergedInventoryAndTa import MergedInventoryAndTa
import pytest
from src.QuantityReconciliation.entity.QueryMergedInventoryAndTa import QueryMergedInventoryAndTa
import numpy as np

@pytest.fixture()
def testMergedInventoryAndTaDependency() -> MergedInventoryAndTa:
    queryMergedInventoryAndTa:QueryMergedInventoryAndTa = QueryMergedInventoryAndTa("inventory.xlsx")
    mergedInventoryAndTa:MergedInventoryAndTa = queryMergedInventoryAndTa.extract()
    return mergedInventoryAndTa

class TestQueryNonReconsiledDataExtractor:
    def test_one_non_reconsiled_data(self,testMergedInventoryAndTaDependency):
        output = testMergedInventoryAndTaDependency.filterNotReconsiledData()
        expectedOutput = np.array(['Pwc_0002',np.NaN,np.NaN,'Siege',np.NaN,np.NaN,'dfjj',np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN],dtype=object)
        areEqual = output.isEqual(expectedOutput)
        assert areEqual
   
    if __name__ == '__main__':
        pytest.main()
