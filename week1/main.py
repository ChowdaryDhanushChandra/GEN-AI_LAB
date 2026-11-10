
import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

try:
    print("\nConnecting to Gemini 3.5 Flash Lite...")

    # Generate AI response
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="What is Artificial Intelligence? Explain in simple words."
    )

    # Display response
    print("\n========== LLM RESPONSE ==========\n")
    print(response.text)
    print("\n==================================")

except APIError as e:
    print("\nGemini API Error:")
    print(e)

except Exception as e:
    print("\nUnexpected Error:")
    print(e)
