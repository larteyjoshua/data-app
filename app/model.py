from typing import List, Optional
from pydantic import BaseModel

class GenerateData(BaseModel):
    name: str
    job: str
    number: str
    company: str
    account: str
    swift: str
    balance: str
    code: str

    class Config():
        orm_mode = True