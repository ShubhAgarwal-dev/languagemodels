from fastapi import FastAPI, File, UploadFile

from summary import summary_using_t5, generate_qna
from api_nlp import get_answer
from tr import translate as trr
from pdfEx import pdfExtract

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! We are ready to rock the world"}
    
    
@app.get("/summary/")
async def summary(text: str = "Paste the text here"):
    return summary_using_t5(text)


@app.get("/qna/")
async def qna(text: str = "Paste the text here"):
    return generate_qna(text)
    

@app.get("/ans/")
async def ans(question:str, context:str):
    return get_answer(question, context)
    

@app.post("/upload/")
async def file_upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(f"./data/{file.filename}", 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return pdfExtract(f"./data/{file.filename}")


@app.get("/translate/")
async def translate(text: str = "Paste the text here"):
    return trr(text)

