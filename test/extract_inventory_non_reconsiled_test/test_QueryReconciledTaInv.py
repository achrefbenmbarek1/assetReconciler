from QuantityReconciliation.interactor.QueryProblematicPreviouslyReconsiledTaAndInventoryHandler import QueryProblematicPreviouslyReconsiledTaAndInventoryHandler
from QuantityReconciliation.infrastructure.query.QueryPreviouslyReconciledTaAndInventory import QueryPreviouslyReconsiledTaAndInventory
import pytest

@pytest.fixture()
def queryNonPreviouslyReconciledMergedInventoryAndTaDependency():
    return QueryPreviouslyReconsiledTaAndInventory("testSample.xlsx")

class TestQueryNonReconsiledDataExtractor:
    def test_one_non_reconsiled_data(self,queryNonPreviouslyReconciledMergedInventoryAndTaDependency):
        queryHandler = QueryProblematicPreviouslyReconsiledTaAndInventoryHandler(queryNonPreviouslyReconciledMergedInventoryAndTaDependency)
        output = queryHandler.extract()
        # expectedOutput = [[ 'Bs_4558',None,'dfkjfkj',None,'pwc',None,None,'dfjjfdfk']]
        # areEqual = output.isEqual(expectedOutput)
        assert areEqual
   
    if __name__ == '__main__':
        pytest.main()


