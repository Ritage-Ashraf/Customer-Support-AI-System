# Customer-Support-AI-System
This project is an AI-powered customer support system that:

- Predicts Ticket Category
- Predicts Ticket Priority
- Detects Sentiment (VADER + TextBlob)
- Generates AI Responses using Ollama (RAG)

## Technologies Used
- Python
- FastAPI
- Scikit-learn
- TF-IDF
- Logistic Regression
- VADER
- TextBlob
- Ollama (LLM)

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run API:
   uvicorn app:app --reload

3. Test endpoint:
   POST /ticket
