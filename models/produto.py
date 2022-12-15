from db import db
from typing import List

class ProdutoModel(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float(precision=2), nullable=False)
    
    carrinhos = db.relationship("CarrinhoModel", lazy="dynamic", primaryjoin="ProdutoModel.id == CarrinhoModel.produto_id")
    
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __repr__(self):
        return f'Produto(nome={self.nome}, preco={self.preco})'
    
    def json(self):
        return{
            'nome': self.nome,
            'preco': self.preco
        }
        
    @classmethod
    def find_by_name(cls, name) -> "ProdutoModel":
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_id(cls, id) -> "ProdutoModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls) -> List["ProdutoModel"]:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()