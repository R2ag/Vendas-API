from ma import ma 
from models.cliente import ClienteModel
from models.venda import VendaModel
from schemas.venda import VendaSchema

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    vendas = ma.Nested(VendaSchema, many=True)
    class Meta:
        model = ClienteModel
        load_instance = True
        include_fk = True