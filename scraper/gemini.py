import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("Gemini_api_key")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are a stock parser.

Always return ONLY valid JSON.
Never return markdown or explanations.

Schema:
{
    "company": "Company Name"
}

Examples:

Input:
Tata Motors

Output:
{"company":"Tata Motors"}

Input:
Show me Infosys quarterly revenue

Output:
{"company":"Infosys"}
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