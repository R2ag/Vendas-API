from ma import ma 
from models.produto import ProdutoModel
from models.carrinho import CarrinhoModel
from schemas.carrinho import CarrinhoSchema

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    carrinhos = ma.Nested(CarrinhoSchema, many=True)
    class Meta:
        model = ProdutoModel
        load_instance = True
        include_fk = True