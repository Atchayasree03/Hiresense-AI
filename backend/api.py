from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.rank_candidates import rank_candidates

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobRequest(BaseModel):
    jd: str


@app.get("/")
def home():
    return {
        "message": "API Running"
    }


@app.post("/rank")
def rank(request: JobRequest):

    candidates = rank_candidates(
        request.jd,
        top_k=10
    )

    return {
        "candidates": candidates
    }