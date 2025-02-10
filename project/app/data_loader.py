

from langchain.document_loaders import PyPDFDirectoryLoader


def data_load(data):
    pdf_loader = PyPDFDirectoryLoader(data)

    pdf_doc = pdf_loader.load_and_split()
    
  
    
    return pdf_doc

extracted_data =data_load(r'E:\django\djang x gen\soplex_clinic_backend\project\docs')


    