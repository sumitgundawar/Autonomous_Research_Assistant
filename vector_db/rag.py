from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

class RAGSystem:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_db = Chroma(persist_directory="vector_db", embedding_function=self.embeddings)

    def ingest_documents(self, documents: list[str]):
        chunks = self.text_splitter.split_documents(documents)
        self.vector_db.add_documents(chunks)

    def retrieve(self, query: str, k=5) -> list[str]:
        return self.vector_db.similarity_search(query, k=k)