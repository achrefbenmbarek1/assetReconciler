from celery import Celery

celery = Celery(
    "myapp", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery.task(bind=True, max_retries=3)
def buildAmortizationReadModel(self):
    try:
        retry_number = 0
        raise Exception("this is for test purposes")
    except Exception as e:
         retry_number = self.request.retries
         if retry_number < 3:
            print(f"Retrying task (retry {retry_number}): {e}")
            print(f"Task ID: {self.request.id}")
            raise self.retry(countdown=2 ** retry_number)
         else:
            print(f"Stopped retrying after {retry_number} retries.")
            return retry_number
