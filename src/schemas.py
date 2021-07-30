from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class PreRegistrationForm(BaseModel):
    pre_registration_id: int
    title: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email:str
    gender: str
    dob: date
    nationality: str

    class Config:
        orm_mode = True
        
