from prompts import PromptManager
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from modelConfig import ModelConfigManager

class OpenAIModel:

    def __init__(self, name, temperature, max_retries):
        self.name = name
        self.temperature = temperature
        self.max_retries = max_retries

    def load_model(self):
        llm = ModelConfigManager(self.name, self.temperature, self.max_retries).model()
        return llm

    def run_chain(self, prompt_name, query):
        llm = self.load_model()
        prompt_manager = PromptManager()
        prompt = prompt_manager.create_prompt(prompt_name)
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        chat_llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,
        )
        response = chat_llm_chain.predict(human_input=query)
        return response


model = OpenAIModel("gpt-4", "0", "1")
response = model.run_chain("System Prompt", "What is your job description?")
print(response)
