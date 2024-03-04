from fastapi import FastAPI
from pydantic import BaseModel
from agent import load_docs, split_docs, process_qa

app = FastAPI()

directory = './content'

documents = load_docs(directory)
docs = split_docs(documents)

class Payload(BaseModel):
    message: str

@app.post("/chat")
async def chat(payload: Payload):
    response = process_qa(payload.message, docs)
    return {"message": response}