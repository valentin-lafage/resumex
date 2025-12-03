from typing import Optional

from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: str
