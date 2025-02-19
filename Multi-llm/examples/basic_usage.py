from src.llm_manager import LLMManager

def test_all_providers():
    """Test all available providers with a simple prompt."""
    llm = LLMManager()
    prompt = "What is artificial intelligence?"
    
    print("Testing all providers...")
    print("-" * 50)
    
    for provider in llm.list_providers():
        print(f"\nTesting {provider.upper()}:")
        try:
            response = llm.generate(prompt, provider=provider)
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    print("\nDone!")

if __name__ == "__main__":
    test_all_providers()