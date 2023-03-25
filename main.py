from fastapi import FastAPI, File, UploadFile
from summary import summary_using_t5, generate_qna
from api_nlp import get_answer

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World\nWe are ready to rock the world"}
    
    
@app.get("/summary/")
async def summary(text: str = "Hello World"):
    return summary_using_t5(text)


@app.get("/qna/")
async def qna(text: str = "Hello World"):
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

    return {"message": f"Successfully uploaded {file.filename}"}

