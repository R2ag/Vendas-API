from flask import Flask, Blueprint, jsonify
from flask_restx import Api
from marshmallow import ValidationError

from ma import ma 
from db import db

from resources.cliente import Cliente, ClienteList, cliente_ns, clientes_ns
from resources.carrinho import Carrinho, CarrinhoList, carrinho_ns, carrinhos_ns
from resources.produto import Produto, ProdutoList, produto_ns, produtos_ns
from resources.venda import Venda, VendaList, venda_ns, vendas_ns



app = Flask(__name__)
bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp, doc='/doc', title='Api flask')
app.register_blueprint(bp)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api.add_namespace(cliente_ns)
api.add_namespace(clientes_ns)
api.add_namespace(carrinho_ns)
api.add_namespace(carrinhos_ns)
api.add_namespace(produto_ns)
api.add_namespace(produtos_ns)
api.add_namespace(venda_ns)
api.add_namespace(vendas_ns)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

cliente_ns.add_resource(Cliente, '/<int:id>')
clientes_ns.add_resource(ClienteList, "")
carrinho_ns.add_resource(Carrinho, '/<int:id>')
carrinhos_ns.add_resource(CarrinhoList, "")
produto_ns.add_resource(Produto, '/<int:id>')
produtos_ns.add_resource(ProdutoList, "")
venda_ns.add_resource(Venda, '/<int:id>')
vendas_ns.add_resource(VendaList, "")


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True,host='0.0.0.0')