from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.ingest import ingest_pdf
from app.qa import answer_question
from app.schemas import QueryRequest

app = FastAPI(title="Document QA API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    doc_id = ingest_pdf(file_path, title=file.filename)

    return {"doc_id": doc_id, "message": "Document indexed successfully"}


@app.post("/query")
async def query_docs(request: QueryRequest):
    result = answer_question(request.question)

    return {
        "answer": result["answer"],
        "sources": [
            {
                "title": doc.metadata.get("title"),
                "doc_id": doc.metadata.get("doc_id")
            }
            for doc in result["source_documents"]
        ]
    }
