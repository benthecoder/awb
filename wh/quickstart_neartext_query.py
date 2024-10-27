import weaviate
from weaviate.classes.init import Auth
import os, json
from dotenv import load_dotenv

load_dotenv()

# Best practice: store your credentials in environment variables
wcd_url = os.environ["WCD_URL"]
wcd_api_key = os.environ["WCD_API_KEY"]
openai_api_key = os.environ["OPENAI_APIKEY"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,  # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(wcd_api_key),  # Replace with your Weaviate Cloud key
    headers={"X-OpenAI-Api-Key": openai_api_key},  # Replace with your OpenAI API key
)

questions = client.collections.get("Question")

response = questions.query.near_text(query="biology", limit=2)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()  # Free up resources