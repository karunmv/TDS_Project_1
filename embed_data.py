# embed_data.py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

docs = TextLoader("tds_all_content.txt").load()
chunks = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)

db = Chroma.from_documents(chunks, OpenAIEmbeddings())
