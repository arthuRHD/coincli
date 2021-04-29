from pydantic import BaseModel
from datetime import datetime


class Balance(BaseModel):
    amount: str
    currency: str

    @property
    def count(self):
        return float(self.amount)


class Wallet(BaseModel):
    id: str
    name: str
    primary: bool
    type: str
    balance: Balance
    created_at: str
    updated_at: str

    @property   
    def created_date(self):
        return datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ")

    @property
    def updated_date(self):
        return datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%SZ")
