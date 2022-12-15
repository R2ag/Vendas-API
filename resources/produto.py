from flask import request
from flask_restx import Resource, fields, Namespace

from models.produto import ProdutoModel
from schemas.produto import ProdutoSchema

PRODUTO_NOT_FOUND = "Produto Não encontrado"
PRODUTO_ALREADY_EXISTS = "Produto {} Ja existe."

produto_ns = Namespace('produto', description='Operaçoes relacionadas a produto')
produtos_ns = Namespace('produtos', description='Operaçoes relacionadas a produtos')

produto_schema = ProdutoSchema()
produto_list_schema = ProdutoSchema(many=True)

produto = produto_ns.model('Produto',{
    'nome':fields.String('Nome do produto'),
    'preco': fields.Float(0)
})

class Produto(Resource):
    def get(self, id):
        produto_data = ProdutoModel.find_by_id(id)
        if produto_data:
            return produto_schema.dump(produto_data)
        return {'message': PRODUTO_NOT_FOUND}, 404
    
    def delete(self, id):
        produto_data = ProdutoModel.find_by_id(id)
        if produto_data:
            produto_data.delete_from_db()
            return {'message': "Store Deleted successfully"}, 200
        return {'message': PRODUTO_NOT_FOUND}, 404

class ProdutoList(Resource):
    @produtos_ns.doc('Todos os produtos')
    def get(self):
        return produto_list_schema.dump(ProdutoModel.find_all()), 200
    
    @produtos_ns.expect(produto)
    @produtos_ns.doc('Cadastro de produto')
    def post(self):
        produto_json = request.get_json()
        produto_data = produto_schema.load(produto_json)
        
        produto_data.save_to_db()
        
        return produto_schema.dump(produto_data), 201