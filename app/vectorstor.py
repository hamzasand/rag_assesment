from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant

from app.config import QDRANT_PATH, COLLECTION_NAME, OPENAI_API_KEY


def get_vectorstore():
    client = QdrantClient(path=QDRANT_PATH)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=OPENAI_API_KEY
    )

    # 👇 IMPORTANT: ensure collection exists
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=1536,  # ada-002 embedding size
                distance=Distance.COSINE
            )
        )

    vectorstore = Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=embeddings,
    )

    return vectorstore
