import weaviate
from weaviate.classes.config import Configure, Property, DataType
import os

class WeaviateVectorStore:

    def __init__(self):
        self.client = None

    def connect_weaviate(self):
        self.client = weaviate.connect_to_local(headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")})
        return self.client
    
    def create_schema(self):
        self.client.collections.create(
            "BookInventory",
            properties = [
                Property(name = "BookDescription", data_type= DataType.TEXT)
            ]
        )

    def read_txt_file(self,file_path):
        """
        Reads a text file and returns its content as a string.

        Parameters:
        file_path (str): The path to the text file.

        Returns:
        str: The content of the text file as a string.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = [line.strip() for line in file.readlines()]
                return content
        except FileNotFoundError:
            return f"Error: The file at {file_path} was not found."
        except Exception as e:
            return f"Error: {str(e)}"


    def write_to_db(self, data):
        pass
    def search_vector():
        pass

    def close_connection(self):
        if self.client != None:
            self.client.close()
            self.client = None

    
    

vector_store = WeaviateVectorStore()
client = vector_store.connect_weaviate()
# print(client)
# # inventory = client.collections.get("BookInventory")
# # print(inventory)
# data = vector_store.read_txt_file("/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/books.txt")
# # print(data)
# # vector_store.write_to_db(data)
# vector_store.close_connection()



