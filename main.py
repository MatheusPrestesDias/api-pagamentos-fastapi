from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
import uuid

app = FastAPI()

# Lista de status permitidos
ALLOWED_STATUS = ["pending", "approved", "rejected", "cancelled"]

class Payment(BaseModel):
    id: str
    amount: float
    status: str

class PaymentCreate(BaseModel):
    amount: float
    status: Optional[str] = Field(default="pending", description="Status do pagamento. Ex: pending, approved, rejected, cancelled")

payments_db = {}

@app.post("/payments", response_model=Payment)
def create_payment(payment: PaymentCreate):
    if payment.status not in ALLOWED_STATUS:
        raise HTTPException(status_code=400, detail=f"Status inválido. Use um dos: {ALLOWED_STATUS}")
    payment_id = str(uuid.uuid4())
    new_payment = Payment(id=payment_id, amount=payment.amount, status=payment.status)
    payments_db[payment_id] = new_payment
    return new_payment

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: str):
    payment = payments_db.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.get("/payments", response_model=List[Payment])
def list_payments():
    return list(payments_db.values())
