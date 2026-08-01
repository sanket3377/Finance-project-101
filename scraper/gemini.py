import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("Gemini_api_key")

client = api_key # Replace with a new key

SYSTEM_PROMPT = """
You are a stock parser.

Always return ONLY valid JSON.
Never return markdown or explanations.

Schema:
{
    "stock": "Company Name"
}

Examples:

Input:
Tata Motors

Output:
{"stock":"Tata Motors"}

Input:
Show me Infosys quarterly revenue

Output:
{"stock":"Infosys"}
"""

def parse_query(user_input: str) -> dict:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            temperature=0
        ),
    )

    return json.loads(response.text)