import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend URL(s)
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# USE_OPENAI = os.getenv("USE_OPENAI", "true").lower() == "true"

USE_OPENAI = False

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class QueryResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=QueryResponse)
async def answer_query(req: QueryRequest):
    # Use mock or real LLM based on environment
    if USE_OPENAI:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.question}],
            temperature=0
        )
        answer_text = completion.choices[0].message.content.strip()
    else:
        # 🔁 Mocked answer for development/testing
        answer_text = f"Mocked answer for: '{req.question}'"

    # Example dummy links — replace with actual retrieval logic or keep for mock mode
    links = [
        Link(
            url="https://discourse.onlinedegree.iitm.ac.in/t/sample-thread/12345",
            text="Example link relevant to your question."
        )
    ]

    return QueryResponse(answer=answer_text, links=links)

@app.get("/")
async def root():
    return {"message": "TDS Virtual TA API. POST your question to /api/"}
