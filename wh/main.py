import weaviate
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv
from weaviate.classes.config import Configure

load_dotenv()
# Best practice: store your credentials in environment variables
wcd_url = os.environ["WCD_URL"]
wcd_api_key = os.environ["WCD_API_KEY"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,  # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(wcd_api_key),  # Replace with your Weaviate Cloud key
)

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(),  # Configure the OpenAI embedding integration
    generative_config=Configure.Generative.openai(),  # Configure the OpenAI generative AI integration
)

print(client.is_ready())  # Should print: `True`

client.close()  # Free up resources
