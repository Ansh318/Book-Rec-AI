from langchain_openai import ChatOpenAI
class ModelConfig:

    def __init__(self, model_name, temperature, max_retries):
        self.model_name = model_name
        self.temperature = temperature
        self.max_retries = max_retries
    
    def model(self):
        llm = ChatOpenAI(
            model = self.model_name,
            temperature = self.temperature,
            max_retries = self.max_retries,
        )
        return llm
    
params = ModelConfig("gpt-4", "0", "1")
params.model()


