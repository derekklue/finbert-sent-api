# main.py
from fastapi import FastAPI
from model_loader import FinBERTModel
from schemas import TextInput, PredictionOutput

app = FastAPI(title="FinBERT Sentiment API")

model = FinBERTModel()

@app.get("/")
def root():
    return {"message": "Welcome to FinBERT Sentiment API!"}

@app.post("/predict", response_model=PredictionOutput)
def predict_sentiment(input: TextInput):
    """Predict the sentiment of financial text."""
    result = model.predict(input.text)
    return result