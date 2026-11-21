### Week 4 (`Practical/week4/README.md`)

```markdown
# Week 4: Multilingual Tokenizer Comparison

Compares how **BPE (GPT-2)**, **WordPiece (Multilingual BERT)**, and **SentencePiece (XLM-R)** tokenize English and Telugu text using Hugging Face `transformers`.

## Project Structure
- `tokenizer_comparison.py` — Loads tokenizers and prints tokens, token IDs, and token counts.
- `requirements.txt` — Required libraries (`transformers`, etc.).

## Setup & Usage
```cmd
cd Practical/week4
pip install -r requirements.txt
python tokenizer_comparison.py
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.
============================================================

BPE - GPT-2
Tokens     : ['Art', 'ificial', 'Ġintelligence', 'Ġis', 'Ġchanging', 'Ġthe', 'Ġworld', '.']
Token IDs  : [8001, 9542, 4430, 318, 5609, 262, 995, 13]
Token count: 8

WordPiece - Multilingual BERT
Tokens     : ['[CLS]', 'Arti', '##ficial', 'intelligence', 'is', 'changing', 'the', 'world', '.', '[SEP]']
Token IDs  : [101, 90841, 69229, 30151, 10124, 43068, 10105, 11356, 119, 102]
Token count: 10

SentencePiece - XLM-R
Tokens     : ['<s>', '▁Artificial', '▁', 'intelligence', '▁is', '▁changing', '▁the', '▁world', '.', '</s>']
Token IDs  : [0, 231996, 6, 130687, 83, 151134, 70, 8999, 5, 2]
Token count: 10