import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from EmbeddingModel import allMiniLM

class Titles(BaseModel):
    reference: str
    other: list[str]

model = allMiniLM()

app = FastAPI()

@app.post("/")
async def find_title(titles: Titles):
    result = model.most_similar(titles.reference, titles.other)
    return {"top_result": result[0]}


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)