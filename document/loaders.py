from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

def setup_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("La chiave API OPENAI_API_KEY non è definita nel file .env")
    os.environ["OPENAI_API_KEY"] = api_key

def create_faiss_index(docx_path, index_path="faiss_index"):
    setup_openai()
    loader = UnstructuredWordDocumentLoader(docx_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore

def load_vectorstore(index_path="faiss_index"):
    setup_openai()
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)