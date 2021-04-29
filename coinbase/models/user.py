from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str
    native_currency: str
    has_made_a_purchase: bool
    has_blocking_buy_restrictions: bool
    has_buy_deposit_payment_methods: bool
    
