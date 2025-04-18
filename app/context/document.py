from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split_documents(file_path: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    """Load and split documents into chunks."""
    # Load the document
    loader = PyPDFLoader(file_path)
    document = loader.load()

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = text_splitter.split_documents(document)

    return chunks
