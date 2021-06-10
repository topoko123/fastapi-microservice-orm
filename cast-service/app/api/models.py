from pydantic import BaseModel

from typing import Optional


class CastBase(BaseModel):
    cast_name: str
    nationality: Optional[str] = None
    
    class Config:
        orm_mode = True
        
class CastId(CastBase):
    cast_id: int
    
class CastUpdate(CastBase):
    cast_name: Optional[str] = None
    
    class Config:
        orm_mode = True