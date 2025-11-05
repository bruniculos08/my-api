from fastapi import APIRouter
from schemas import VerticeSchema, EdgeSchema
from use_cases import GraphUseCase

router = APIRouter()

@router.get("/vertices/")
def get_vertices():
    result = GraphUseCase().get_vertices()
    return result

@router.get("/edges/")
def get_edges():
    result = GraphUseCase().get_edges()
    return result

@router.post("/vertices/post")
def post_vertice(name : str):
    vertice = {"name" : name}
    GraphUseCase().add_vertice(vertice)

@router.post("/edges/post")
def post_vertice(start_vertice : int, end_vertice : int, name : str, value : float):
    edge = {
        "start_vertice" : start_vertice,
        "end_vertice" : end_vertice,
        "name" : name,
        "value" : value
        }
    GraphUseCase().add_edge(edge)