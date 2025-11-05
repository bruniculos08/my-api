from pydantic import BaseModel

class EdgeSchema(BaseModel):
    start_vertice : int
    end_vertice : int
    name : str
    value : float