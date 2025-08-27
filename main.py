from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv

load_dotenv()

def ai_talk(system_prompt, user_input):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",   
        groq_api_key=os.getenv("GROQ_API_KEY"), # type: ignore
        temperature=2,
    )
    memory = ConversationBufferMemory(return_messages=True, memory_key="history")

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
        ("human", "{input}")
    ])

    conversation = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )
    response = conversation.predict(input=user_input)
    return response 

