from ma import ma
from models.carrinho import CarrinhoModel

class CarrinhoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CarrinhoModel
        load_instance = True
        load_only = ("venda", "produto", )
        include_fk = True