# 🌱 Chatplants

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-🔥-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-supported-lightgrey)
![RAG](https://img.shields.io/badge/RAG-enabled-brightgreen)

Este projeto é um chatbot inteligente treinado com RAG (Retrieval-Augmented Generation) para ajudar pessoas que querem começar a cuidar de plantas, mas ainda não entendem os conceitos básicos. Seja você um jardineiro de primeira viagem ou alguém tentando salvar aquela plantinha na varanda, esse agente está aqui pra te ajudar!

## 🧠 Como funciona

O agente usa a técnica de RAG para fornecer respostas fundamentadas em uma base de dados personalizada com:

- Artigos sobre jardinagem e cuidados com plantas
- Livros técnicos e educativos
- Guias para iniciantes
- Materiais sobre tipos de plantas, rega, solo, luz, poda e muito mais

As respostas são geradas com linguagem simples, didática e acolhedora — perfeitas para quem está começando do zero.

## 💬 Exemplos de perguntas que ele responde

- "Como sei se estou regando minha planta demais?"
- "Qual o melhor tipo de vaso para começar?"
- "Como cuidar de uma suculenta em apartamento?"
- "Minha planta tá com as folhas amarelas, o que pode ser?"

## ⚙️ Tecnologias utilizadas

- 🧩 **LangChain** - Framework para desenvolvimento de aplicações com LLMs
- 🧠 **Gemini 2.0** - Modelo de linguagem para geração de respostas
- 🔎 **ChromaDB** - Banco de dados vetorial para armazenar embeddings

## 🚀 Como rodar o projeto

```bash
# clone o repositório
git clone https://github.com/gabriel-rch/chatplants.git
cd chatplants

# instale as dependências
pip install -r requirements.txt

# inicie o agente
python src/main.py
```
