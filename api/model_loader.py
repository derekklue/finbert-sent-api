# model_loader.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class FinBERTModel:
    def __init__(self):
        model_name = "yiyanghkust/finbert-tone"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = ["neutral", "positive", "negative"]

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)
            confidence, label_id = torch.max(probs, dim=1)
        return {
            "label": self.labels[label_id],
            "confidence": round(confidence.item(), 4)
        }