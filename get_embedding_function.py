from langchain_community.embeddings import ollama


"""
It is very important to get the Ollama embedding function in this way.

The following import contains embedding function that works with Chroma db:
from langchain_community.embeddings import ollama

This does not:
from langchain_community.embeddings import OllamaEmbeddings
"""
def get_embedding_function():
    ollama_emb = ollama.OllamaEmbeddings(model='nomic-embed-text')

    return ollama_emb