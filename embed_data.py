import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

def embed_data():
    loader = TextLoader("data/course_notes.txt")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="./chroma_db")
    db.persist()
    print("Embedded course data")

if __name__ == "__main__":
    embed_data()
