from QuantityReconciliation.infrastructure.command.CreateAndApplyStrategy import (
    CreateAndApplyStrategy,
)
from QuantityReconciliation.infrastructure.eventStore.EventStoreMongoDbImp import (
    EventStoreMongoDbImp,
)
from QuantityReconciliation.infrastructure.repository.ReconciliationRepository import (
    ReconciliationRepository,
)
from QuantityReconciliation.infrastructure.service.FileWrapperImp import FileWrapperImp
from QuantityReconciliation.infrastructure.service.IdGeneratorImp import IdGeneratorImp
from QuantityReconciliation.interactor.CreateAndApplyStrategyHandler import (
    CreateAndApplyStrategyHandler,
)
from QuantityReconciliation.interactor.InitializeReconciliationHandler import (
    InitializeReconciliationHandler,
)
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


class Cycle(BaseModel):
    similarityThreshold: int
    reconciliationKeys: list[str]
    categorizationPrecision: str
    algorithm: str


class Strategy(BaseModel):
    reconciliationId: str
    orderedCycles: list[Cycle]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/initializeReconciliation")
async def initializeReconciliation(fileUploaded: UploadFile = File(...)):
    try:
        idGenerator: IdGeneratorImp = IdGeneratorImp()
        file = FileWrapperImp(fileUploaded)
        eventStore: EventStoreMongoDbImp = EventStoreMongoDbImp(
            "mongodb://localhost:27017/", "eventstore", "ReconciliationEventStream"
        )
        reconciliationRepository: ReconciliationRepository = ReconciliationRepository(
            eventStore
        )
        initializeReconciliationHandler: InitializeReconciliationHandler = (
            InitializeReconciliationHandler(reconciliationRepository, idGenerator, file)
        )
        initializeReconciliationHandler.initializeReconciliation()
        return {"msg": "reconciliation initialized succesfully"}

    except Exception as e:
        print(str(e))
        return {"error": str(e)}, 400


@app.post("/createAndApplyStrategy")
async def createAndApplyStrategy(strategy: Strategy):
    try:
        idGenerator = IdGeneratorImp()
        eventStore = EventStoreMongoDbImp(
            "mongodb://localhost:27017/", "eventstore", "ReconciliationEventStream"
        )
        reconciliationRepository = ReconciliationRepository(eventStore)
        createAndApplyStrategyHandler = CreateAndApplyStrategyHandler(
            reconciliationRepository, idGenerator
        )
        serializedStrategy = strategy.model_dump()
        createAndApplyStrategyCmd = CreateAndApplyStrategy(
            strategy.reconciliationId, serializedStrategy["orderedCycles"]
        )
        createAndApplyStrategyHandler.createAndApplyStrategy(createAndApplyStrategyCmd)

        return {"msg": "strategy accepted and is being applied"}
    except Exception as e:
        print(str(e))
        return {"error"}, 400


@app.get("/")
async def hello():
    return {"msg": "reconciliation initialized succesfully"}


if __name__ == "__main__":
    import uvicorn
    from tasks import celery

    uvicorn.run(app, host="0.0.0.0", port=8000)
