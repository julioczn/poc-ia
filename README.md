# POC-AI

Poc com o uso de python + langchain + OpenAI + ChromaDB

## Índice

- [POC-AI](#poc-ai)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Instalação](#instalação)
  - [Uso](#uso)

## Visão Geral

Agente de vendas capaz de sugerir e recomendar vendas casadas de produtos de forma eficaz e envolvente.

## Instalação

- Python
- Instale as dependencias a partir do requirements.txt
- Crie uma conta na OpenAI API e utilize a `secret` gerado no `.env` criado a partir do `.env.example`
- Utilize o ChromaDB
- a lista de produtos está na pasta `content` que será carregada ao iniciar a aplicação

## Uso

Rodar a API
```
uvicorn api:app --reload --port 3000
```

Requisição para a API
```
curl --location 'http://localhost:3000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "message": "quero comprar peças de vestuário"
}'
```
