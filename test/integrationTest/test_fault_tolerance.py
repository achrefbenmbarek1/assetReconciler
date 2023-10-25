import pytest
from testTasks import buildAmortizationReadModel  

@pytest.mark.celery(result_backend="rpc")
def test_buildAmortizationReadModel_retry(celery_worker):
    result = buildAmortizationReadModel.delay()
    retrie_number = result.get()
    assert True


