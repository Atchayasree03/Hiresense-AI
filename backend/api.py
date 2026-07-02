from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.rank_candidates import rank_candidates
from src.candidate_mapper import get_candidate
from src.candidate_mapper import get_candidate_by_id

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
        top_k=100
    )

    return {
        "candidates": candidates
    }

@app.get("/candidate/{candidate_id}")
def candidate_details(candidate_id: str):

    candidate = get_candidate_by_id(candidate_id)

    if candidate is None:
        return {
            "error": "Candidate not found"
        }

    return candidate