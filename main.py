import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Titles(BaseModel):
    reference: str
    other: list[str]

app = FastAPI()

@app.post("/")
async def find_title(titles: Titles):
    return {"top_result": titles.reference}


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)