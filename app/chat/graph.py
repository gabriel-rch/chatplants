from context.store import load_vector_store
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import START, StateGraph

vector_store = load_vector_store()
llm = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")
prompt = ChatPromptTemplate.from_messages(
    [
        HumanMessagePromptTemplate.from_template(
            "Você é um assistente especializado em tarefas de perguntas e respostas. "
            "Utilize os seguintes trechos de contexto recuperados para responder à pergunta. "
            "Se não souber a resposta, diga simplesmente que não sabe. "
            "Use no máximo três frases e mantenha a resposta concisa.\n\n"
            "Pergunta: {question}\n"
            "Contexto: {context}\n"
            "Resposta:"
        )
    ]
)


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


def create_graph():
    """Create a state graph for the question-answering process."""
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()

    return graph
