from dotenv import load_dotenv

load_dotenv()
import os
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch(tavily_api_key=os.getenv("TAVILYT_API_KEY"))]
llm = ChatOpenAI(model="gpt-4",api_key=os.getenv("OPEN_API_KEY"), temperature=0)
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
chain = agent_executor
# Example usage
def main():
    print("Hello from react-search-agents!")
    result = chain.invoke(
        {
            "input": "What are the top 3 latest news about AI in 2025?",
        }
    )
    print(result)

if __name__ == "__main__":
    main()
