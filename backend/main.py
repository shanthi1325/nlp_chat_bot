from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import get_bot_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user: str
    message: str

user_sessions = {}

@app.post("/chat")
def chat(req: ChatRequest):
    user_sessions.setdefault(req.user, [])
    reply = get_bot_response(req.message)
    user_sessions[req.user].append((req.message, reply))
    return {"reply": reply}

@app.get("/history/{user}")
def get_history(user: str):
    return {"history": user_sessions.get(user, [])}