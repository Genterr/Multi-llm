import os
from typing import Optional

def generate(prompt: str) -> str:
    """
    OpenAI text generation.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return "[DEMO MODE] OpenAI would generate a response here."
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error with OpenAI: {str(e)}"