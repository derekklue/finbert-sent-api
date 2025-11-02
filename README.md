# finbert-sent-api

FinBERT Sentiment Analysis API

A simple and production-ready REST API built with FastAPI that uses FinBERT, a transformer-based NLP model fine-tuned for financial sentiment analysis.
This API takes financial text (e.g., news, earnings reports, SEC filings) and returns a predicted sentiment label: positive, neutral, or negative — along with a confidence score.


Features

Text-to-Sentiment API – Analyze short or long financial text <br>
FastAPI backend – Async, high-performance Python API <br>
Transformer-powered – Uses FinBERT (yiyanghkust/finbert-tone) <br>
Extensible – Easily swap in any other Hugging Face sentiment model <br>
Interactive Swagger UI – Auto-generated docs at /docs <br>


Model Information

Model: yiyanghkust/finbert-tone
FinBERT is a domain-specific adaptation of BERT (Bidirectional Encoder Representations from Transformers) trained on financial text from corporate reports and news articles.

Labels:
Positive <br>
Neutral <br>
Negative <br>


Live Demo (Coming Soon)
Deployment to Render / Hugging Face Spaces will be added soon.

