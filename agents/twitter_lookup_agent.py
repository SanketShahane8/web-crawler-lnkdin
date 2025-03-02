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
    # return "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
    # llm = ChatOpenAI(
    #     temperature=0,
    #     model_name="gpt-3.5-turbo",
    # )

    llm = ChatOllama(model="llama3.2")
    template="""Given the name {name_of_person} , I want you to find to their Twitter profile page and extract their username.
    In your final answer only the the person's username
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Twitter Page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True,handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if  __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marko")
    print(linkedin_url)