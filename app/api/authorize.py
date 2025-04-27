from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from app.db.database import get_db
from app.db.models import Transaction
from app.schemas.transaction import TransactionRequest, TransactionResponse

router = APIRouter()

@router.post("/authorize", response_model=TransactionResponse)
def authorize_payment(request: TransactionRequest, db: Session = Depends(get_db)):
    # Создаем запись с начальным статусом 'initiated'
    new_tx = Transaction(
        transaction_id=str(uuid.uuid4()),
        merchant_id=request.merchant_id,
        amount=request.amount,
        currency=request.currency,
        card_token=request.card_token,
        status="initiated"
    )
    db.add(new_tx)
    db.commit()

    # Простейшая имитация логики авторизации:
    # "success", если amount <= 1000, иначе "fail"
    success = True
    if request.amount > 1000:
        success = False
    if success:
        new_tx.status = "authorized"
        db.commit()

    return {
        "transaction_id": new_tx.transaction_id,
        "success": success
    }