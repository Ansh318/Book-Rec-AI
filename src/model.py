from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import OpenAI
from prompts import PromptManager
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.callbacks import StdOutCallbackHandler
handler = StdOutCallbackHandler()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

prompt_manager = PromptManager()
prompt = prompt_manager.create_prompt("System Prompt")
llm = OpenAI()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chat_llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
    callbacks=[handler],
)
print(chat_llm_chain.predict(human_input="What is your job description?"))
# response = chain.invoke({"query":"Hi! What is your job description?"})
# print(response)