from sqlalchemy import Column, Integer, String
from database import Base

class VerticeModel(Base):
    __tablename__ = "vertices"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)