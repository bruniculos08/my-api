from schemas import VerticeSchema, EdgeSchema
from repositories import GraphRepository

class GraphUseCase():

    def __init__(self):
        self.repository = GraphRepository()

    def get_vertices(self):
        vertice_models = self.repository.get_vertices()
        result = []
        for vertice in vertice_models:
            result.append({"id" : vertice.id, "name" : vertice.name})
        return result
    
    def get_edges(self):
        edge_models = self.repository.get_edges()
        result = []
        for edge in edge_models:
            result.append({
                "id" : edge.id,
                "start_vertice" : edge.start_vertice,
                "end_vertice" : edge.start_vertice,
                "name" : edge.name,
                "value" : edge.value
                })
        return result
    
    def add_vertice(self, vertice : dict):
        vertice_schema = VerticeSchema(**vertice)
        self.repository.add_vertice(vertice=vertice_schema)

    def add_edge(self, edge : dict):
        edge_schema = EdgeSchema(**edge)
        self.repository.add_edge(edge=edge_schema)