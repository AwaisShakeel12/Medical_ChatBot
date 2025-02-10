
import os
from langchain.vectorstores import Chroma
import google.generativeai as genai

import warnings
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
from .splitting import text_chunk
import os

load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)


from langchain_google_genai import GoogleGenerativeAIEmbeddings


gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


pr_directory ="chroma_data_new"


vectorStore = Chroma.from_documents(documents=text_chunk, embedding=gemini_embeddings, persist_directory=pr_directory)

vectorStore.persist()
vectorStore = Chroma(embedding_function=gemini_embeddings, persist_directory=pr_directory)


retriever = vectorStore.as_retriever(search_kwargs={"k": 3})