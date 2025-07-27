# docu-rag

Simple RAG system skeleton for internal document QA. Documents stay on-premise and models run locally.

## Modules

- `ingestion/` - download and preprocess documents from SharePoint.
- `retrieval/` - hashed vector store and retrieval utilities with reranking.
- `llm/` - prompt handling and local model loading.
- `memory/` - conversation history logging and search.
- `api_server.py` - FastAPI application exposing `/query` and `/generate`.
- `ui/` - minimal chat frontend with conversation view.
- Embeddings use a lightweight word hashing scheme so no external model downloads are required.

## Dummy SharePoint client

The repository includes `DummySharePointClient` which provides static document
URLs like `https://sharepoint.example.com/docs/doc1.txt`. The dummy client
returns placeholder bytes for these URLs so the ingestion pipeline can be tested
without real SharePoint credentials.
