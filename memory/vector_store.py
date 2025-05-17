from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import Config

class VectorStore:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL,
            model_kwargs={'device': 'cpu'}
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        self.db = None

    def create_from_documents(self, documents):
        docs = self.text_splitter.split_text(documents)
        self.db = FAISS.from_texts(docs, self.embedding)
        return self.db

    def search(self, query, k=3):
        if self.db is None:
            raise ValueError("Vector store not initialized")
        return self.db.similarity_search(query, k=k)