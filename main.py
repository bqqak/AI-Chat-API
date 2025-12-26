from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.params import Body
from fastapi import Request
from db import Base, engine, get_user_request, add_request_data
from gemini_client import get_answer_from_gemini

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("Table is created!")
    yield
app = FastAPI(
    title="AI Chat API",
    lifespan=lifespan)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/requests")
def get_my_requests(request: Request):
    user_ip_address = request.client.host
    print(f"{user_ip_address}")
    user_requests = get_user_request(ip_address=user_ip_address)
    return user_requests

@app.post("/requests")
def send_prompt(
        request: Request,
        prompt: str = Body(embed=True)):
    user_ip_address = request.client.host
    answer = get_answer_from_gemini(prompt)
    add_request_data(
        ip_address=user_ip_address,
        prompt=prompt,
        response=answer,
    )
    return {"answer": answer}