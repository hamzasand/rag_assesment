import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

QDRANT_PATH = "./qdrant_data"

COLLECTION_NAME = "documents"
