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

Always return ONLY valid string.
Never return markdown or explanations.

Schema:
    "Company Name"


Examples:

Input:
Tata Motors

Output:
"Tata Motors"

Input:
Show me Infosys quarterly revenue

Output:
"Infosys"
no matter of the prompt just give back the company name in full UPPER case letters
"""

def parse_query(user_input: str) -> dict:
    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=user_input,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        response_mime_type="application/string",
        temperature=0
    ),
)
    return response