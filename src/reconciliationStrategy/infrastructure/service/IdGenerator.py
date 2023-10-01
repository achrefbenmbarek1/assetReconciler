import uuid

class IdGenerator :
    @classmethod
    def generateId(cls) -> str:
        id = str(uuid.uuid4())
        return id
        
