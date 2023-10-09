from .DomainEvent import DomainEvent


class FileLoaded(DomainEvent):
    def __init__(self, eventId, aggregateId, filePath):
        payload = {
            "filePath": filePath
        }
        super().__init__(eventId, aggregateId, payload)
