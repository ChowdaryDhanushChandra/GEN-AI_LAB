### Week 2 (`Practical/week2/README.md`)
Based on your `llm_client.py`, `main.py`, `requirements.txt` (`python-dotenv`, `pytest`), and `.env` files[cite: 2]:

```markdown
# Week 2: Modular LLM Client & Testing

Refactors LLM API interactions into a reusable client module (`llm_client.py`) with environment variable configuration and unit testing support.

## Project Structure
- `llm_client.py` — Wrapper module for handling LLM API requests.
- `main.py` — Main application script using the LLM client.
- `requirements.txt` — Project dependencies (`python-dotenv`, `pytest`, etc.).
- `.env` — API key configuration (ignored by Git).

## Setup & Usage
1. Activate your virtual environment and install dependencies:
   ```cmd
   pip install -r requirements.txt
   C:\Users\Dhanush\OneDrive\Desktop\GEN_AI_LAB\Practical\week2>python main.py
Choose provider (gemini/ollama): ollama
Enter your question: 1

LLM Response:
It seems like you just sent a number. Can I help you with something or would you like to chat?

C:\Users\Dhanush\OneDrive\Desktop\GEN_AI_LAB\Practical\week2>python main.py
Choose provider (gemini/ollama): ollama
Enter your question: 2

LLM Response:
It looks like you've entered a number, but you haven't given me any context or asked a question. What would you like to talk about or ask?