from turtle import hideturtle
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
proxy_url = os.getenv("PROXY_URL")

system_prompt = """
You're Einstein. 
Answer questions through Einstein's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life
even when the user don't ask for it. For example, if the user asks about the theory og
relativity, you will share your personal experiences with it and not only explain the theory.
Answer in 2-6 sentences.
you should have a sense of humor
"""

user_input = input("You: ")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5,
    client_args={
        "proxy": proxy_url,
        "timeout": 30.0,
    },
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        (MessagesPlaceholder(variable_name="history")),
        ("user", "{input}"),
    ]
)

chain = prompt | llm | StrOutputParser()

print("Hi! I'm albert, how can I help you today?")
history = []


"""the commented rows are related to memorizing history without using langchain"""
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    #history.append({"role": "user", "content": user_input})
    response = chain.invoke({"input": user_input, "history": history})
    #response = llm.invoke(
        #[
        #    {"role": "system", "content": system_prompt}
            # {"role": "user", "content": user_input},
      #  ]
      #  + history
    #)
    #history.append({"role": "system", "content": system_prompt})
    history.append(HumanMessage(content=user_input))

    history.append(response)

    print(f"Albert: {response}")
