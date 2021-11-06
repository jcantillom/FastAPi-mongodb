from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

         id : Optional [str]
         first_name :Optional [str]
         last_name : Optional [str]
         date_birth : Optional [str]
         address : Optional [str]
         token :  str
         password : Optional [str]
         email : Optional [str]
         mobil_phone: Optional [str]
         
        
