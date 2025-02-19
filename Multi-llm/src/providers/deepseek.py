import os
import requests

def generate(prompt: str) -> str:
    """
    Deepseek text generation.
    """
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        return "[DEMO MODE] Deepseek would generate a response here."
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error with Deepseek: {str(e)}"