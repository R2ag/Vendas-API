from flask import request
from flask_restx import Resource, fields, Namespace

from models.cliente import ClienteModel
from schemas.cliente import ClienteSchema

ITEM_NOT_FOUND = "Cliente Nao encontrado"

cliente_ns = Namespace('cliente', description='operacoes relacionadas ao cliente')
clientes_ns = Namespace('clientes', description='operacoes relacionadas aos clientes')

cliente_schema = ClienteSchema()
cliente_list_schema = ClienteSchema(many=True)

cliente = cliente_ns.model('Cliente',{
    'nome':fields.String('Nome do cliente'),
    'cpf': fields.String('Cpf do cliente')
})

class Cliente(Resource):
    def get(self, id):
        cliente_data = ClienteModel.find_by_id(id)
        if cliente_data:
            return cliente_schema.dump(cliente_data)
        return {'message': ITEM_NOT_FOUND}, 404
    
    def delete(self,id):
        cliente_data = ClienteModel.find_by_id(id)
        if cliente_data:
            cliente_data.delete_from_db()
            return {'message': "Cliente Deletado com sucesso"}, 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    @cliente_ns.expect(cliente)
    def put(self, id):
        cliente_data = ClienteModel.find_by_id(id)
        cliente_json = request.get_json()
        
        if cliente_data:
            cliente_data.nome = cliente_json['nome']
            cliente_data.cpf = cliente_json['cpf']
        else:
            cliente_data = cliente_schema.load(cliente_json)
            
        cliente_data.save_to_db()
        return cliente_schema.dump(cliente_data), 200
    
class ClienteList(Resource):
    @clientes_ns.doc('Exibe todos os clientes')
    def get(self):
        return cliente_list_schema.dump(ClienteModel.find_all()), 200
    
    @clientes_ns.expect(cliente)
    @clientes_ns.doc('Inclusao de um cliente')
    def post(self):
        cliente_json = request.get_json()
        cliente_data = cliente_schema.load(cliente_json)
        cliente_data.save_to_db()
        
        return cliente_schema.dump(cliente_data), 201