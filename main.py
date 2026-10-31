from pathlib import Path
import json
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Retail Transactions API",
    description="Synthetic online marketplace transactions for an ETL teaching project.",
    version="1.0.0",
)

DATA_FILE = Path(__file__).with_name("transactions.json")

def load_transactions():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

@app.get("/")
def root():
    return {"message": "Retail Transactions API", "docs": "/docs"}

@app.get("/transactions")
def get_transactions():
    return load_transactions()

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    for transaction in load_transactions():
        if transaction["transaction_id"] == transaction_id:
            return transaction
    raise HTTPException(status_code=404, detail="Transaction not found")
