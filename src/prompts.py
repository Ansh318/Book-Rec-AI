from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os
import json

class PromptManager:
    def __init__(self):
        """
        Initalize PromptManager with Prompt Templates for Virtual Librarian.
        """
        self.system_prompt_path = os.getenv("SYSTEM_PROMPT_PATH")
        self.prompts = None

    def read_prompt(self):
        """
        Read prompt content
        """
        try:
            with open(self.system_prompt_path, 'r') as file:
                prompts_json = json.load(file)
                self.prompts = prompts_json['prompts']
        except FileNotFoundError:
            return f"Error: File '{self.system_prompt_path} not found' not found."
        except json.JSONDecodeError:
            return f"Error: Failed to decode JSON."
        except Exception as e:
            return f"Encountered unexpected error due to {e}"

    def create_prompt(self, prompt_id,input_variables):
        """
        Initalize and Return Prompt Instance 
        """
        try:
            self.read_prompt()
            content = self.prompts[prompt_id]['content']
            prompt = PromptTemplate(template=content, input_variables=input_variables)
            return prompt
        except ValueError as ve:
            return f"Value error: {ve}"
        except KeyError as ke:
            return f"KeyError: Key not found: {ke}"
        except Exception as e:
            return f"An unexpected error occured due to {e}"
    
prompt_manager = PromptManager()
print(prompt_manager.create_prompt("System Prompt", ['query']))