from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database import Base

class EdgeModel(Base):
    __tablename__ = "edges"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_vertice = Column(Integer, ForeignKey("vertices.id"))
    end_vertice = Column(Integer, ForeignKey("vertices.id"))
    name = Column(String)
    value = Column(Float)