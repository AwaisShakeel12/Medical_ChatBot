from langchain.text_splitter import RecursiveCharacterTextSplitter
from .data_loader import extracted_data

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size =5000, chunk_overlap=200)
    text_chunk= text_splitter.split_documents(extracted_data)
    return text_chunk


text_chunk = text_split(extracted_data)
