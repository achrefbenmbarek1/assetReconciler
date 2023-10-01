class InitializeReconciliation:
    def __init__(self, reconciliationId:str, physicalInventory:list[dict], amortizationTable:list[dict], eventsIds:list[str]) -> None:
        self.reconciliationId = reconciliationId
        self.physcialInventoryLineItems = physicalInventory
        self.amortizationTable = amortizationTable
        self.eventsIds = eventsIds
        # self.reconciliationInitializedId = reconciliationInitializedId
        # self.missingPhysicalInvententoryLineItemsExtractedId = missingPhysicalInvententoryLineItemsExtractedId
        # self.missingAmortizationTableLineItemsExtractedId = missingAmortizationTableLineItemsExtractedId
