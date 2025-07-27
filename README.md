# docu-rag

Simple RAG system skeleton for internal document QA.

## Modules

- `ingestion/` - download and preprocess documents.
- `retrieval/` - simple vector store and search utilities.
- `llm/` - prompt handling and model loading.
- `memory/` - conversation history logging and search.
- `api_server.py` - FastAPI application.
- `ui/` - minimal chat frontend.
