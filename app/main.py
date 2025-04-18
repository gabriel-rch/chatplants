from chat.graph import create_graph


graph = create_graph()
result = graph.invoke({"question": "Quais os nutrientes importantes para plantas?"})

print(f'Context: {result["context"]}\n\n')
print(f'Answer: {result["answer"]}')
