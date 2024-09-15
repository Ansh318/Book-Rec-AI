from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import OpenAI


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')



llm = OpenAI()

print(llm.invoke("Hello how are you?"))