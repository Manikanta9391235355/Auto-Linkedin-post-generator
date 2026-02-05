import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)


def generate_text(topic: str) -> str:
    """
    Generates a professional LinkedIn post.
    Never asks questions. Never prints.
    """

    prompt = f"""
Write a professional LinkedIn post (100–130 words) about "{topic}".

Rules:
- DO NOT ask questions
- DO NOT use bullet points
- Write as if a human professional is posting
- Tone: confident, insightful, engaging
- End with 3–4 relevant hashtags
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()
