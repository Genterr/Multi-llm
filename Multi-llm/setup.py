from setuptools import setup, find_packages

setup(
    name="multi-llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0',
        'anthropic>=0.7.0',
        'google-generativeai>=0.3.0',
        'groq>=0.3.0',
        'requests>=2.31.0',
        'python-dotenv>=1.0.0',
    ],
)