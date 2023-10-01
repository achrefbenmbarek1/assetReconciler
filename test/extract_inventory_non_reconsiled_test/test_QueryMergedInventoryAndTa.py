import pytest
from src.QuantityReconciliation.entity.QueryMergedInventoryAndTa import QueryMergedInventoryAndTa   
import numpy as np


class TestQueryMergedInventoryAndTaDataExtractor:
    def test_with_one_non_reconsiled_data(self):
        queryMergedInventoryAndTa:QueryMergedInventoryAndTa = QueryMergedInventoryAndTa("inventory.xlsx")
        output = queryMergedInventoryAndTa.extract()
        expectedOutput:np.ndarray = np.array([['Pwc_00001', 'jfdkfj', np.nan, 'Siege', np.nan, np.nan, 'ghd', 'jfdkfj', np.nan, 'Siege', np.nan, np.nan, 'thidjkdjk'], ['Pwc_00002', 'dfkjfkj', np.nan, 'pwc', np.nan, np.nan, 'dfjjfdfkfjkf', 'dfkjfkj', np.nan, 'pwc', np.nan, np.nan, 'dfjjfdfk'], ['Pwc_0002', np.nan, np.nan, 'Siege', np.nan, np.nan, 'dfjj', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], ['Pwc_0003', 'dfkjfkj', np.nan,'Siege', np.nan, np.nan, 'dfjj', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]],dtype = object)
        assert output.isEqual(expectedOutput) 
   
    if __name__ == '__main__':
        pytest.main()

