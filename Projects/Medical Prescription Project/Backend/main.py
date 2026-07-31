from fastapi import FastAPI,Form,UploadFile,File
from pydantic import BaseModel
import uuid
import os

app = FastAPI()

import extractor

class Request(BaseModel):
    file_format:str=Form(...)
    file:UploadFile= File(...)

@app.post("/extract_from_doc")

def extract_from_doc(request:Request):

    contents = Request.file.file.read()
    file_path = "/Users/pranavaditya/Desktop/Data-Engineering-Journey/Projects/Medical Prescription Project/Backend/Uploads/"+str(uuid.uuid4())+".pdf"

    with open(file_path,'wb') as f:
        f.write(contents)

    try:
        data = extractor.extract(file_path,request.file_format)
    except Exception as e:
        data = {'error':str(e)}

    if os.path.exists(file_path):
        os.remove(file_path)

    return data