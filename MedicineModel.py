from pydantic import BaseModel

class Medicine(BaseModel):

    id: int
    name: str
    description: str
    used_disease: str
    stock_price:str
    sale_price:str
    stock_qty:int   
    