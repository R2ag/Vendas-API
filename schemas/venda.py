from ma import ma 
from models.venda import VendaModel
from models.cliente import ClienteModel
from models.carrinho import CarrinhoModel
from schemas.carrinho import CarrinhoSchema

class VendaSchema(ma.SQLAlchemyAutoSchema):
    carrinhos = ma.Nested(CarrinhoSchema, many=True)
    class Meta:
        model = VendaModel
        load_instance = True
        load_only = ("cliente",)
        include_fk = True