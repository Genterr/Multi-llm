import os

def generate(prompt: str) -> str:
    """
    Anthropic (Claude) text generation.
    """
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        return "[DEMO MODE] Anthropic Claude would generate a response here."
    
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-opus-20240229",
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error with Anthropic: {str(e)}"