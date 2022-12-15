from flask import request
from flask_restx import Resource, fields, Namespace

from models.venda import VendaModel
from schemas.venda import VendaSchema

VENDA_NOT_FOUND = "Venda Não encontrada"

venda_ns = Namespace('venda', description='Operaçoes relacionadas a venda')
vendas_ns = Namespace('vendas', description='Operaçoes relacionadas a vendas')

venda_schema = VendaSchema()
venda_list_schema = VendaSchema(many=True)

venda = venda_ns.model('venda',{
    'cliente_id':fields.Integer('id do Cliente')
})

class Venda(Resource):
    def get(self, id):
        venda_data = VendaModel.find_by_id(id)
        if venda_data:
            return venda_schema.dump(venda_data)
        return {'message': VENDA_NOT_FOUND}, 404
    
    def delete(self, id):
        venda_data = VendaModel.find_by_id(id)
        if venda_data:
            venda_data.delete_from_db()
            return {'message': "Venda Deleted successfully"}, 200
        return {'message': VENDA_NOT_FOUND}, 404

class VendaList(Resource):
    @vendas_ns.doc('Todos os vendas')
    def get(self):
        return venda_list_schema.dump(VendaModel.find_all()), 200
    
    @vendas_ns.expect(venda)
    @vendas_ns.doc('Cadastro de venda')
    def post(self):
        venda_json = request.get_json()
        venda_data = venda_schema.load(venda_json)
        
        venda_data.save_to_db()
        
        return venda_schema.dump(venda_data), 201