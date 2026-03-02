from fastapi import FastAPI
from services.ml_service import predict_ml
from services.nlp_service import analysis_sentiment
from pydantic import BaseModel
import joblib
from services.rag_service import generate_ticket_response

app = FastAPI()

# Load the real classification model
category_model = joblib.load("models/category.joblib")
priority_model = joblib.load("models/priority.joblib")
sentiment_model = joblib.load("sentiment.joblib")
@app.post("/ticket")
def process_ticket(ticket: dict):
    try:
        text = ticket.get("title", "") + " " + ticket.get("description", "")

        category = category_model.predict([text])[0]
        priority = priority_model.predict([text])[0]

        sentiment = sentiment_model.predict([text])[0]

        solution = generate_ticket_response(text, category, priority, sentiment)

        return {
            "Category": category,
            "Priority": priority,
            "Sentiment": sentiment,
             "AI_Response": solution
        }

    except Exception as e:
        return {"error": str(e)}
