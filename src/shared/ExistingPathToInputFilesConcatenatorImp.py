import os
from shared.PathNotExistException import PathNotExistException

class ExistingPathToInputFilesConcatenatorImp:
    def concatenateFileToPath(self, fileName:str) -> str:
        path = os.path.join('..','inputFiles', fileName)
        isPathExist = os.path.exists(path)
        if(not isPathExist):
            raise PathNotExistException(f"there were either a typo or the path:{path} doen't exist")
        return path
