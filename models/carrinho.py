from db import db
from typing import List

class CarrinhoModel(db.Model):
    __tablename__ = "carrinho"
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
   
    produto_id = db.Column(db.Integer, db.ForeignKey("produto.id"),nullable=False)
    venda_id = db.Column(db.Integer, db.ForeignKey("venda.id"),nullable=False)
    
    def __init__(self, venda_id, produto_id, qtd) -> None:
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.qtd = qtd
        self.preco = self.produto.preco * qtd
        
    def __repr__(self) -> str:
        return f'Carrinho(id={self.id}, venda={self.venda_id}, Produto={self.produto_id}, qtd={self.qtd}, preco={self.preco})'
    
    @classmethod
    def find_by_venda(cls, id_venda) -> List["CarrinhoModel"]:
        return cls.query.filter_by(venda_id=id_venda)
    
    @classmethod
    def find_by_produto(cls, id_produto) -> List["CarrinhoModel"]:
        return cls.query.filter_by(produto_id=id_produto)
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()