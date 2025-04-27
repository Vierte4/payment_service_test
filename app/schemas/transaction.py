from pydantic import BaseModel, conint, condecimal, constr

class TransactionRequest(BaseModel):
    merchant_id: conint(gt=0)
    amount: condecimal(gt=0, max_digits=12, decimal_places=2)
    currency: constr(min_length=3, max_length=3)
    card_token: constr(min_length=1)

class TransactionResponse(BaseModel):
    transaction_id: str
    success: bool