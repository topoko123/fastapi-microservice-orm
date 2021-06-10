from sqlalchemy import Column, Integer, String

from .config_db import Base

class Casts(Base):
    __tablename__ = 'casts'
    
    cast_id = Column(Integer, primary_key=True, index=True)
    cast_name = Column(String(60))
    nationality = Column(String(20))
    
