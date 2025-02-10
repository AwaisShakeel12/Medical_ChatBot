from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .retriver_fun import  rag_chain

@api_view(['POST'])
def ask_question(request):
    user_input = request.data.get('query', '')
    
    if not user_input:
        return Response({"error": "No query provided."}, status=400)
    
    
    response = rag_chain.invoke(
        {"input": user_input},
      
    )
    
    return Response({"answer": response["answer"]})
