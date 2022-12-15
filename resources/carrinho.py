from flask import request
from flask_restx import Resource, fields, Namespace

from models.carrinho import CarrinhoModel
from schemas.carrinho import CarrinhoSchema

CARRINHO_NOT_FOUND = "carrinho Não encontrada"

carrinho_ns = Namespace('carrinho', description='Operaçoes relacionadas a carrinho')
carrinhos_ns = Namespace('carrinhos', description='Operaçoes relacionadas a carrinhos')

carrinho_schema = CarrinhoSchema()
carrinho_list_schema = CarrinhoSchema(many=True)

carrinho = carrinho_ns.model('carrinho',{
    'venda_id':fields.Integer('id da venda'),
    'produto_id': fields.Integer('id do produto'),
    'qtd': fields.Integer('qtd produto'),
    'preco': fields.Float('preco dos produtos')
                                 
})

class Carrinho(Resource):
    def get(self, id):
        carrinho_data = CarrinhoModel.find_by_id(id)
        if carrinho_data:
            return carrinho_schema.dump(carrinho_data)
        return {'message': CARRINHO_NOT_FOUND}, 404
    
    def delete(self, id):
        carrinho_data = CarrinhoModel.find_by_id(id)
        if carrinho_data:
            carrinho_data.delete_from_db()
            return {'message': "carrinho Deleted successfully"}, 200
        return {'message': CARRINHO_NOT_FOUND}, 404

class CarrinhoList(Resource):
    
    @carrinhos_ns.expect(carrinho)
    @carrinhos_ns.doc('Cadastro de carrinho')
    def post(self):
        carrinho_json = request.get_json()
        carrinho_data = carrinho_schema.load(carrinho_json)
        
        carrinho_data.save_to_db()
        
        return carrinho_schema.dump(carrinho_data), 201