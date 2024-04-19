from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("llmpdftest.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, separators=[
    "\n\n",
    ".",
    "\n",
    " ",
    "",
])
all_splits = text_splitter.split_documents(data)
print(all_splits)
