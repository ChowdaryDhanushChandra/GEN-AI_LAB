### Week 5 (`Practical/week5/TokenEconomics/README.md`)

```markdown
# Week 5: Token Economics & Budget Management

Tracks and enforces LLM token usage and cost budgets, verified with automated unit tests.

## Project Structure
- `budget.py` — Core logic for token counting, cost calculation, and budget limits.
- `test_budget.py` — Unit tests for validating budget calculations and edge cases.
- `requirements.txt` — Python dependencies.
- `.env` — API configuration (ignored by Git).

## Setup & Usage
```cmd
cd Practical/week5/TokenEconomics
pip install -r requirements.txt
python budget.py
pytest
TOKEN ECONOMICS REPORT
---------------------------
Input tokens/day:  2,400,000
Output tokens/day: 600,000
Total tokens/day:  3,000,000
Estimated daily cost:   $1.4400
Estimated monthly cost: $43.20
Peak RPM with margin: 36.0
Peak TPM with margin: 54000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: REVIEW

Recommendation: REVISE assumptions, limits, or design before build.