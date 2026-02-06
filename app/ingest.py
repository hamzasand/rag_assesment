import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from app.vectorstor import get_vectorstore

def ingest_pdf(file_path: str, title: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    doc_id = str(uuid.uuid4())
    for chunk in chunks:
        chunk.metadata["doc_id"] = doc_id
        chunk.metadata["title"] = title

    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)

    return doc_id
