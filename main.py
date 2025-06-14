from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from generate_answer import generate_answer
from utils import extract_text_from_base64

load_dotenv()
app = FastAPI()
db = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())

class Link(BaseModel):
    url: str
    text: str

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=QueryResponse)
async def answer_query(req: QueryRequest):
    q = req.question
    if req.image:
        ocr = extract_text_from_base64(req.image)
        if ocr:
            q += "\n\n" + ocr
    docs = db.similarity_search(q, k=3)
    passages = [d.page_content for d in docs]
    answer, links = generate_answer(req.question, passages)
    return QueryResponse(answer=answer, links=links)
