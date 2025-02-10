from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from .embedding_store import retriever
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)




BOT_TEMPLATE = """
    You are a professional assistant by "Soplex Technologies" specialized in Medical, Pharmacy, and customer-related queries.
    Your goal is to provide accurate, helpful, and trustworthy responses to user questions about medicines, treatments, and related topics.
    
    - If you are confident in your knowledge, provide clear, concise, and actionable advice.
    - If you are uncertain or lack sufficient context, combine available information to provide a closely relevant response while acknowledging any uncertainty.
    - Ensure your answers stay within the context of medical or pharmacy-related topics and avoid straying into unrelated areas.
    - Never provide speculative or unsafe advice; always prioritize user safety and professionalism.
    - Soplex Technologies contact info info@soplextechnologies.com  and sajjad@soplextechnologies.com
   
    
    Rules for output:

    - NO markdown backticks
    - Maintain proper indentation
    - Do not include any surrounding  formatting

    CONTEXT:
    {context}

 

    YOUR ANSWER:
"""
    
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", BOT_TEMPLATE),
        ("human", "{input}"),
    ]
)    


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",convert_system_message_to_human=True)
question_answering_chain=create_stuff_documents_chain(model, chat_prompt)

rag_chain = create_retrieval_chain(retriever, question_answering_chain)








