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

Model: dereklu/finbert-local <br>
FinBERT is a domain-specific adaptation of BERT (Bidirectional Encoder Representations from Transformers) trained on financial text from corporate reports and news articles.

Labels: <br>
Positive <br>
Neutral <br>
Negative <br>


Visuals: <br>
<img width="679" height="607" alt="Screenshot 2025-11-02 at 3 59 27 PM" src="https://github.com/user-attachments/assets/9a492393-e83c-4ab1-a673-270735348fe3" />
<img width="689" height="696" alt="Screenshot 2025-11-02 at 4 47 10 PM" src="https://github.com/user-attachments/assets/9661658d-d599-4960-83e7-91ec974c6b1d" />



Live Demo (Coming Soon) <br>
Deployment to Render / Hugging Face Spaces will be added soon.

