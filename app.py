#Meu primeiro agente de IA com a Framework AGNO
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Carrega a chave que está no seu arquivo .env
load_dotenv()

# Criação do Agente autônomo OPENAI
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    description="Você é um assistente de pesquisa prestativo.",
    instructions=[
        "Sempre use a ferramenta de busca para confirmar dados atuais.",
        "Responda em Português do Brasil de forma clara.",
    ],
    markdown=True
)

# Comando para o agente falar
print("--- AGENTE INICIADO ---")
pergunta = input("Digite a sua pergunta: ")
agente.print_response(pergunta, stream=True)