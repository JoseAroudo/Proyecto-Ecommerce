from config.database import Session
from models.producto import TransactionType as TransactionTypeModel
from schemas.transaction_type import TransactionType as TransactionType


class TransactionTypeServices:
    def __init__(self):
        self.db = Session()

    def create(self, transaction_type_data: TransactionType):
        transaction_type = TransactionTypeModel(**transaction_type_data.model_dump())
        self.db.add(transaction_type)
        self.db.commit()
        return {"message": "Transaction Type Created"}
