from pydantic import BaseModel

class Auth(BaseModel):
        password: str
        mobil_phone: str