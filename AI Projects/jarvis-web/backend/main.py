from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from jarvis import chat_stream, manage_history

app = FastAPI(title="JARVIS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Message(BaseModel):
    role: str     
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/")
def root():
    return {"status": "JARVIS is online"}


@app.post("/chat")
async def chat(request: ChatRequest):


    messages = [
        {"role": msg.role, "content": msg.content}
        for msg in request.messages
    ]


    messages = manage_history(messages)

    return StreamingResponse(
        chat_stream(messages),
        media_type="text/plain"
    )


