from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os

class PromptManager:
    def __init__(self):
        """
        Initalize PromptManager with Prompt Templates for Virtual Librarian.
        """
        self.system_prompt_path = os.getenv("SYSTEM_PROMPT_PATH")

    def read_prompt(self, path):
        """
        Read prompt content
        """
        pass

    def create_prompt(self, input_variables):
        """
        Initalize and Return Prompt Instance 
        """
        content = self.read_prompt()
        prompt = PromptTemplate.from_template(content)
        return prompt