from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import httpx
from langchain.tools import tool
from langchain.agents import create_agent, AgentState
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.callbacks import StdOutCallbackHandler



load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
proxy_url = os.getenv("PROXY_URL")
# os.environ['NO_PROXY'] = 'googleapis.com,google.com,gstatic.com,*.googleusercontent.com'


@tool
def add_task(task):
    """add a new task to the user's task list"""
    print(task)
    print("Task added")



tools = [add_task]


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.3,
    client_args={
        "proxy": proxy_url,
        "timeout": 30.0,
    },
)

#system_prompt: specify the domain in which answer user prompt
system_prompt = "you are a helpgul assistant. You will help the user add tasks."
user_input = "What day is it today?"

#prompt: used in chan not in agent
prompt = ChatPromptTemplate([
    ("system", system_prompt), 
    ("user", user_input),
    MessagesPlaceholder("agent_scratchpad")
    ])


# chain = prompt | llm | StrOutputParser()
# print(chain)
# response = chain.invoke({"input": user_input})
agent = create_agent(llm, tools, system_prompt=system_prompt )
response = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
    config={
        "callbacks": [StdOutCallbackHandler()]
    }
    )

ai_msg = response['messages'][1]
text = ai_msg.content[0]['text']

print(text)
