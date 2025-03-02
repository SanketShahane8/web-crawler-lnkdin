import os
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3.2")

    # The issue is here - you're using a custom prompt but not passing it correctly to the agent
    # We'll modify how the input is formatted and passed to the agent

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the LinkedIn Page URL"
        )
    ]

    # Pull the ReAct prompt from the hub
    react_prompt = hub.pull("hwchase17/react")

    # Create the agent
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # Add handle_parsing_errors=True to handle the format error
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        handle_parsing_errors=True  # Add this parameter to handle parsing errors
    )

    # Simplify the input to the agent
    result = agent_executor.invoke(
        {
            "input": f"Given the full name {name}, I want you to get me a link to their LinkedIn profile page. Return only the URL."
        }
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marko Udemy")
    print(linkedin_url)