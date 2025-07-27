# docu-rag

Simple RAG system skeleton for internal document QA. Documents stay on-premise and models run locally.

## Modules

- `ingestion/` - download and preprocess documents from SharePoint.
- `retrieval/` - simple vector store and search utilities with reranking.
- `llm/` - prompt handling and local model loading.
- `memory/` - conversation history logging and search.
- `api_server.py` - FastAPI application exposing `/query` and `/generate`.
- `ui/` - minimal chat frontend with conversation view.
