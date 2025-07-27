"""Minimal FastAPI server for querying the RAG system."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from retrieval.search import Searcher
from retrieval.vector_store import VectorStore
from llm.generator import generate_with_citations
from memory import memory_db

app = FastAPI()
store = VectorStore()
searcher = Searcher(store)
memory_db.init_db()


class QueryRequest(BaseModel):
    user: str
    question: str


@app.post("/query")
async def query(req: QueryRequest) -> dict:
    """Answer a user question and log the conversation."""

    try:
        results = searcher.search(req.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    records = [
        {"text": r.text, "source": r.metadata.get("source", "")}
        for r in results
    ]

    try:
        resp = generate_with_citations(records, req.question, model_name="dummy")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    memory_db.log(req.user, "user", req.question)
    memory_db.log(req.user, "assistant", resp["answer"])

    return resp


class GenerateRequest(BaseModel):
    user: str
    instruction: str


@app.post("/generate")
async def generate(req: GenerateRequest) -> dict:
    """Generate a new document draft from instructions."""

    memory_db.log(req.user, "user", req.instruction)
    try:
        resp = generate_with_citations([], req.instruction, model_name="dummy")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    memory_db.log(req.user, "assistant", resp["answer"])
    return resp
