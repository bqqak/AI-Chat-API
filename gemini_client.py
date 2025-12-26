from config import config_obj
from google import genai

client = genai.Client(api_key=config_obj.gemini_api_key)

def get_answer_from_gemini(prompt: str):
    response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
    )
    return response.text

