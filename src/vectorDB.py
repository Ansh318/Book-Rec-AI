import weaviate
import os

class WeaviateVectorStore:

    def __init__(self):
        pass

    def connect_weaviate(self):
        client = weaviate.connect_to_local(headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")})
        client.close()
        return client


    def read_txt_file(file_path):
        """
        Reads a text file and returns its content as a string.

        Parameters:
        file_path (str): The path to the text file.

        Returns:
        str: The content of the text file as a string.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"Error: The file at {file_path} was not found."
        except Exception as e:
            return f"Error: {str(e)}"


    def write_to_db(self, data):
        pass

vector_store = WeaviateVectorStore()
vector_store.connect_weaviate()



