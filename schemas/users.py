from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    username: str
    first_name: str
    last_name: str
    dni: str
    phone: str
    email: str
    password: str
    created_at: Optional[str]
    updated_at: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_blocked: Optional[bool]
    last_login: Optional[str]
    date_joined: Optional[str]
    avatar: Optional[bytes]
    role: Optional[str]
