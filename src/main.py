import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from .EmbeddingModel import allMiniLM
from contextlib import asynccontextmanager

class Titles(BaseModel):
    reference: str
    other: list[str]

model: allMiniLM

@asynccontextmanager
async def lifespan(app: FastAPI):
    # load embedding model on startup
    global model
    model = allMiniLM()

    yield

    model = None

app = FastAPI(lifespan=lifespan)


@app.post("/")
async def find_title(titles: Titles):
    if len(titles.other) == 0:
        return {"top_result": "No titles to compare provided."}

    result = model.most_similar(titles.reference, titles.other)

    return {"top_result": result[0]}

if __name__=="__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=False)