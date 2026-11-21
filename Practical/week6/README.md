### Week 6 (`Practical/week6/README.md`)

```markdown
# Week 6: LLM Baseline Evaluation

Evaluates LLM outputs against a curated golden dataset (`golden_set.json`) and exports baseline performance metrics to `baseline_results.csv`.

## Project Structure
- `main.py` — Runs evaluation prompts against the model and logs results.
- `golden_set.json` — Reference test cases and expected outputs.
- `baseline_results.csv` — Recorded evaluation results and baseline metrics.
- `requirements.txt` — Required Python packages.

## Setup & Usage
```cmd
cd Practical/week6
pip install -r requirements.txt
python main.py
Expected Answer:
Both are subword tokenization methods, but BPE merges frequent symbol pairs while WordPiece uses a vocabulary learning approach based on the usefulness of word pieces.

Matched Keywords: ['subword', 'BPE', 'WordPiece', 'vocabulary']
Missing Keywords: []
Score: 100.0 %
Status: PASS

-----------------------------------
Question 7: Q007
Question: Why can Telugu text produce different token counts from English text?

LLM Answer:
Telugu text can produce different token counts from English text due to several reasons:

1. **Script and encoding**: Telugu is written in its own script, which is different from the Latin script used for English. The Telugu script has its own set of characters, which may not be recognized by all NLP tools and libraries. This can lead to differences in tokenization, as the same sequence of characters may be split or merged into...