import os
import shutil
from QuantityReconciliation.infrastructure.service.FileUploader import FileUploader

from fastapi import UploadFile

class FileUploaderImp(FileUploader):
    def upload(self, file:UploadFile):
        uploadDirectory = "uploads"
        os.makedirs(uploadDirectory, exist_ok=True)
        if file.filename is None:
            raise Exception("the file must have a name")
        filePath = os.path.join(uploadDirectory, file.filename)
        if os.path.exists(filePath):
            raise Exception(f"A file with the name '{file.filename}' already exists")
        with open(filePath, "wb") as destFile:
            shutil.copyfileobj(file.file, destFile)

