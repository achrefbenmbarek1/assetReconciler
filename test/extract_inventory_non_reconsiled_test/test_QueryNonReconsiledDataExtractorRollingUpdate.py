from QuantityReconciliation.infrastructure.repository.InvRepositoryImp import InvRepositoryImp
from QuantityReconciliation.interactor.QueryNonPreviouslyReconsiledTaAndInventoryHandler import QueryNonPreviouslyReconsiledTaAndInventoryHandler
from QuantityReconciliation.infrastructure.query.QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate import QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate
import pytest
from shared.ExistingPathToInputFilesConcatenatorImp import ExistingPathToInputFilesConcatenatorImp

@pytest.fixture()
def queryNonPreviouslyReconciledMergedInventoryAndTaDependency():
    return QueryNonPreviouslyReconciledTaAndInventoryRollingUpdate("testSample.xlsx")

@pytest.fixture()
def invRepositoryDependency():
    return InvRepositoryImp()

@pytest.fixture()
def exitingPathToInputFilesConcatenatorDependency():
    return ExistingPathToInputFilesConcatenatorImp()

class TestQueryNonReconsiledDataExtractor:
    def test_one_non_reconsiled_data(self,queryNonPreviouslyReconciledMergedInventoryAndTaDependency, exitingPathToInputFilesConcatenatorDependency, invRepositoryDependency):
        queryHandler = QueryNonPreviouslyReconsiledTaAndInventoryHandler(queryNonPreviouslyReconciledMergedInventoryAndTaDependency,exitingPathToInputFilesConcatenatorDependency,invRepositoryDependency)
        output = queryHandler.extract()
        expectedOutput = [[ 'Bs_4558',None,'dfkjfkj',None,'pwc',None,None,'dfjjfdfk']]
        output.debug()
        areEqual = output.isEqual(expectedOutput)
        assert areEqual
   
    if __name__ == '__main__':
        pytest.main()

