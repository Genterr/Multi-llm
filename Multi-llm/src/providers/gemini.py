import os

def generate(prompt: str) -> str:
    """
    Google Gemini text generation.
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return "[DEMO MODE] Google Gemini would generate a response here."
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error with Gemini: {str(e)}"