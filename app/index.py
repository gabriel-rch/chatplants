# index.py - loads the context files, splits it into chunks, and stores them in a vector store.
from context.store import load_vector_store
from context.document import load_and_split_documents


def load_and_store_documents():
    """Load documents, split them into chunks, and store in vector store."""
    vector_store = load_vector_store()

    sources = [
        "https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1129379/1/CPAF-AP-2020-cap-4-Principios-de-nutricao.pdf",
    ]

    for source in sources:
        chunks = load_and_split_documents(source)
        print(f"Loaded {len(chunks)} chunks from {source}.")
        vector_store.add_documents(documents=chunks)

    print("all documents loaded and stored in vector store.")


if __name__ == "__main__":
    load_and_store_documents()
