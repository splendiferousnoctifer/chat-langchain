"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import ReadTheDocsLoader, DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


def ingest_docs():
    """Get documents from web pages."""
    
    print("Loading documents...")
    loader = DirectoryLoader('www.stoeckl.ai/', glob="**/*.html")

    

    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    print("Splitting documents...")
    documents = text_splitter.split_documents(raw_documents)

    print("Embedding documents...")
    embeddings = OpenAIEmbeddings()

    print("Ingesting documents...")
    vectorstore = FAISS.from_documents(documents, embeddings)

    print("Saving vectorstore...")
    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
