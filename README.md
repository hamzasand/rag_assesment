# Document Question Answering API (RAG)

A **document-based Question Answering API** built using **FastAPI, LangChain, OpenAI, and Qdrant**.
The system allows users to upload PDF documents, index them using vector embeddings, and ask natural language questions that are answered using retrieved document context.

---

## Features

* Upload and index **PDF documents**
* Semantic search using **OpenAI embeddings**
* Context-aware answers using **GPT (RAG)**
* Source documents returned with each answer
* Persistent local **Qdrant vector database**
* Clean, modular, interview-ready architecture

---

## Tech Stack & Rationale

| Tool                 | Why it’s used                                 |
| -------------------- | --------------------------------------------- |
| **Python 3.11**      | Stable and compatible with LangChain & Qdrant |
| **FastAPI**          | High-performance, async-ready REST API        |
| **LangChain (LCEL)** | Modern RAG pipeline orchestration             |
| **OpenAI API**       | High-quality embeddings & LLM responses       |
| **Qdrant (local)**   | Persistent, production-grade vector DB        |
| **PyPDF**            | Reliable PDF text extraction                  |
| **Uvicorn**          | ASGI server for FastAPI                       |

---

## Project Structure

```text
rag_assessment/
│
├── app/
│   ├── main.py          # FastAPI routes
│   ├── config.py        # Environment & constants
│   ├── ingest.py        # PDF ingestion & chunking
│   ├── qa.py            # RAG question answering logic
│   ├── vectorstore.py   # Qdrant + embeddings setup
│   └── schemas.py       # Request/response models
│
├── data/
│   └── sample.pdf       # Sample test document
│
├── qdrant_data/         # Local vector DB storage
├── requirements.txt
├── .env
└── README.md
```

---

## Setup Instructions

### 1️ Prerequisites

* Python **3.10 or 3.11**
* OpenAI API key

---

### 2️ Clone the Repository

```bash
git clone https://github.com/your-username/document-qa-api.git
cd document-qa-api
```

---

### 3️ Create & Activate Virtual Environment

**Windows (PowerShell / Git Bash):**

```bash
py -3.11 -m venv myvenv
source myvenv/Scripts/activate
```

---

### 4️ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5️ Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

### 6️ Run the Server

```bash
uvicorn app.main:app --reload
```

API base URL:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints & Testing (Using Postman)

### 🔹 Upload & Index Document

* **Method:** POST
* **URL:** `http://127.0.0.1:8000/documents`
* **Body Type:** `form-data`

  * Key: `file` (Type: File, choose a PDF file)

**Expected Response:**

```json
{
  "doc_id": "uuid-string",
  "message": "Document indexed successfully"
}
```

---

### 🔹 Ask a Question

* **Method:** POST
* **URL:** `http://127.0.0.1:8000/query`
* **Headers:** `Content-Type: application/json`
* **Body (raw → JSON):**

```json
{
  "question": "What is this document about?"
}
```

**Expected Response:**

```json
{
  "answer": "Generated answer based on document context",
  "sources": [
    {
      "title": "sample.pdf",
      "doc_id": "1234"
    }
  ]
}
```

---

### 🔹 List All Documents

* **Method:** GET
* **URL:** `http://127.0.0.1:8000/documents`

**Expected Response:**

```json
[
  {
    "doc_id": "1234",
    "title": "sample.pdf"
  }
]
```

---

### 🔹 Delete a Document

* **Method:** DELETE
* **URL:** `http://127.0.0.1:8000/documents/{doc_id}`

Replace `{doc_id}` with the actual document ID.

**Expected Response:**

```json
{
  "message": "Document deleted successfully"
}
```

---

## How It Works (RAG Flow)

1. PDF is loaded and split into overlapping chunks
2. Each chunk is embedded using OpenAI embeddings
3. Vectors are stored in a local Qdrant collection
4. User question is embedded and used for similarity search
5. Top relevant chunks are injected into the LLM prompt
6. GPT generates a grounded answer using retrieved context

---

## Sample Data

A sample PDF is provided for easy evaluation:

```
data/sample.pdf
```
---


