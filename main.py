# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import base64

app = FastAPI()

class QARequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer_question(payload: QARequest):
    # Process image if provided
    if payload.image:
        img_bytes = base64.b64decode(payload.image)
        # OCR or vision processing if needed

    # Query your vector DB
    relevant_docs = db.similarity_search(payload.question, k=3)

    # Construct prompt & get answer from OpenAI
    context = "\n".join([d.page_content for d in relevant_docs])
    prompt = f"Answer the question based on context:\n\n{context}\n\nQuestion: {payload.question}"
    answer = get_llm_response(prompt)

    # Include links if available
    links = extract_links(relevant_docs)

    return {
        "answer": answer,
        "links": links
    }
