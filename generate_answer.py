from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def generate_answer(question: str, passages: list[str]) -> tuple[str, list[dict]]:
    context = "\n\n".join(passages)
    prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer with bullet points. Also include source URLs (if any) in links list."
    response = llm.predict(prompt)
    links = []
    for line in response.splitlines():
        if line.startswith("http"):
            url, *text = line.split(" ", 1)
            links.append({"url": url, "text": text[0] if text else url})
    return response.strip(), links
