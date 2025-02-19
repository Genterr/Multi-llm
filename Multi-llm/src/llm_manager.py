from typing import Optional, Dict, Any
import os
from .providers import (
    openai_generate,
    anthropic_generate,
    gemini_generate,
    groq_generate,
    deepseek_generate,
    llama_generate
)

class LLMManager:
    def __init__(self):
        """Initialize LLM manager with all available providers."""
        self.providers = {
            'openai': openai_generate,
            'anthropic': anthropic_generate,
            'gemini': gemini_generate,
            'groq': groq_generate,
            'deepseek': deepseek_generate,
            'llama': llama_generate
        }
    
    def list_providers(self) -> list:
        """Return list of all available providers."""
        return list(self.providers.keys())
    
    def generate(self, prompt: str, provider: str = 'openai') -> str:
        """
        Generate text using specified provider.
        
        Args:
            prompt: Input prompt
            provider: Name of the LLM provider to use
            
        Returns:
            Generated text response
        """
        if provider not in self.providers:
            available = self.list_providers()
            raise ValueError(
                f"Provider '{provider}' not available. "
                f"Available providers: {available}"
            )
        
        return self.providers[provider](prompt)