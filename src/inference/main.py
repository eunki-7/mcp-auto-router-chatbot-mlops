"""
Inference API using FastAPI.
This API serves the MCP router, chatbot, and vector store integration.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from src.router.router import Router
from src.vectorstore.faiss_store import VectorStore

app = FastAPI(title="MCP Auto-Router Chatbot")
Instrumentator().instrument(app).expose(app)

router = Router()
vector_db = VectorStore()

class ChatRequest(BaseModel):
    text: str

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    route = router.route(req.text)
    if route["component"] == "vector_search":
        return {"response": "Search results from vector DB."}
    else:
        return {"response": "Chatbot response generated."}

@app.get("/health")
def health_check():
    return {"status": "ok"}
