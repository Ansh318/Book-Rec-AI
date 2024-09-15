import weaviate

client = weaviate.connect_to_local()
print(client)
client.close()