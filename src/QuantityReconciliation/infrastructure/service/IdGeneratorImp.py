import uuid

from .IdGenerator import IdGenerator

class IdGeneratorImp(IdGenerator) :
    def generateId(self) -> str:
        id = str(uuid.uuid4())
        return id
        
