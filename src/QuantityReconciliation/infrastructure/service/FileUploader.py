from abc import ABC, abstractmethod

from fastapi import UploadFile

class FileUploader(ABC):
    @abstractmethod
    def upload(self, file:UploadFile) -> str:
        pass
