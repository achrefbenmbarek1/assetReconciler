from datetime import datetime


class DomainEvent:
    def __init__(self,eventId, aggregateId, payload):
        self.eventId = eventId
        self.reconciliationId = aggregateId
        self.payload = payload
        self.timestamp = datetime.now()
