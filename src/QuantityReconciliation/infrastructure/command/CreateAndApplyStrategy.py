
class CreateAndApplyStrategy:
    def __init__(self, reconciliationId:str, orderedCycles:list[dict]) -> None:
        self.reconciliationId = reconciliationId
        self.orderedCycles = orderedCycles
