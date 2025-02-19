import os

def generate(prompt: str) -> str:
    """
    Groq text generation.
    """
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        return "[DEMO MODE] Groq would generate a response here."
    
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error with Groq: {str(e)}"