from fastapi import FastAPI
from summary import summary_using_t5, generate_qna
from api_nlp import get_answer
from tr import translate as trr

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


@app.get("/translate/")
async def translate(text: str = "Hello World"):
    return trr(text)

#if __name__ == "__main__":
#    uvicorn.run(app, host="10.196.28.63", port=8000)

