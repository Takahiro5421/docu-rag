"""Minimal FastAPI server for querying the RAG system."""

from fastapi import FastAPI
from pydantic import BaseModel

from retrieval.search import Searcher
from retrieval.vector_store import VectorStore
from llm.generator import generate_answer

app = FastAPI()
store = VectorStore()
searcher = Searcher(store)


class QueryRequest(BaseModel):
    user: str
    question: str


@app.post("/query")
async def query(req: QueryRequest) -> dict:
    docs = [r.text for r in searcher.search(req.question)]
    answer = generate_answer(docs, req.question, model_name="dummy")
    return {"answer": answer}
