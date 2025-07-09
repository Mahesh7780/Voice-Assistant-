from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from agent.tools import search

llm = OllamaLLM(model="llama3")

tools = [search]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)
