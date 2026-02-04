from typing import Optional
from dotenv import load_dotenv
import os
import langchain
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import httpx
from langchain.tools import tool
from langchain.agents import create_agent, AgentState
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.callbacks import StdOutCallbackHandler
from todoist_api_python.api import TodoistAPI
from langchain.agents.structured_output import ToolStrategy
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver






load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
proxy_url = os.getenv("PROXY_URL")
# os.environ['NO_PROXY'] = 'googleapis.com,google.com,gstatic.com,*.googleusercontent.com'


# Evitiamo proxy per Todoist
os.environ["NO_PROXY"] = "api.todoist.com"



todoist = TodoistAPI(f"{todoist_api_key}")


@tool
def add_task(task:str, desc: Optional[str] = None):
    """add a new task to the user's task list"""
    #print(task)
    #print("Task added")
    todoist.add_task(content=task, description=desc)



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
system_prompt = "you are a helpful assistant. You will help the user add tasks."

#prompt: used in chain not in agent
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), 
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    ])

checkpointer= MemorySaver()
# chain = prompt | llm | StrOutputParser()
# print(chain)
# response = chain.invoke({"input": user_input})
agent = create_agent(llm, tools, system_prompt=system_prompt, checkpointer=checkpointer)


while True:
    user_input = input("You: ")
    
    response = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
    config={
        "configurable": {
            "thread_id": "session-1",   # identifica la conversazione
            # "user_id": "user-123",    # opzionale, se lo usi nel tuo setup
        }
    },
    #config={"callbacks": [StdOutCallbackHandler()]}
    )
    last_message = response["messages"][-1]

    if isinstance(last_message.content, list):
        ai_answer = "".join(
            block["text"]
            for block in last_message.content
            if block.get("type") == "text"
        )
    else:
        ai_answer = last_message.content

    print(ai_answer)


