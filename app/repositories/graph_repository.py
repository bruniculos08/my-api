from database import Db
from schemas import VerticeSchema, EdgeSchema
from models import VerticeModel, EdgeModel


class GraphRepository():

    def get_vertices(self):
        with Db() as session:
            result = session.query(VerticeModel).all()
            return result
        
    def get_edges(self):
        with Db() as session:
            result = session.query(EdgeModel).all()
            return result
        
    def add_vertice(self, vertice : VerticeSchema):
        with Db() as session:
            vertice_model = VerticeModel(
                name = vertice.name
            )
            session.add(vertice_model)

    def add_edge(self, edge : EdgeSchema):
        with Db() as session:
            edge_model = EdgeModel(
                start_vertice=edge.start_vertice,
                end_vertice=edge.end_vertice,
                name=edge.name,
                value=edge.value
            )
            session.add(edge_model)