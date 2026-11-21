### Week 3 (`Practical/week3/README.md`)

```markdown
# Week 3: Gemini API & Monitoring

*(Add a 1-sentence summary of your Week 3 lab objective here.)*

## Setup & Usage
```cmd
cd Practical/week3
pip install -r requirements.txt
python main.py
Enter your question (or type exit): What is 1+1 ?
API attempt 1 failed: 504 DEADLINE_EXCEEDED. {'error': {'code': 504, 'message': 'Deadline expired before operation could complete.', 'status': 'DEADLINE_EXCEEDED'}}
Log saved in MongoDB!

========== API MONITORING ==========
Request ID: bb63ef39-dd40-4885-89ab-a7a8812fa393
Attempt: 1
Status: failed
Input Tokens: 0
Output Tokens: 0
Total Tokens: 0
Latency: 28.208 seconds
Estimated Cost: $ 0.0
Retrying after 1.10 seconds...
Log saved in MongoDB!

========== API MONITORING ==========
Request ID: bb63ef39-dd40-4885-89ab-a7a8812fa393
Attempt: 2
Status: success
Input Tokens: 8
Output Tokens: 7
Total Tokens: 92
Latency: 2.14 seconds
Estimated Cost: $ 1.99e-05

========== GEMINI RESPONSE ==========
1 + 1 = 2