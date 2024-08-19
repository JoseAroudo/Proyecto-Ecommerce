from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from schemas.transaction_type import TransactionType
from services.transaction_type import TransactionTypeServices


transaction_type_router = APIRouter(
    prefix="/transaction_type",
    tags=["transaction_type"],
)

service =TransactionTypeServices()

@transaction_type_router.post("")
def create_transaction_type(request: Request, transaction_type: TransactionType):
    result = service.create(transaction_type)
    return JSONResponse(content=result, status_code=201)