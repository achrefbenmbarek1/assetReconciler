class NumberOfCycles:
    def __init__(self,numberOfCycles:int) -> None:
        if numberOfCycles <= 0:
            raise Exception("number of cycles has to be superior strictly than 0")
        self.numberOfCycles = numberOfCycles
