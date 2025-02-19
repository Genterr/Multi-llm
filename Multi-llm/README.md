# Multi-LLM Integration

A simple Python library for integrating multiple LLM providers (OpenAI, Anthropic, Gemini, Groq, Deepseek, Llama).

## Features

- Unified interface for various LLM providers
- Demo mode without API keys for testing
- Easy extensibility for new providers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-llm.git
cd multi-llm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set API keys as environment variables:
```bash
# Linux/Mac
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"
export GEMINI_API_KEY="your-key"
export GROQ_API_KEY="your-key"
export DEEPSEEK_API_KEY="your-key"
export LLAMA_MODEL_PATH="/path/to/model"

# Windows
set OPENAI_API_KEY=your-key
set ANTHROPIC_API_KEY=your-key
# etc.
```

## Quick Start

```python
from src.llm_manager import LLMManager

# Initialize manager
llm = LLMManager()

# Generate text
response = llm.generate(
    prompt="What is AI?",
    provider="openai"  # or 'anthropic', 'gemini', etc.
)
print(response)
```

## Demo Mode

When no API keys are set, the library runs in demo mode and returns placeholder responses.

## Supported Providers

- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Google Gemini
- Groq
- Deepseek
- Llama (local model)

## Examples

Check out the files in the `examples/` directory:

```bash
python examples/basic_usage.py
```

## Contributing

Improvements and pull requests are welcome!